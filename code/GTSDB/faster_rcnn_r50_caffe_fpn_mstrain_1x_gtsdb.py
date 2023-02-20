# The new config inherits a base config to highlight the necessary modification
_base_ = '../faster_rcnn/faster_rcnn_r50_caffe_fpn_mstrain_1x_coco.py'

# We also need to change the num_classes in head to match the dataset's annotation
model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=43)))

# Modify dataset related settings
dataset_type = 'COCODataset'

classes = ("speed limit 20", "speed limit 30", "speed limit 50", "speed limit 60", "speed limit 70", "speed limit 80", "restriction ends 80", "speed limit 100", "speed limit 120", "no overtaking", "no overtaking (trucks)", "priority at next intersection", "priority road", "give way", "stop", "no traffic both ways", "no trucks", "no entry", "danger","bend left","bend right","bend","uneven road", "slippery road","road narrows", "construction", "traffic signal", "pedestrian crossing", "school crossing", "cycles crossing", "snow", "animals", "restriction ends", "go right", "go left", "go straight", "go right or straight", "go left or straight", "keep right", "keep left", "roundabout", "restriction ends (overtaking)", "restriction ends (overtaking (trucks))")

data = dict(
    train=dict(
        img_prefix='/n/holyscratch01/wadduwage_lab/test_00001/GTSDB/Train/',
        classes=classes,
        ann_file='../other/GTSDB/data/annotations/train.json'),
    val=dict(
        img_prefix='/n/holyscratch01/wadduwage_lab/test_00001/GTSDB/Test/',
        classes=classes,
        ann_file='../other/GTSDB/data/annotations/test.json'),
    test=dict(
        img_prefix='/n/holyscratch01/wadduwage_lab/test_00001/GTSDB/Test/',
        classes=classes,
        ann_file='../other/GTSDB/data/annotations/test.json'))


