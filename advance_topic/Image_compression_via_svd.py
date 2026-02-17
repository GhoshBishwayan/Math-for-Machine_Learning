import requests
from PIL import Image
import matplotlib.pyplot as plt
from io import BytesIO

url = "https://raw.githubusercontent.com/jonkrohn/DLTFpT/master/notebooks/oboe-with-book.jpg"

response = requests.get(url)
img = Image.open(BytesIO(response.content))

plt.imshow(img)
# plt.axis("off")
plt.show()

imggray = img.convert('LA')