from __future__ import unicode_literals
import yt_dlp
import ffmpeg

ydl_opts = {
    'format': 'bestaudio/best',
    #'outtmpl': 'data/%(title)s.%(ext)s',
    'outtmpl': 'data/audio.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
    }],
}

def download_from_url(url):
    ydl.download([url])
    stream = ffmpeg.input('output.m4a')
    stream = ffmpeg.output(stream, 'output.wav')

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    url=input("Enter Youtube URL: ")
    download_from_url(url)