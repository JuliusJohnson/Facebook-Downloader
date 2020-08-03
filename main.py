#!/usr/bin/env python3
#Facebook Video to Audio Tool
import requests as r
from moviepy.editor import *
import os, re
from datetime import datetime
from bs4 import BeautifulSoup

today_datetime = str(datetime.today().strftime("%Y-%m-%d"))
file_location = os.path.abspath("output/")
    
def is_valid():
    #Performs a check to ensure that the a valid Facebook url is pasted
    while True:
        url = input("Enter a Facebook Video URL: ")
        regex = re.compile(
            r'^(http:\/\/|https:\/\/)[a-z0-9]+([\-\.]facebook+)\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?\W*(videos)\W*?\/?(\d+)$'
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
            
        valid =(re.match(regex, url) is not None) # True
      
        if valid == True:
             print(f"{url}, is a valid URL!")
             return url
             break
        else:
            print("Please insert a valid url")
            print("Make sure that the url contains \"http://\" or \"https://\" ")
            continue
        print("Please insert a valid Facebook Video URL")
        
def parse_html(url):
    #Finds mp4 file through parsing html using Beautiful Soup
    html = r.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    facebook_title = soup.title.string
    title = f"{today_datetime} - {facebook_title}"
    video_url = (soup.find_all('meta')[9].attrs['content'])
    video_url_alt = (soup.find("meta", property="og:video:secure_url").attrs['content'])

    try:
        r.get(video_url).status_code < 400
        return video_url, title
    except r.exceptions.MissingSchema: #Handles errors from request module
        r.get(video_url_alt).status_code <400
        return video_url_alt, title
    except:
        print('The link could not be parsed. Please try again. :(')

def download_video(video_url):
    #Downloads video and converts to audio
    os.chdir("output")
    print("Please be patient while the video is downloading...")
    video_requests = r.get(video_url[0], stream = True)
    with open('facebook2.mp4', 'wb') as f:
        for chunk in video_requests.iter_content(chunk_size = 5120*1024):
            if chunk:
                f.write(chunk)
    video = VideoFileClip('facebook2.mp4')
    video.audio.write_audiofile(video_url[1] +'.mp3')
    os.remove('facebook2.mp4')

def create_output():
    #Checks if output folder exists; if not creates "output"
    directory = ("output")
    check_folder = os.path.isdir(directory)
    if not check_folder:
        os.makedirs(directory)
        print(f"Created Folder: {directory}")
        
def main():
    #Executes previously defined functions
    create_output()
    file_path = os.path.abspath("output")
    download_video(parse_html(is_valid()))
    print(f'You may find your video at {file_path}')
    
if __name__ == "__main__":
    while True:
        try:
            main()
         
        except IndexError:
            print('The provided link is either a private video or the video is no longer live. Please try a different URL. :)')
            pass
        else:
            break