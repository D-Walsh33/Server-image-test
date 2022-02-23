import urllib.request
from PIL import Image
import requests

response = requests.get(
    'http://flip3.engr.oregonstate.edu:3331/micro?query=monkey')
res = response.json()['micro']
urllib.request.urlretrieve(res, "myImage.png")

img = Image.open('myImage.png')

img.show()
