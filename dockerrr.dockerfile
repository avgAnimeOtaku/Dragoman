FROM python:3

ADD main.py .

RUN pip install yt_dlp youtube_dl ffmpeg

CMD ["python", "./main.py"]