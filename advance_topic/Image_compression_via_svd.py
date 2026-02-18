import requests
from PIL import Image
import matplotlib.pyplot as plt
from io import BytesIO
import numpy as np

url = "https://raw.githubusercontent.com/jonkrohn/DLTFpT/master/notebooks/oboe-with-book.jpg"

response = requests.get(url)
img = Image.open(BytesIO(response.content))

plt.imshow(img)
# plt.axis("off")


imggray = img.convert('L')
plt.imshow(imggray)
# convert image data to numpy matrix
imgmat = np.array(imggray, dtype=float)
# plt.imshow(imgmat, cmap='gray')
plt.show()

U, sigma, V = np.linalg.svd(imgmat)