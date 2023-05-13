from __future__ import unicode_literals
import yt_dlp
import ffmpeg
import os

ydl_opts = {
    'format': 'bestaudio/best',
    #'outtmpl': 'data/wav/%(title)s.%(ext)s',
    'outtmpl': 'data/wav2/audio.%(ext)s',
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
    with open('data/links.txt', 'r') as f:
        for line in f:
            name = line.split("=")[1].strip()
            download_from_url(line.strip())
            os.rename("data/wav2/audio.wav", "data/wav2/" + name + ".wav")


