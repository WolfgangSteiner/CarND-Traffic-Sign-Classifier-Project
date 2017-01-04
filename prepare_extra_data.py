import csv
from PIL import Image
import numpy as np
import pickle

label_dict = {}

data = []
labels = []


for id,label in csv.reader(open('extra/labels.csv', 'r')):
    img = Image.open("extra/" + id + ".png")
    img_data = np.asarray(img)
    data.append(img_data)
    labels.append(label)

data = np.array(data)
labels = np.array(labels, dtype=np.int)

with open('extra/labels.pickle','wb') as f:
    pickle.dump(labels,f)

with open('extra/data.pickle','wb') as f:
    pickle.dump(data,f)
