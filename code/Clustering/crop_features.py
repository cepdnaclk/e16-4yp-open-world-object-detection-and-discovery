import torch
from get_features import get_features
from get_objects import get_objects

def crop_features(annotation_file, image_dir, FH, FW):

    image_names, features = get_features(image_dir, FH, FW)
    objects = get_objects(annotation_file, image_names, features, FH, FW)
    print("Number of objects obtained : ", len(objects.keys()))

    objects_arr = []
    class_arr = []
    img_id_arr = []
    bbox_arr = []

    for obj in objects.values():
        obj_feature = obj["object_feature"]
        obj_feature = torch.mean(obj_feature, (1,2)).detach()
        objects_arr.append(obj_feature)
        class_arr.append(obj["category"])
        img_id_arr.append(obj["image_id"])
        bbox_arr.append(obj["bbox"])

    return objects_arr, class_arr, img_id_arr, bbox_arr


