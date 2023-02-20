import os
from pylabel import importer

path_to_annotations = './data/coco/annotations/instances_train2017.json'
image_dir = './data/coco/images'
path_to_images = '../images'
path_to_new_annotations = './datasets/t1_train/'
new_dataset_name = 't1_train_coco'

def create_annotation_file(path_to_annotations, image_dir, path_to_images, path_to_new_annotations, new_dataset_name):
    files = sorted(os.listdir(image_dir))
    print(f"{len(files)} files from {files[0]} to {files[len(files)-1]}")


    dataset = importer.ImportCoco(path_to_annotations, path_to_images = path_to_images, name = 'COCO')
    dataset.df = dataset.df[dataset.df.img_filename.isin(files)].reset_index()
    print("Dataframe creted for image subset")

    dataset.path_to_annotations = path_to_new_annotations
    dataset.name = new_dataset_name
    dataset.export.ExportToCoco()
    print(f"{dataset.name} dataframe exported")