1. For this app, you can use the existing image in the learningpal_api_test for testing.
2. To test the api, make sure you installed the python2.7 and dependency requests and json, you can use 
  pip install requests 
  pip install json 
 to install the package if you don't have them.
3. Run 
  python image_sender.py 
 then the image will be sent to api, results will come up after seconds.
4. If you want to change the image for testing, please replace the IMG_NAME in image_sender.py to the image that you put in the same directory.

## dependency
```
pip install requests 
pip install json 
```

## Example

![alt text](https://github.com/TomNong/learningpal_api/blob/master/commonmath.png?raw=true)

```
python image_sender.py 
```
###### Output:
```
u'{"confidence": 0.9945661408039893, "isResult": "true", "result": "( 3 - x ) ( x - 2 ) = 0 "}'
```

Replace handwritten images as you like

note: image resize to height of 50 pixs is recommended
