import requests
import json
from time import sleep
import multiprocessing

IMG_NAMES = ["homework2.jpg"]


def worker(IMG_NAME):
    
    try:
        url = 'http://api.learningpal.com/run_img'
        files = {'file': open('./' + IMG_NAME, 'rb')}
        headers = {'content-type': 'application/json'}
        r = requests.post(url, files=files)
        print r.text
        response = json.loads(r.text)
        return response
    except Exception as e :
        print e

if __name__ == '__main__':
    boxes = worker(IMG_NAMES[0])
    print boxes
