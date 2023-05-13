from youtube_transcript_api import YouTubeTranscriptApi
srt = YouTubeTranscriptApi.get_transcript("9KNmqar0Dd8")

with open("caption.txt", "w") as f:
    for i in srt:
        f.write("%s\n" % i)