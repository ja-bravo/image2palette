from image import getWithPalette
from PIL import Image
from pathlib import Path

imgPath = f'{Path(__file__).parent.parent.name}/test-images/1.jpg'
baseImage = Image.open(imgPath)
newImage = getWithPalette(baseImage)
newImage.show()
