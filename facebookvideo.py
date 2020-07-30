#facebook video to audio
import requests as r
from pprint import pprint
from moviepy.editor import *
import os, re
from datetime import time   
from datetime import datetime
from bs4 import BeautifulSoup



def is_valid():
    
    while True:
        url = input("Enter a Facebook Video URL: ")
        regex = re.compile(
            r'^(http:\/\/|https:\/\/)[a-z0-9]+([\-\.]facebook+)\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?\W*(videos)\W*?\/?(\d+)$'
            #r'^(?:http|ftp)s?://' # http:// or https://
            # r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
            # r'localhost|' #localhost...
            # r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
            # r'(?::\d+)?' # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
            
        
        valid =(re.match(regex, url) is not None) # True
      
        if valid == True:
             print(f"{url}, is a valid URL!")
             break
        else:
            print("Please insert a valid url")
            print("Make sure that the url contains \"http://\" or \"https://\" ")
            continue
        print("Please insert a valid Facebook Video URL")
        
        
    
is_valid()

"""     
### Sermon title
sermonTitle = "ThePathSermon-" + str(datetime.today().strftime("%Y-%m-%d"))

#finds mp4 file through parsing html using Beautiful soup
url = 'https://www.facebook.com/ThePathChurch/videos/972778836528420' #<--- URL HERE
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
 """