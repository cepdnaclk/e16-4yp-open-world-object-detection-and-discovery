import json
from torchvision import transforms as T
import math

def get_objects(annotation_file, image_names, features, FH, FW):

    objects = {}
    

    with open(annotation_file, 'r') as file:
        _data = json.load(file)
        _images = _data["images"]
        _annotations =  _data["annotations"]
  
        for idx, img_name in enumerate(image_names):

            feature = features[idx]
            img_id = int(img_name.split('.')[0])
            H : float
            W : float

            for img in _images:
                if (img["id"] == img_id):
                    H, W = img["height"], img["width"]
                    break

            for ann in _annotations:
                if(ann["image_id"] == img_id):
                    object_id = str(ann["id"]) 
                    objects[object_id] = {}
                    objects[object_id]["image_id"] = ann["image_id"]
                    objects[object_id]["category"] = ann["category_id"]
                    objects[object_id]["bbox"] = ann["bbox"]

                    #crop object from the feature
                    [x_min, y_min, width, height] = ann["bbox"]

                    x_min = math.floor((x_min*FW)/(W*4))
                    width = math.ceil((width*FW)/(W*4))
                    y_min = math.floor((y_min*FH)/(H*4))
                    height = math.ceil((height*FH)/(H*4))
                    
                    

                    object_feature = feature[:, y_min:y_min+height, x_min:x_min+width]
                    objects[object_id]["object_feature"] = object_feature.detach()
                    objects[object_id]["object_shape"] = object_feature.shape
         
    return objects
