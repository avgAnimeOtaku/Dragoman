import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
from playsound import playsound
import pafy

r = sr.Recognizer()
t = Translator()

video_url = "https://youtu.be/zzOZ9awO9b4"

# Get the audio stream for the YouTube video
video = pafy.new(video_url)
bestaudio = video.getbestaudio()
audio_url = bestaudio.url

with sr.AudioFile(sr.AudioData(audio_url)) as source:
    audio = r.record(source)
try:
    speech_text = r.recognize_google(audio)
    print(speech_text)
except sr.UnknownValueError:
    print("Could not understand")
except sr.RequestError:
    print("Could not request result from google")

translated_text = t.translate(speech_text, dest='hi')
print(translated_text.text)

voice = gTTS(translated_text.text, lang='hi')
voice.save("voice.mp3")
playsound("voice.mp3")