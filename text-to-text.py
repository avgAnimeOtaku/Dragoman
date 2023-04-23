import os
from google.cloud import translate_v2 as translate

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "api/key.json"
translate_client = translate.Client()

target = "hi"
with open("data/english.txt") as text_file:
    text = text_file.readlines()

output = translate_client.translate(text, target_language=target)

for key, value in output[0].items():
    if key == "translatedText":
        print(value)
        file = open("data/hindi.txt", "w")
        file.write(str(value.encode("utf-8")))
