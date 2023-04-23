from __future__ import unicode_literals
import yt_dlp
import ffmpeg
import os
import pathlib
import mimetypes
from google.cloud import storage

ydl_opts = {
    'format': 'bestaudio/best',
#    'outtmpl': 'data/%(title)s.%(ext)s',
    'outtmpl': 'data/audio.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
    }],
}

STORAGE_CLASSES = ('STANDARD', 'NEARLINE', 'COLDLINE', 'ARCHIVE')

class GCStorage:
    def __init__(self, storage_client):
        self.client = storage_client

    def get_bucket(self, bucket_name):
        return self.client.get_bucket(bucket_name)

    def upload_file(self, bucket, blob_destination, file_path):
        content_type = mimetypes.guess_type(file_path)[0]
        blob = bucket.blob(blob_destination)
        blob.upload_from_filename(file_path, content_type=content_type)
        return blob

    def list_blobs(self, bucket_name):
        return self.client.list_blobs(bucket_name)

def download_from_url(url):
    ydl.download([url])
    stream = ffmpeg.input('output.m4a')
    stream = ffmpeg.output(stream, 'output.wav')

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    url=input("Enter Youtube URL: ")
    download_from_url(url)

def __init__main()
