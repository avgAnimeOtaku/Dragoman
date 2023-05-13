from pytube import Channel

channel_id = "https://www.youtube.com/channel/UCEBb1b_L6zDS3xTUrIALZOw"

channel = Channel(channel_id)
with open("data/mit_links.txt", "w") as f:
    for video in channel.videos:
        f.write(video.watch_url)
        f.write("\n")