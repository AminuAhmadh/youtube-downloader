# A YOUTUBE VIDEO DOWNLOADER
# BY AMINU AHMADH
# GITHUB @AminuAhmadh


from pytube import YouTube, Playlist
import pyinputplus
import time
import os
from pytube.cli import on_progress
from rich.progress import track


# path to save the file
def file_path():
    home = os.path.expanduser('~')
    download_path = os.path.join(home, 'downloads')
    return download_path

def pl_file_path():
    home = os.path.expanduser('~')
    download_path = os.path.join(home, 'downloads', pl.title)
    return download_path


# Get the file size
def file_size():
    if size < 1000000000:
        megabyte = size / 1000000
        print('SIZE:', round(megabyte), 'MB')
    elif size >= 1000000000:
        gigabyte = size / 1000000000
        print('SIZE:', round(gigabyte), 'GB')

print(""" Download YouTube Video, Playlist (in audio or video format) or single video Audio.
A - for Audio
V - for Video
P - for Playlist (both Video & Audio)""")

again = True
while again != False:
    content_type = pyinputplus.inputChoice(['A', 'V', 'P'])

<<<<<<< HEAD
try:
    yt = YouTube(link, on_progress_callback=on_progress)
    highest_resolution = yt.streams.get_highest_resolution()
    # prints out details of the video
    print('Getting Video...')
    print('TITLE:', yt.title)
    print('YOUTUBER/CHANNEL:', yt.author)
    size()
    quality = highest_resolution
    file_size = quality.filesize
    print('Downloading the video with highest resolution available...')
    print(f'RESOLUTION: {highest_resolution.resolution}')
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
=======
    if content_type == 'A':
        link = pyinputplus.inputURL('Enter the Youtube video Link to get its audio: \n')
        audio = YouTube(link, on_progress_callback=on_progress)
        size = audio.streams.get_audio_only().filesize
        file_size()
        print(f'Downloading your file:- {audio.title} ')
        try:
            audio.streams.get_audio_only().download(file_path())
        except Exception as e:
            print("Error occured due to:", e)
            exit()
        print(f'Downloaded on {file_path} folder')
    elif content_type == 'V':
        yt = YouTube(pyinputplus.inputURL('Enter the Youtube video Link: \n'), on_progress_callback=on_progress)
        size = yt.streams.get_audio_only().filesize
        file_size()
        print(f'Downloading your file:- {yt.title} ')
        try:
            yt.streams.get_highest_resolution().download(file_path())
        except Exception as e:
            print("Error occured due to:", e)
            exit()
        print(f'Downloaded on {file_path} folder')
    elif content_type == 'P':
        pl = Playlist(pyinputplus.inputURL('Enter the Youtube PlayList Link: \n'))
        print("""
        A - for Audio
        V - for Video""")
        type = pyinputplus.inputChoice(['A', 'V'], blank=True)
        if type == 'A':
            size = [video.streams.get_audio_only().filesize for video in pl.videos]
            size = sum(size)
            file_size()
            print(f'Downloading :- {pl.title}')
            length = pl.length
            print(f'{length} contents.')
            try:
                for content in track(pl.videos, "Downloading Playlist..."):
                    print(f'Downloading:- {content.title}')
                    content.streams.get_audio_only().download(pl_file_path())
                    print(f'Downloaded:- {content.title}')
                    print()
            except Exception as e:
                print("Error occured due to:", e)
                exit()
        elif type == 'V':
            size = [video.streams.get_highest_resolution().filesize for video in pl.videos]
            size = sum(size)
            file_size()
            print(f'Downloading :- {pl.title}')
            length = pl.length
            print(f'{length} contents.')
            try:
                for content in track(pl.videos, "Downloading Playlist..."):
                    print(f'Downloading:- {content.title}')
                    content.streams.get_highest_resolution().download(pl_file_path())
                    print(f'Downloaded:- {content.title}')
                    print()
            except Exception as e:
                print("Error occured due to:", e)
                exit()
    redo = pyinputplus.inputYesNo("Redo again? ")
    if redo == 'NO':
        again = False
    continue
>>>>>>> editing





#     print('YOUTUBER/CHANNEL:', yt.author)
#     desc = pyinputplus.inputYesNo(
#         prompt='Do you also wants to see the video description? ')
#     if desc == 'yes':
#         print('DESCRIPTION:', yt.description)
#     else:
#         pass
#     print('Getting Video...')
#     quality = highest_resolution
#     file_size = quality.filesize
#     print('Downloading the video with highest resolution available...')
#     print(f'RESOLUTION: {highest_resolution.resolution}')
#     size()
#     print('Downloading Your File...')
#     print()
#     try: 
#         quality.download(file_path())
#     except Exception as Downloaderror:
#         print("Error occured due to:", Downloaderror)
#         exit()
# except Exception as error:
#     print('Opps! an ERROR Occured. try: \n — Checking your connection \n — Url is a valid YouTube watch url \n — Or try again later ')
#     print("Your error occured due to:", error)
#     exit()

# print(f"Downloaded Successfully on location '{file_path()}'")
