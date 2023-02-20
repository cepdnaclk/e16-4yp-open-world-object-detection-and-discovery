#!/bin/bash




wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget \

    --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate \

    'https://docs.google.com/uc?export=download&id=105J3fU3G_ujxNCFp9KX3u_PnbGcCkhXa' \

    -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=105J3fU3G_ujxNCFp9KX3u_PnbGcCkhXa" \

    -O train.zip && rm -rf /tmp/cookies.txt




wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget \

    --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate \

    'https://docs.google.com/uc?export=download&id=1MHqePR3ShjCh6GdpUKHbFpGyMztqAR6A' \

    -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1MHqePR3ShjCh6GdpUKHbFpGyMztqAR6A" \

    -O test.zip && rm -rf /tmp/cookies.txt




unzip train.zip -d ../

unzip test.zip -d ../




cd ..

mkdir Images

mkdir Annotations




mkdir Images/train

mkdir Images/test

mkdir Annotations/train

mkdir Annotations/test




mv train/*.jpg Images/train

mv train/*.xml Annotations/train




mv test/*.jpg Images/test

mv test/*.xml Annotations/test




python ~/projects/other/CeyRo/data/generate_ids.py




python ~/projects/other/CeyRo/data/voc2coco.py \

    --ann_dir Annotations/train \

    --ann_ids dataset_ids/train.txt \

    --labels ~/projects/other/CeyRo/data/labels.txt \

    --output Annotations/train.json \

    --ext xml




python ~/projects/other/CeyRo/data/voc2coco.py \

    --ann_dir Annotations/test \

    --ann_ids dataset_ids/test.txt \

    --labels ~/projects/other/CeyRo/data/labels.txt \

    --output Annotations/test.json \

    --ext xml



