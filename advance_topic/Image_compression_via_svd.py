import requests 
from PIL import Image
import os
import matplotlib.pyplot as plt
from io import BytesIO
import numpy as np

'''
# Image from online
url = "https://raw.githubusercontent.com/jonkrohn/DLTFpT/master/notebooks/oboe-with-book.jpg"

response = requests.get(url)
img = Image.open(BytesIO(response.content))
'''

'''
# Image from local (more stable technique)
base_dir = os.path.dirname(__file__)
img_path = os.path.join(base_dir, "..", "assets", "350z.jpg")

img = Image.open(img_path)
print(os.getcwd())
'''


img = Image.open("assets/350z.jpg") # terminal: python advance_topic/Image_compression_via_svd.py
# plt.imshow(img)
# plt.axis("off")


imggray = img.convert('L')
# plt.imshow(imggray)
# convert image data to numpy array 2D matrix
imgmat = np.array(imggray, dtype=float)
# plt.imshow(imgmat, cmap='gray')


U, sigma, V = np.linalg.svd(imgmat)

# reconstimg = np.matrix(U[:, :1]) * np.diag(sigma[:1]) * np.matrix(V[:1, :])
# plt.imshow(reconstimg, cmap='gray')

U = np.matrix(U)
V = np.matrix(V)

plt.figure(figsize=(12, 8))


for idx,i in enumerate([1, 2, 4, 8, 16, 32, 64])                    :
    reconstimg = U[:, :i] * np.diag(sigma[:i]) * V[:i, :]
    plt.subplot(3, 3, idx + 1)   # 2 rows, 3 columns
    plt.imshow(reconstimg, cmap='gray')
    title = "n = %s" % i  # n = n set of sigular values
    plt.title(title)
    
plt.subplot(3, 3, 8)
plt.imshow(imgmat, cmap='gray')
plt.title("Original-greyscale")

plt.subplot(3, 3, 9)
plt.imshow(img)
plt.title("Original")

plt.tight_layout()
plt.show()