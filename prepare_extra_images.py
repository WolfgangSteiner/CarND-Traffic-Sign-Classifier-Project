from glob import glob
from PIL import Image
import pickle


for f in glob('extra/*.png'):
    img = Image.open(f)
    w,h = img.size
    if (w < h):
        y0 = (h-w) / 2
        rect = (0, y0, w, y0 + w)
        img = img.crop(rect)
    elif w > h:
        x0 = (w - h)/2
        rect = (x0, 0, x0+h, h)
        img = img.crop(rect)

    img = img.resize((32,32), Image.ANTIALIAS)
    img.save(f)
