import os
import torch
import torchvision
from PIL import Image
from torchvision import transforms as T
import torch.nn as nn

# image_dir = './data/coco/images'
def get_features(image_dir, FH, FW):
  images = []
  image_names = []

  for filename in os.listdir(image_dir):
    image = Image.open(image_dir + '/' + filename)
    transform = T.Compose([T.PILToTensor(), T.Resize((FH, FW))])
    image_tensor = transform(image)

    #omit b&w images : 000000100896.jpg etc.
    if(image_tensor.shape == torch.Size([1, FH, FW])):
      # print(filename)
      continue

    images.append(image_tensor)
    image_names.append(filename)

    #first 100 images are considered (o.w. process killed for 10325 images)
    if(len(images) == 100):
      break


  image_set = torch.stack(images) 
  print("Image set created with shape ", image_set.shape)


  model = torchvision.models.resnet50(pretrained = True)
  # print(model)

  features = image_set.to(torch.float32)

  layers = [model.conv1, model.bn1, model.relu, model.maxpool, model.layer1]

  for layer in layers:
    features = layer(features)
    # print("Shape after passing through ", layer, features.shape)
    
  print("Features created with shape", features.shape)

  return image_names, features.detach()

