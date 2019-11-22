import os
import json
import base64
import requests
from PIL import Image

path = "imagens/"
dirs = os.listdir(path)

data = {}

for files in dirs:
    with open(("imagens/"+files), "rb") as img_file:
        codigo = base64.b64encode(img_file.read())
    data[files] = codigo

r = requests.get('http://34.95.155.151/index.php', json = data)

for files in dirs:
    os.remove("imagens/"+files)