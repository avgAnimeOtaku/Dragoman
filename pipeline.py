import os
import mimetypes
from google.cloud import storage
from google.cloud import speech
from google.cloud import translate_v2 as translate
import aspose.words as aw

count = 0

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "api/key.json"

STORAGE_CLASSES = ('STANDARD', 'NEARLINE', 'COLDLINE', 'ARCHIVE')
speech_client = speech.SpeechClient()
translate_client = translate.Client()
target = "hi"
doc = aw.Document()

class GCStorage:
    def __init__(self, storage_client):
        self.client = storage_client

    def get_bucket(self, bucket_name):
        return self.client.get_bucket(bucket_name)

    def upload_file(self, bucket, blob_destination, file_path):
        content_type = mimetypes.guess_type(file_path)[0]
        blob = bucket.blob(blob_destination)
        blob.upload_from_filename(file_path, content_type=content_type)
        return blob

    def list_blobs(self, bucket_name):
        return self.client.list_blobs(bucket_name)


# Step 2. construct GCStorage instance
storage_client = storage.Client()
gcs = GCStorage(storage_client)

# Step 3. Create gcp_api_demo Cloud Storage bucket
bucket_gcs = gcs.get_bucket("dragoman-audio-files-for-speech-to-text")

for filename in os.listdir("data/wav2"):
    if os.path.isfile(os.path.join("data/wav2", filename)):
        print(filename)
        gcs.upload_file(bucket_gcs, filename, os.path.join("data/wav2", filename))
        audio_uri = "gs://dragoman-audio-files-for-speech-to-text/" + filename
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

        file = open(f"data/english/{filename}", "w")

        for result in response.results:
            print(result.alternatives[0].transcript + "\n")
            file.write(result.alternatives[0].transcript + "\n")

        with open(f"data/english/{filename}") as text_file:
            text = text_file.readlines()

        output = translate_client.translate(text, target_language=target)

        for key, value in output[0].items():
            if key == "translatedText":
                print(value)
                builder = aw.DocumentBuilder(doc)
                builder.write(str(count) + "\n" + "https://youtube.com/watch?v=" + str(filename.split(".")[0].strip()) + "\n" + str(text) + "\n" + str(value) + "\n\n")
                count += 1


        gcs_demo_blobs = gcs.list_blobs(bucket_gcs)
        for blob in gcs_demo_blobs:
            blob.delete()

doc.save("data/hindi.docx")


