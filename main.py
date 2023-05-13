import os

folder_path = '' # Replace with the path to your folder

for filename in os.listdir("data/wav2"):
    if os.path.isfile(os.path.join("data/wav2", filename)):
        print(filename)