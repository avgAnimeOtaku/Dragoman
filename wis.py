import whisper

model = whisper.load_model("medium.en")
result = model.transcribe("data/OpenAI Whisper Demo： Convert Speech to Text in Python.wav", fp16=False,)
print(result["text"])
file = open("data/english.txt", "w")
file.write(result["text"])