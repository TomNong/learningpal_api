#!/usr/bin/env python

import cv2, json, sys, requests, traceback
import numpy as np
from time import sleep

def threshold(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.medianBlur(img,1)
    th3 = cv2.adaptiveThreshold(img, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                                cv2.THRESH_BINARY,25,12)
    return th3


def recognize(img_name):
    IMG_NAME = img_name

    url = 'http://api.learningpal.com/math/upload'
    #url = 'http://no3.xwism.com:10500/upload'
    files = {'file': open('./' + IMG_NAME, 'rb')}
    headers = {'content-type': 'application/json'}

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
        
def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation = inter)

    # return the resized image
    return resized
    
def run_img(argv):
    #Create MSER object
    mser = cv2.MSER_create()
    #Your image path i-e receipt path
    img = cv2.imread(argv)

    height, width, _ = img.shape

    height_rate = height/3264.0 # respect size: 3024 x 4032
    
    #imgcp = img.copy() #make copy

    img=cv2.medianBlur(img,5) #blur to reduce noise

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #detect regions in gray scale image
    regions, _ = mser.detectRegions(gray)
    hulls = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in regions]

    mask = np.zeros((img.shape[0], img.shape[1], 1), dtype=np.uint8)
    for contour in hulls: 
        #hull_area = cv2.contourArea(contour)
        [x, y, w, h] = cv2.boundingRect(contour)
        #if not w > 1200 * height_rate:
        if w < 700 * height_rate and h < 700 * height_rate:
            #cv2.rectangle(mask, (x - w - 20, y + h/4), (x + 2*w + 20, y + 3*h/4), (255, 255, 255), -1) # put some white area
            cv2.rectangle(mask, (x - w/2 - int(20.0*height_rate), y + h/4 ), (x + 3*w/2 + int(20.0*height_rate), y + 3*h/4), (255, 255, 255), -1)
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (20,1))
    kernel2 = cv2.getStructuringElement(cv2.MORPH_CROSS, (1,6))
    dilated = cv2.erode(mask, kernel2, iterations=1)
    dilated = cv2.dilate(dilated, kernel, iterations=1)
    #dilated = cv2.dilate(mask, kernel, iterations=1)

    _, contours, hierarchy = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    n = 0
    boxes = []
    for contour in contours:
        # get rectangle bounding contour
        [x, y, w, h] = cv2.boundingRect(contour)

        # Don't plot small false positives that aren't text
        if w < 50 and h < 50:
            continue

        #if w > 1000 and h > 700:
        if w > 2000 * height_rate:
            continue
            
        #roi = imgcp[y-int(20.0*height_rate):y + h + int(20.0*height_rate), x:x+w]
        #cv2.imwrite("img3/"+str(n)+".jpg", roi)
        n += 1
        # draw rectangle around contour on original image
        #cv2.rectangle(imgcp, (x, y-int(20.0*height_rate)), (x + w, y + h + int(20.0*height_rate)), (0, 0, 255), 1)
        boxes.append([(x,y-int(20.0*height_rate) - h/2), (x + w, y + h + int(20.0*height_rate) + h/2)])
        
    print "total boxes: ", n
    return boxes
    

if __name__ == "__main__":
    run_img(sys.argv[1:][0])
