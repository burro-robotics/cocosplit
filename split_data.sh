#/bin/bash
if [ -z "$1" ]
then
    data_root=$HOME/catkin_ws/dataset/coco
else
    data_root=$1
fi
annotation_path=$(echo $data_root/*.json)
python3 cocosplit.py --having-annotations -s 0.75 --having-annotations $annotation_path $data_root/train.json $data_root/split.json
python3 cocosplit.py --having-annotations -s 0.6 --having-annotations $data_root/split.json $data_root/val.json $data_root/test.json
rm -rf $data_root/split.json
python3 cocosplit_images.py -val val.json -train train.json -test test.json -input_dir $data_root



