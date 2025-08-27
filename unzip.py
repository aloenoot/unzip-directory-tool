from zipfile import ZipFile
import os

path = "./"

for file in os.listdir(path):
    if file.endswith(".zip"):
        file_name = os.path.abspath(file)
        with ZipFile(file_name, 'r') as zip:
            zip.extractall()
            zip.close()
        # os.remove(file_name)
