# coding:utf-8
"""
 Copyright (c) 2020 Baidu.com, Inc. All Rights Reserved
 Author: You Xiaohe, youxiaohe@baidu.com
"""

import requests
import json
import base64
import cv2 as cv

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
    image = cv.imread(image_path)
    for target in result:
        box = target['location']
        label = target['name']
        score = target['score']
        first_point = (box['left'], box['top'])
        last_point = (box['left'] + box['width'], box['top'] + box['height'])
        cv.rectangle(image, first_point, last_point, (0, 255, 0), 2)
        cv.putText(image, label + ':' + '%.4f' % score, first_point, cv.FONT_HERSHEY_SIMPLEX, 0.5,(255,0,0), 1, cv.LINE_AA)
    cv.imwrite('./output/detection_result.jpg', image)
    img = cv.resize(image, (600,600))
  

def detection(image_path, header, request_url):
    """
    Processing detection results.
    """
    data = data_form(image_path)
    request_payload = {
        "image": data,
        "threshold": "0.7"}
    response = requests.post(request_url,data=json.dumps(request_payload),headers=header).text
    tt = json.loads(response)
    result = tt['results']
    show_result(image_path, result)
    print(result)

if __name__ == "__main__":
    image_path = './data/detection.jpg'
    header = {"Content-Type": "application/json"}
    access_token = '24.1f5e1f2a847fcde0aa526f743db8ddd4.2592000.1584518941.282335-18497426' #填入获取的access_token
    request_url = 'https://aip.baidubce.com/rpc/2.0/ai_custom/v1/detection/garbage_det?access_token=' + access_token #填入API接口地址
    detection(image_path, header, request_url)