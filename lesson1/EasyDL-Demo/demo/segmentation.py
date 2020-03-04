# coding:utf-8
"""
 Copyright (c) 2020 Baidu.com, Inc. All Rights Reserved
 Author: You Xiaohe, youxiaohe@baidu.com
"""

import requests
import json
import base64
import cv2 as cv
import pycocotools.mask as mask_util
import numpy as np

def data_form(image_path):
    """
    Convert data format.
    """
    with open(image_path, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        data = base64_data.decode()
    return data

def show_result(image_path, result):
    """
    Draw results on image.
    """
    image = cv.imread(image_path).astype(np.float32)
    height, width = image.shape[:2]
    for item in result:
        box = item['location']
        label = item['name']
        score = item['score']
        first_point = (box['left'], box['top'])
        last_point = (box['left'] + box['width'], box['top'] + box['height'])
        cv.rectangle(image, first_point, last_point, (0, 255, 0), 2)
        cv.putText(image, label + ':' + '%.4f' % score, first_point, cv.FONT_HERSHEY_SIMPLEX, 1.1,(255,0,0), 2, cv.LINE_AA)

        rle_obj = {"counts": item['mask'],
                   "size": [height, width]}
        mask = mask_util.decode(rle_obj)
        random_color = np.array([np.random.random()* 255.0,
                                 np.random.random()* 255.0,
                                 np.random.random()* 255.0])
        idx = np.nonzero(mask)
        image[idx[0], idx[1], :] *= 1.0 - 0.5
        image[idx[0], idx[1], :] += 0.5 * random_color
    image = image.astype(np.uint8)
    cv.imwrite('./output/segmentation_result.jpg', image)
    img = cv.resize(image, (600,600))


def segment(image_path, header, request_url):
    """
    Processing segmentation results.
    """
    data = data_form(image_path)
    request_payload = {
        "image": data,
        "threshold": "0.7"}
    response = requests.post(request_url,data=json.dumps(request_payload),headers=header).text
    tt = json.loads(response)
    print(tt)
    result = tt['results']
    show_result(image_path, result)

if __name__ == "__main__":
    image_path = './data/segmentation.png'
    header = {"Content-Type": "application/json"}
    access_token = '24.9dbf914011293b2542ed4dbc3435f1c5.2592000.1584521571.282335-18500615' #填入获取的access_token
    request_url = 'https://aip.baidubce.com/rpc/2.0/ai_custom/v1/segmentation/workpiece_seg_v1?access_token=' + access_token #填入API接口地址
    segment(image_path, header, request_url)