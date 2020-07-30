#facebook video to audio
import requests as r
from pprint import pprint
from moviepy.editor import *
import os, re
from datetime import time   
from datetime import datetime
from bs4 import BeautifulSoup

url = input("Enter a Facebook Video URL:")

### Sermon title
sermonTitle = "ThePathSermon-" + str(datetime.today().strftime("%Y-%m-%d"))

#finds mp4 file through parsing html using Beautiful soup
url = 'www.facebook.com/ThePathChurch/videos/972778836528420' #<--- URL HERE
html = r.get(url)
soup = BeautifulSoup(html.text, 'html.parser')
video_url = (soup.find_all('meta')[9].attrs['content'])

print(video_url)

#Downloads video and converts to audio
video_requests = r.get(video_url, stream = True)
with open('facebook2.mp4', 'wb') as f:
    for chunk in video_requests.iter_content(chunk_size = 1024*1024):
        if chunk:
            f.write(chunk)

video = VideoFileClip('facebook2.mp4')
video.audio.write_audiofile(sermonTitle +'.mp3')

os.remove('facebook2.mp4')
