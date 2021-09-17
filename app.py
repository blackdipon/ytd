#!/usr/bin/env python

from pytube import YouTube, exceptions
from clipboard import paste
import ffmpeg


# Get file link
def get_file_link():
    response = input("Copy from clipboard (y/n): ") # Prompt for coping from Clipboard
    if response == "y":
        # Get link From Clipboard and check if Empty.
        try:
            link = paste()
            if link == "":
                print("Clipboard Empty")
                return None
            else:
                return link
        except:
            print("Error copping link")
            return None

    elif response == "n":
        link = input("Input the link here : ") # Link Input Prompt
        return link
    else:
        print("Invalid Response")
        return None

def process_link(link):
    # Initiate the file object and return the object
    try:
        file = YouTube(link)
        return file
    except exceptions.RegexMatchError:
        print('Error Getting video.Please check the URL.')
        return None
    except exceptions.VideoUnavailable:
        print("Video is unavailable.")
        return None
    except:
        print("Error")
        return None

def get_stream(file):
    preferde_videos = ("360p","480p","720p","1080p")
    preferde_audio = ("128kbps","160kbps")
    info={0: file.title}
    stream = file.streams
    i=1

    for video in preferde_videos:
        x = stream.filter(resolution=video).first()
        if x:
            info[i] = x
            i = i+1

    for audio in preferde_audio:
        x = stream.filter(abr=audio).first()
        if x:
            info[i] = x
            i = i+1

    return info    

    # info['video'] = file.streams.filter(type="video",progressive=True).order_by("resolution")
    # info['1080'] = file.streams.filter(resolution="1080p").first()
    # info['audio'] = file.streams.filter(only_audio=True).order_by("abr")

# def arrange_stream(info):
#     stream_list={}
#     i = 1
#     for video in info['video']:
#         if video.resolution > "144p"

#     for audio in info['audio']:
#         pass

#     return stream_list

# Main function
if __name__ == "__main__" :
    link = get_file_link()

    if link:
        file = process_link(link)

    if file:
        info = get_stream(file)
    
    print(info)
