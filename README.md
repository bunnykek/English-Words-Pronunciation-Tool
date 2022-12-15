# English-Words-Pronunciation-Tool
Tool to download the English words correct pronunciation, sourced from Google search.    
You can select any one amog these three accents: American, British and Indian.        

![tmp](https://ssl.gstatic.com/dictionary/static/pronunciation/20180801/desktop/t_d_s_z.svg)       

Using Google search engine is literally more easy and convenient lol, but I have made it just for fun.
Thought to make a telegram bot, send a word and get back its correct pronunciation video clip.

Requirements:
- LINUX (SVG to JPG conversion via CLI in Windows is 💀)
- ImageMagick (sudo apt install -y imagemagick librsvg2-dev)
- FFMPEG (sudo apt install -y ffmpeg)

`pip install -r requirements.txt`       
`python3 pronounce.py -h`
```
usage: pronounce.py [-h] [-A ACCENT] word

Tool to download the English words pronunciation.

positional arguments:
  word                  English Word

options:
  -h, --help            show this help message and exit
  -A ACCENT, --accent ACCENT
                        [IN, US, UK]
```                   
Example:
`python3 pronounce.py -A IN lolipop`    
(the clip will be saved in a Downloads folder at the project directory)
