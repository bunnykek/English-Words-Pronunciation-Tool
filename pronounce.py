#by bunnykek @ github
import requests
import os
import subprocess
import shutil
import argparse
from bs4 import BeautifulSoup

class pronounce:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(
            {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'})

    def process(self, word: str, accent: str):
        params = {
            'q': f'{word} pronunciation',
            'gl': accent
        }

        if not os.path.exists(word):
            os.makedirs(word)

        response = self.session.get(f"https://www.google.com/search", params=params)
        soup = BeautifulSoup(response.text, "lxml")
        concat_path =  self.download_jpgs(word, soup)
        audio_path = self.download_audio(word, soup)
        output_path = os.path.join("Downloads", f"{word}_{accent}.mp4")

        #multiplex using ffmpeg
        subprocess.Popen(["ffmpeg", "-hide_banner", "-loglevel", "error", "-i", concat_path, "-i", audio_path, output_path]).wait()
        shutil.rmtree(word)
        print("done for", word)

    def download_jpgs(self, word, soup):
        frames_data = soup.find_all("g-img", "qk2RKd")
        i = 0
        concat_path = os.path.join(word, "concat")
        with open(concat_path, "w") as concat:
            concat.write("ffconcat version 1.0\n")
            for frame in frames_data:
                frame_time_span = float(frame["data-viseme-duration"])/1000
                frame_url = "https:"+frame.find("img")["data-src"]
                svg_path = os.path.join(word, f"{i}.svg")
                jpg_path = os.path.join(word, f"{i}.jpg")
                with open(svg_path, "wb") as f:
                    f.write(self.session.get(frame_url).content)
                subprocess.Popen(["convert", "-density", "500", svg_path, jpg_path]).wait()
                os.remove(svg_path)
                concat.write(f"file {i}.jpg\nduration {frame_time_span}\n")
                i+=1
        return concat_path
    
    def download_audio(self, word, soup):
        audio_url = "https:"+soup.find("audio")["src"]
        audio_path = os.path.join(word, f"{word}.mp3")
        with open(audio_path, "wb") as audio:
            audio.write(self.session.get(audio_url).content)
        return audio_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Tool to download the English words pronunciation.")
    parser.add_argument('-A', '--accent', help="[IN, US, UK]", default="IN", type=str)
    parser.add_argument('word', help="English Word")
    args = parser.parse_args()
    accent = args.accent
    word = args.word
    pr = pronounce()
    pr.process(word, accent)
        
