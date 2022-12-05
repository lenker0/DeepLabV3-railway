import numpy as np
from PIL import Image
import os

images_dir = "/content/data/dataset/train_data/masks/"
IMAGES_NAME = os.listdir(images_dir)

for img in IMAGES_NAME:
  im = Image.open(images_dir + img)
  data = np.array(im)

  train = 10 # Original value of train
  rail_add = 6 # Original value of additional railroad
  rail = 7 # Original value of railroad
  black = 0 # Value that we want to replace it with

  red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]
  mask = (red == train) & (green == train) & (blue == train)
  data[:,:,:3][mask] = [black, black, black]

  red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]
  mask = (red == rail_add) & (green == rail_add) & (blue == rail_add)
  data[:,:,:3][mask] = [rail, rail, rail]

  im = Image.fromarray(data)
  im.save(images_dir + img)

