import os
from google.cloud import speech

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "api/key.json"

speech_client = speech.SpeechClient()

"""audio_file = "audio.wav"

with open(audio_file, "rb") as file:
    byte_data = file.read()
audio = speech.RecognitionAudio(content=byte_data)

config_audio = speech.RecognitionConfig(
    sample_rate_hertz=48000,
    enable_automatic_punctuation=True,
    language_code='en-US'#,
    #audio_channel_count=2
)

response_standard = speech_client.recognize(
    config=config_audio,
    audio=audio
)
print(response_standard)"""

audio_uri = "gs://dragoman-audio-files-for-speech-to-text/audio.wav"
audio = speech.RecognitionAudio(uri=audio_uri)

config = speech.RecognitionConfig(
    sample_rate_hertz=48000,
    enable_automatic_punctuation=True,
    language_code='en-US',
    use_enhanced=True,
    model='video',
    audio_channel_count=2
)

operation = speech_client.long_running_recognize(config=config, audio=audio)
response = operation.result(timeout=90)

file = open("data/english.txt", "w")

for result in response.results:
    print(result.alternatives[0].transcript + "\n")
    file.write(result.alternatives[0].transcript + "\n")

