import os
import mimetypes
from google.cloud import storage
from google.cloud import speech
import json

file = input("enter the path of file: ")

speech_client = speech.SpeechClient()

x = r'{"type": "service_account", "project_id": "dragoman-381011", "private_key_id": "15203646ee8b1c34dd3e79446b5d18bff1b14743", "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCEgmxMzlKFMgxU\n9BKJyjAz2aNBtosetJVdIGDDwW0KKvorYYUuBgC5FPYrVYJ3obCYDpcLzkfhIa7O\nyVYDdC2jagzqSNu4ZdKOLVvgsGDUjF7ouNvKdeGkwuK2ZXPWSvvho3HjbDAgtSJl\nCEIQ0w5ukuNkQ2cISDkip427+1ZsPerboKHYMeb0hd/cEI78dRc76NG4HcMeqVKM\n6ToKH1gk8RxTMr0uYqE8O/6Dk5hWXF/ML/33SqPXy74cp8hJKLEuZThggqyKax04\nCcEAeVZvig9KFok9dHjvf8AXgg/MYqwS7apHanqmYr5h+HjqGyFjMTSgpp+QvWxl\n2Wha/yF7AgMBAAECggEAHgb8Ca+bbYl41+tzI/xITgecgjCed/fN/QtwQgvb7Lju\nddQkfNhpY4eHfSxkYz2lqd9shQVarn6WgU+IiUHTcbt/b7vQ5olUXFmU/2aYmrGw\ndCYn0EpENrTe8RwuUrotN+V00mdaxJ6nS6PCbNOW6qGom7jWaT8Mi3jSmm2LGP3f\ndY1UXk/cD5+TpEr7mp22n5QFHR9I++MtrDCaQhbxbMd7zjaaTdbc3QL+mIKbly6z\nYqGIyTerIGQyyvjsOsbdCxp935RKSXTrfPovwg22F4W3zYhLrlGoCG9QyHXorbLh\nLmdv/CZ3zgoTv0fK5RImcCcOW8stTDDeyrvnK2aQQQKBgQC7NYbC4QvxWrNGKWuT\n4uWiRoKHVZbMWZFplLwUA3Pndt40qZgK1Cf/VKCtU6JANdVrtx/46uCDHdNTQ2Ow\nFhHPfhUPHadJFXQiUJhloc2njLstr+FCoI0LBeVF8C4AX5FjtyMDmd7KWxrlLeZc\n3E1rl0SjiD5MoFn+MOgn06724QKBgQC1M2LxmxOldBzFPjV86HqGo7/zPq7IGpuZ\nEMC7T8FBJIRazLX5sUcMgYsnnjXG5sIJANx0OE/IS4WGDBIri7DI3eGC8t7NzUVc\nnDjj32C/XILOCHXCVf+tT9pFVy+iWbVTKW3V5k1f2nGEINLt/yIh8SHXHkbCnfQx\n1Et1qvLP2wKBgQCWVvfwDHZgzqvljmHcE3zCAsnUEQHW/Z7vIQihMdykZysvM3rs\nR1APllCqoN1Nn23S4O8GIOlHom4REa8+u5p1/RTAXNn4sQfgfsTD6VqUUUoH+JR3\nwyNBVOy4a5clqZnCcFHoFGt8KgnBPkkfDbQG0SXIBiOxuZxLq87kHPUHQQKBgQCP\nM1IhoK3xFwdZtiUtVsjmOOkMwl/80lJfsEawgYI4CjTzUU8LStfcgVBI+haD34A+\n/0g6LPqYT17xpf6CHX6T8A41n90HBg+n9epb5AAgm2rgiv0NnUtXW4EjRZjmlEDh\nvR8JaV2CwC7v/cTUw8nkyx00VcAUNCJ1ctJD5trH+wKBgBt8mxsYcZRaDNpy+5lK\nNYxi7IuqCajTbHJ/4M7xx5BiF7RwS/C4+UTrhSp2ZcZI6ysT1s8rpJ57BnmYbNby\noWfp8mQbkpCw4y3YG8A9bPYxbep/zHd6N6DzG6wM5gNUngKg9vHnsrmHLGggZsXb\nuPjsHk8C+1BmbsVWWc8PwKoC\n-----END PRIVATE KEY-----\n", "client_email": "dragoman@dragoman-381011.iam.gserviceaccount.com", "client_id": "117404857815706962500", "auth_uri": "https://accounts.google.com/o/oauth2/auth", "token_uri": "https://oauth2.googleapis.com/token", "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs", "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/dragoman%40dragoman-381011.iam.gserviceaccount.com"}'

