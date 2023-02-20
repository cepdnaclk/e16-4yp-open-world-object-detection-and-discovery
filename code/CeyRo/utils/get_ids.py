import os
path = "~/CeyRo/images" 
train_imgs =os.listdir(path) + "/train"
test_imgs  =os.listdir(path) + "/test"

with open ("dataset_ids/train.txt", "w") as f:
    for img_name in train_imgs:
        img_id = img_name.split('.')[0]
        f.write("%s\n" % img_id)
    print('Train IDs written to train.txt')

with open ("dataset_ids/test.txt", "w") as f:
    for img_name in test_imgs:
        img_id = img_name.split('.')[0]
        f.write("%s\n" % img_id)
    print('Test IDs written to test.txt')