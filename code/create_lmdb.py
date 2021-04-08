'''
Title           :create_lmdb.py
Description     :This script divides the training images into 2 sets and stores them in lmdb databases for training and validation.
Author          :Adil Moujahid
Date Created    :20160619
Date Modified   :20160625
version         :0.2
usage           :python create_lmdb.py
python_version  :2.7.11
'''

import os
import glob
import random
import numpy as np

import caffe
from caffe.proto import caffe_pb2
import lmdb
import cv2

#Size of images
IMAGE_WIDTH = 227
IMAGE_HEIGHT = 227

def transform_img(img, img_width=IMAGE_WIDTH, img_height=IMAGE_HEIGHT):

    #Histogram Equalization
    img[:, :, 0] = cv2.equalizeHist(img[:, :, 0])
    img[:, :, 1] = cv2.equalizeHist(img[:, :, 1])
    img[:, :, 2] = cv2.equalizeHist(img[:, :, 2])

    #Image Resizing
    img = cv2.resize(img, (img_width, img_height), interpolation = cv2.INTER_CUBIC)

    return img

def make_datum(img, label):
    #image is numpy.ndarray format. BGR instead of RGB
    return caffe_pb2.Datum(
        channels=3,
        width=IMAGE_WIDTH,
        height=IMAGE_HEIGHT,
        label=label,
        data=np.rollaxis(img, 2).tostring())

train_lmdb = '/mnt/cats-dogs-tutorial/input/train_lmdb'
validation_lmdb = '/mnt/cats-dogs-tutorial/input/validation_lmdb'

os.system('del ' + train_lmdb)
os.system('del  ' + validation_lmdb)


train_data = [img for img in glob.glob("../input/train/*jpg")]
test_data = [img for img in glob.glob("../input/test1/*jpg")]

#Shuffle train_data
random.shuffle(train_data)

print ('Creating train_lmdb')

in_db = lmdb.open(train_lmdb, map_size=int(1e12))
with in_db.begin(write=True) as in_txn:
    for in_idx, img_path in enumerate(train_data):
        if in_idx %  6 == 0:
            continue
        img = cv2.imread(img_path, cv2.IMREAD_COLOR)
        img = transform_img(img, img_width=IMAGE_WIDTH, img_height=IMAGE_HEIGHT)
        if  "ain" in img_path:
            label = 0
        elif "al" in img_path:
            label = 1
        elif "aleff" in img_path:
            label = 2
        elif "bb" in img_path:
            label = 3
        elif "dal" in img_path:
            label = 4
        elif "dha" in img_path:
            label = 5
        elif "dhad" in img_path:
            label = 6
        elif "fa" in img_path:
            label = 7
        elif "gaaf" in img_path:
            label = 8
        elif "ghain" in img_path:
            label = 9
        elif "ha" in img_path:
            label = 10
        elif "haa" in img_path:
            label = 11
        elif "jeem" in img_path:
            label = 12
        elif "kaaf" in img_path:
            label = 13
        elif "khaa" in img_path:
            label = 14
        elif "la" in img_path:
            label = 15
        elif "laam" in img_path:
            label = 16
        elif "meem" in img_path:
            label = 17
        elif "nun" in img_path:
            label = 18
        elif "ra" in img_path:
            label = 19
        elif "saad" in img_path:
            label = 20
        elif "seen" in img_path:
            label = 21
        elif "sheen" in img_path:
            label = 22
        elif "ta" in img_path:
            label = 23
        elif "taa" in img_path:
            label = 24
        elif "test" in img_path:
            label = 25
        elif "thaa" in img_path:
            label = 26
        elif "thal" in img_path:
            label = 27
        elif "toot" in img_path:
            label = 28
        elif "waw" in img_path:
            label = 29
        elif "ya" in img_path:
            label = 30
        elif "yaa" in img_path:
            label = 31
        elif "zay" in img_path:
            label = 32

        datum = make_3datum(img, label)
        in_txn.put('{:0>5d}'.format(in_idx).encode(), datum.SerializeToString())
        print ('{:0>5d}'.format(in_idx) + ':' + img_path)
in_db.close()

print ('\nCreating validation_lmdb')

in_db = lmdb.open(validation_lmdb, map_size=int(1e12))
with in_db.begin(write=True) as in_txn:
    for in_idx, img_path in enumerate(train_data):
        if in_idx % 6 != 0:
            continue
        img = cv2.imread(img_path, cv2.IMREAD_COLOR)
        img = transform_img(img, img_width=IMAGE_WIDTH, img_height=IMAGE_HEIGHT)
        if  "ain" in img_path:
            label = 0
        elif "al" in img_path:
            label = 1
        elif "aleff" in img_path:
            label = 2
        elif "bb" in img_path:
            label = 3
        elif "dal" in img_path:
            label = 4
        elif "dha" in img_path:
            label = 5
        elif "dhad" in img_path:
            label = 6
        elif "fa" in img_path:
            label = 7
        elif "gaaf" in img_path:
            label = 8
        elif "ghain" in img_path:
            label = 9
        elif "ha" in img_path:
            label = 10
        elif "haa" in img_path:
            label = 11
        elif "jeem" in img_path:
            label = 12
        elif "kaaf" in img_path:
            label = 13
        elif "khaa" in img_path:
            label = 14
        elif "la" in img_path:
            label = 15
        elif "laam" in img_path:
            label = 16
        elif "meem" in img_path:
            label = 17
        elif "nun" in img_path:
            label = 18
        elif "ra" in img_path:
            label = 19
        elif "saad" in img_path:
            label = 20
        elif "seen" in img_path:
            label = 21
        elif "sheen" in img_path:
            label = 22
        elif "ta" in img_path:
            label = 23
        elif "taa" in img_path:
            label = 24
        elif "test" in img_path:
            label = 25
        elif "thaa" in img_path:
            label = 26
        elif "thal" in img_path:
            label = 27
        elif "toot" in img_path:
            label = 28
        elif "waw" in img_path:
            label = 29
        elif "ya" in img_path:
            label = 30
        elif "yaa" in img_path:
            label = 31
        elif "zay" in img_path:
            label = 32
        datum = make_datum(img, label)
        in_txn.put('{:0>5d}'.format(in_idx).encode(), datum.SerializeToString())
        print ('{:0>5d}'.format(in_idx) + ':' + img_path)
in_db.close()

print ('\nFinished processing all images')
