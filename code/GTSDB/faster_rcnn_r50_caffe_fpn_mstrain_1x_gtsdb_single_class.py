# The new config inherits a base config to highlight the necessary modification
_base_ = '../faster_rcnn/faster_rcnn_r50_caffe_fpn_mstrain_1x_coco.py'

# We also need to change the num_classes in head to match the dataset's annotation
model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=1)))

# Modify dataset related settings
dataset_type = 'COCODataset'

classes = ("traffic sign",)

data = dict(
    train=dict(
        img_prefix='/n/holyscratch01/wadduwage_lab/test_00001/GTSDB/Train/',
        classes=classes,
        ann_file='../other/GTSDB/data/annotations/train1.json'),
    val=dict(
        img_prefix='/n/holyscratch01/wadduwage_lab/test_00001/GTSDB/Test/',
        classes=classes,
        ann_file='../other/GTSDB/data/annotations/test1.json'),
    test=dict(
        img_prefix='/n/holyscratch01/wadduwage_lab/test_00001/GTSDB/Test/',
        classes=classes,
        ann_file='../other/GTSDB/data/annotations/test1.json'))