key = json.load(x)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r'{"type": "service_account", "project_id": "dragoman-381011", "private_key_id": "15203646ee8b1c34dd3e79446b5d18bff1b14743", "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCEgmxMzlKFMgxU\n9BKJyjAz2aNBtosetJVdIGDDwW0KKvorYYUuBgC5FPYrVYJ3obCYDpcLzkfhIa7O\nyVYDdC2jagzqSNu4ZdKOLVvgsGDUjF7ouNvKdeGkwuK2ZXPWSvvho3HjbDAgtSJl\nCEIQ0w5ukuNkQ2cISDkip427+1ZsPerboKHYMeb0hd/cEI78dRc76NG4HcMeqVKM\n6ToKH1gk8RxTMr0uYqE8O/6Dk5hWXF/ML/33SqPXy74cp8hJKLEuZThggqyKax04\nCcEAeVZvig9KFok9dHjvf8AXgg/MYqwS7apHanqmYr5h+HjqGyFjMTSgpp+QvWxl\n2Wha/yF7AgMBAAECggEAHgb8Ca+bbYl41+tzI/xITgecgjCed/fN/QtwQgvb7Lju\nddQkfNhpY4eHfSxkYz2lqd9shQVarn6WgU+IiUHTcbt/b7vQ5olUXFmU/2aYmrGw\ndCYn0EpENrTe8RwuUrotN+V00mdaxJ6nS6PCbNOW6qGom7jWaT8Mi3jSmm2LGP3f\ndY1UXk/cD5+TpEr7mp22n5QFHR9I++MtrDCaQhbxbMd7zjaaTdbc3QL+mIKbly6z\nYqGIyTerIGQyyvjsOsbdCxp935RKSXTrfPovwg22F4W3zYhLrlGoCG9QyHXorbLh\nLmdv/CZ3zgoTv0fK5RImcCcOW8stTDDeyrvnK2aQQQKBgQC7NYbC4QvxWrNGKWuT\n4uWiRoKHVZbMWZFplLwUA3Pndt40qZgK1Cf/VKCtU6JANdVrtx/46uCDHdNTQ2Ow\nFhHPfhUPHadJFXQiUJhloc2njLstr+FCoI0LBeVF8C4AX5FjtyMDmd7KWxrlLeZc\n3E1rl0SjiD5MoFn+MOgn06724QKBgQC1M2LxmxOldBzFPjV86HqGo7/zPq7IGpuZ\nEMC7T8FBJIRazLX5sUcMgYsnnjXG5sIJANx0OE/IS4WGDBIri7DI3eGC8t7NzUVc\nnDjj32C/XILOCHXCVf+tT9pFVy+iWbVTKW3V5k1f2nGEINLt/yIh8SHXHkbCnfQx\n1Et1qvLP2wKBgQCWVvfwDHZgzqvljmHcE3zCAsnUEQHW/Z7vIQihMdykZysvM3rs\nR1APllCqoN1Nn23S4O8GIOlHom4REa8+u5p1/RTAXNn4sQfgfsTD6VqUUUoH+JR3\nwyNBVOy4a5clqZnCcFHoFGt8KgnBPkkfDbQG0SXIBiOxuZxLq87kHPUHQQKBgQCP\nM1IhoK3xFwdZtiUtVsjmOOkMwl/80lJfsEawgYI4CjTzUU8LStfcgVBI+haD34A+\n/0g6LPqYT17xpf6CHX6T8A41n90HBg+n9epb5AAgm2rgiv0NnUtXW4EjRZjmlEDh\nvR8JaV2CwC7v/cTUw8nkyx00VcAUNCJ1ctJD5trH+wKBgBt8mxsYcZRaDNpy+5lK\nNYxi7IuqCajTbHJ/4M7xx5BiF7RwS/C4+UTrhSp2ZcZI6ysT1s8rpJ57BnmYbNby\noWfp8mQbkpCw4y3YG8A9bPYxbep/zHd6N6DzG6wM5gNUngKg9vHnsrmHLGggZsXb\nuPjsHk8C+1BmbsVWWc8PwKoC\n-----END PRIVATE KEY-----\n", "client_email": "dragoman@dragoman-381011.iam.gserviceaccount.com", "client_id": "117404857815706962500", "auth_uri": "https://accounts.google.com/o/oauth2/auth", "token_uri": "https://oauth2.googleapis.com/token", "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs", "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/dragoman%40dragoman-381011.iam.gserviceaccount.com"}'

STORAGE_CLASSES = ('STANDARD', 'NEARLINE', 'COLDLINE', 'ARCHIVE')

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


# Step 4. Upload Files
gcs.upload_file(bucket_gcs, "audio.wav", file)

# Step 5. Download & Delete Files
"""gcs_demo_blobs = gcs.list_blobs(bucket_gcs)
for blob in gcs_demo_blobs:
    blob.delete()"""

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

for result in response.results:
    print(result.alternatives[0].transcript + "\n")
