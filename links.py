from pytube import Channel

channel_id = "https://www.youtube.com/channel/UC640y4UvDAlya_WOj5U4pfA"

channel = Channel(channel_id)
with open("data/video_links.txt", "w") as f:
    for video in channel.videos:
        f.write(video.watch_url)
        f.write("\n")