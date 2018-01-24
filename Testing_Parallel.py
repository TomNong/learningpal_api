import requests, json, time, multiprocessing, sys, signal

def recognize(IMG_NAME):
#    url = 'http://api.learningpal.com/math/upload'
    url = 'http://34.229.216.102/math/upload'
    files = {'file': open('./' + IMG_NAME, 'rb')}
    headers = {'content-type': 'application/json'}
    try:
        r = requests.post(url, files=files)
        print r.text
        response = json.loads(r.text)
        task_ID = response['task_ID']
        payload = {'task_ID' : task_ID, 'password' : ""}
#        url2 = 'http://api.learningpal.com/math/result'
        url2 = 'http://34.229.216.102/math/result'
        while True:
            response = requests.post(url2, data=json.dumps(payload), headers=headers)
            print response.text
            if response.text and "processing" not in response.text:
                return response.text
                break
    except Exception as e :
        print e
        return None

def main(arg):
    print 'Job started...'
    tasks = ['single_equation.png','single_equation.png','single_equation.png','single_equation.png','single_equation.png',
             'single_equation.png','single_equation.png','single_equation.png','single_equation.png','single_equation.png',
             'single_equation.png','single_equation.png','single_equation.png','single_equation.png','single_equation.png',
            'single_equation.png','single_equation.png','single_equation.png','single_equation.png','single_equation.png',
            'single_equation.png','single_equation.png','single_equation.png','single_equation.png','single_equation.png',
            'single_equation.png','single_equation.png','single_equation.png','single_equation.png','single_equation.png',
            'single_equation.png','single_equation.png','single_equation.png','single_equation.png','single_equation.png',
            'single_equation.png','single_equation.png','single_equation.png','single_equation.png','single_equation.png',
            'single_equation.png','single_equation.png','single_equation.png','single_equation.png','single_equation.png',
            'single_equation.png','single_equation.png','single_equation.png','single_equation.png','single_equation.png',
            'single_equation.png','single_equation.png','single_equation.png','single_equation.png','single_equation.png',
            'single_equation.png','single_equation.png','single_equation.png','single_equation.png','single_equation.png',
            'single_equation.png','single_equation.png','single_equation.png','single_equation.png','single_equation.png',
            'single_equation.png','single_equation.png','single_equation.png','single_equation.png','single_equation.png',
            'single_equation.png','single_equation.png','single_equation.png','single_equation.png','single_equation.png',
            'single_equation.png','single_equation.png','single_equation.png','single_equation.png','single_equation.png']
    tic = time.time()
    #result = worker(arg)
    #print result
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    tasks = tasks[:(int(arg))]
    print '    number of sending images: ', len(tasks)
    results = pool.map(recognize, tasks)
    pool.close()
    pool.join()
    print results
    print '    Done! Time cost: ', str(time.time() - tic), 's'
        
def quit(signum, frame):
    print 'Stop'
    sys.exit()
if __name__=="__main__":
    signal.signal(signal.SIGINT, quit)
    signal.signal(signal.SIGTERM, quit)
    main(sys.argv[1])
