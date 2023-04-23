import requests
import json
import os
from pydub import AudioSegment



os.system("python3 gentle/align.py data/Steve-Jobs-on-Failure.mp4 data/hindi.txt -o alignment.json")

"""
# Load the alignment data from the JSON file
with open('alignment.json', 'r') as f:
    alignment = json.load(f)

# Generate Hindi audio from the aligned text using pyttsx3 TTS engine
hindi_audio = AudioSegment.empty()
for word in alignment['words']:
    start_time = word['start']
    end_time = word['end']
    hindi_text = word['alignedWord']
    engine.save_to_file(hindi_text, 'temp.wav')
    engine.runAndWait()
    hindi_audio += AudioSegment.from_file('temp.wav')

# Adjust the timing of the Hindi audio to match the original English audio
hindi_audio = hindi_audio.set_frame_rate(audio.fps)
hindi_audio = hindi_audio.set_channels(audio.nchannels)
hindi_audio = hindi_audio.set_sample_width(audio.sample_width)
hindi_audio = hindi_audio.set_start_tstamp(audio.start)
hindi_audio = hindi_audio.set_end_tstamp(audio.end)

# Combine the original English audio track with the TTS-generated Hindi audio track
mixed_audio = audio.overlay(hindi_audio)

# Export the mixed audio file
mixed_audio.export('mixed_audio.mp3', format='mp3')"""