#!/usr/bin/env python

import cv2, json, sys, requests, traceback, os, time
import numpy as np
from PIL import Image
from time import sleep
from multiprocessing import Pool, Process, current_process, Manager

def recognize(img_name):
    IMG_NAME = img_name

    url = 'http://api.learningpal.com/math/upload'
    #url = 'http://no3.xwism.com:10500/upload'
    files = {'file': open('./' + IMG_NAME, 'rb')}
    headers = {'content-type': 'application/json', 'Connection':'close'}

    try:
        r = requests.post(url, files=files)
        #print r.text
        response = json.loads(r.text)
        task_ID = response['task_ID']
        payload = {'task_ID' : task_ID, 'password' : ""}
        url2  = 'http://api.learningpal.com/math/result'
        while True:
            response = requests.post(url2, data=json.dumps(payload), headers=headers)
            #print response.text
            if response.text and "processing" not in response.text:
                print "  got result!", response.text
                break
                sleep(1)
        return response.text
    except Exception as e :
        print "except: ", e, IMG_NAME

def run_img(IMG_NAME):
    try:
        url = 'http://api.learningpal.com/run_img'
        files = {'file': open('./' + IMG_NAME, 'rb')}
        headers = {'content-type': 'application/json', 'Connection':'close'}
        r = requests.post(url, files=files)
        #print r.text
        response = json.loads(r.text)
        return response
    except Exception as e :
        print "except: ", e, IMG_NAME

def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]
    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))
    resized = cv2.resize(image, dim, interpolation = inter)
    return resized
        
def rec(imagename, return_dict):
    res = recognize(imagename[1])
    #res = recognize(imagename)
    print "      res:", res
    res_json = json.loads(res)
    result = res_json['result']
    print "      result:", result
    return_dict[res] = imagename[1], result, imagename[0]
    #return_dict[res] = imagename, result
    
def main(arg):
    imagename = arg
    # convert format jpeg to jpg
    lower4 = os.path.splitext(imagename)[1]
    if lower4 == ".jpeg":
        imagename = os.path.splitext(imagename)[0] + ".jpg"
        try:
            Image.open(arg).save(imagename)
            os.remove(arg)
        except IOError:
            print "error occur"
    
    start = time.time()
    img = cv2.imread(imagename)
    imgcp = img.copy()
    boxes = run_img(imagename)
    boxes = boxes['result']
    n = 0
    images = []
    filenames = []
    results = []
    for box in boxes:
        roi = img[box[0][1]: box[1][1], box[0][0]:box[1][0]]
        imagename = "small_images/" + str(n) + "hw.png"
        if roi.shape[0] > 50:
            roi = image_resize(roi, height = 50)
        cv2.imwrite(imagename, roi)
        filenames.append(imagename)
        images.append((box,imagename))
        #cv2.rectangle(imgcp, box[0],box[1], (0, 0, 255), 1)
        n += 1
    print images
    
    procs = []
    manager = Manager()
    return_dict = manager.dict()
    for index, imagename in enumerate(images):
    #for index, imagename in enumerate(filenames):
        proc = Process(target=rec, args=(imagename, return_dict))
        procs.append(proc)
        proc.start()
    for proc in procs:
        proc.join()
        
    all_res = return_dict.values()
        
    print all_res
    print "Found all results, now draw on the image."
    
    math_op_sign = ['=', '<', '>']
    
    
        
    
    for element in all_res:
        label = element[1]
        box = element[2]
        cv2.rectangle(imgcp, (box[0][0],box[0][1]),(box[1][0], box[1][1]), (0, 0, 255), 1)
        if any(x in label for x in math_op_sign):
            cv2.putText(imgcp, label, (box[0][0]+5,box[1][1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imwrite("result.png", imgcp)
    
    print "total time cost: ", str(time.time()-start)
    
if __name__ == "__main__":
    main(sys.argv[1:][0])
    
    
    
    
    
    
    
    