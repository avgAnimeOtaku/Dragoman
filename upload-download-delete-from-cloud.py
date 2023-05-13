import os
import mimetypes
from google.cloud import storage

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "api/key.json"

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
gcs.upload_file(bucket_gcs, "audio.wav", r"data/audio.wav")

# Step 5. Download & Delete Files
"""gcs_demo_blobs = gcs.list_blobs(bucket_gcs)
for blob in gcs_demo_blobs:
    blob.delete()"""

