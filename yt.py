import pafy
import speech_recognition as sr

# Get the YouTube video URL from the user
video_url = "https://youtu.be/zzOZ9awO9b4"

# Get the audio stream for the YouTube video
video = pafy.new(video_url)
bestaudio = video.getbestaudio()
audio_url = bestaudio.url

# Set up the recognizer

r = sr.Recognizer()

# Read the audio stream
with sr.AudioFile(sr.AudioData(audio_url)) as source:
    audio = r.record(source)

# Recognize the speech
try:
    text = r.recognize_google(audio)
    print(text)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand the audio")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")
