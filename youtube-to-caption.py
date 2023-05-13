import yt_dlp
import requests

# Define the URL of the YouTube video to download captions from
VIDEO_URL = "https://youtu.be/9KNmqar0Dd8"

# Set options for yt_dlp to write subtitles and automatic captions in the English language
ydl_opts = {
    'writesubtitles': True,
    'writeautomaticsub': True,
    'subtitleslangs': ['en']
}

# Use yt_dlp to get the info about the YouTube video
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    video_info = ydl.extract_info(VIDEO_URL, download=False)

# Try to open and read the caption file for the downloaded video
try:
    captions_url = video_info['subtitles']['en']['url']
    response = requests.get(captions_url)
    captions = response.content.decode('utf-8')
    with open(f"{video_info['title']}.txt", 'w', encoding='utf-8') as f:
        f.write(captions)
    print("Captions downloaded successfully")

# If the caption file is not found, fall back to automatic captions
except KeyError:
    print("Captions not found, falling back to automatic captions")
    auto_caption_url = f"https://www.youtube.com/api/timedtext?v={video_info['id']}&lang=en&fmt=vtt"
    response = requests.get(auto_caption_url)
    if response.ok:
        with open(f"{video_info['title']}.txt", "w", encoding='utf-8') as f:
            f.write(response.content.decode('utf-8'))
        print("Automatic captions downloaded successfully")
    else:
        print("Automatic captions not available")
