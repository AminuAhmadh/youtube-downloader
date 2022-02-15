# A YOUTUBE VIDEO DOWNLOADER
# BY AMINU AHMADH
# GITHUB @AminuAhmadh


from pytube import YouTube
import pyinputplus
import time
import os
from pytube.cli import on_progress
from pytube.request import filesize


# path to save the file
def file_path():
    home = os.path.expanduser('~')
    download_path = os.path.join(home, 'videos')
    return download_path


# Get the file size
def size():
    if highest_resolution.filesize < 1000000000:
        megabyte = highest_resolution.filesize / 1000000
        print('SIZE:', round(megabyte), 'MB')
    elif highest_resolution.filesize >= 1000000000:
        gigabyte = highest_resolution.filesize / 1000000000
        print('SIZE:', round(gigabyte), 'GB')


print('A Youtube Video downloader')
link = pyinputplus.inputURL('Enter the Youtube video Link: \n')
print('Got the link!')
print('Processing...')

try:
    yt = YouTube(link, on_progress_callback=on_progress)
    highest_resolution = yt.streams.get_highest_resolution()
    # prints out details of the video
    print('TITLE:', yt.title)
    print('YOUTUBER/CHANNEL:', yt.author)
    desc = pyinputplus.inputYesNo(
        prompt='Do you also wants to see the video description? ')
    if desc == 'yes':
        print('DESCRIPTION:', yt.description)
    else:
        pass
    print('Getting Video...')
    quality = highest_resolution
    file_size = quality.filesize
    print('Downloading the video with highest resolution available...')
    print(f'RESOLUTION: {highest_resolution.resolution}')
    size()
    print('Downloading Your File...')
    print()
    try: 
        quality.download(file_path())
    except Exception as Downloaderror:
        print("Error occured due to:", Downloaderror)
        exit()
except Exception as error:
    print('Opps! an ERROR Occured. try: \n — Checking your connection \n — Url is a valid YouTube watch url \n — Or try again later ')
    print("Your error occured due to:", error)
    exit()

print(f"Downloaded Successfully on location '{file_path()}'")
