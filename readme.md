This repository includes:
  1. Handwritten math equation recognition API
  2. Math equation detection in a single image API
  3. Using above two API to achieve problem sheet auto grading

## For Usage of Handwritten math equation recognition API
You can use provided image to test.
If you want to change the image for testing, please replace the IMG_NAME in image_sender.py to the image that you put in the same directory.

### Dependency
```
pip install requests 
pip install json 
```

### Example

![alt text](https://github.com/TomNong/learningpal_api/blob/master/single_equation.png?raw=true)

```
python image_sender.py 
```
###### Output:
```
u'{"confidence": 0.9945661408039893, "isResult": "true", "result": "( 3 - x ) ( x - 2 ) = 0 "}'
```

Replace handwritten images as you like

note: image resize to height of 50 pixs is recommended

## For Usage of Math equation detection in a single image API
### Example
```
python run_imgApi.py
```
###### Output 
returns a list of [(x1,y1),(x2,y2)] box location coordinates

## For Problem Sheet Auto Grading
### Example
Testing on problem sheet image
![alt text](https://github.com/TomNong/learningpal_api/blob/master/homework.png?raw=true)
```
python recognize_hw.py homework.png
```
###### Output
The program draws boxes on detected math equtions on image, and put recognized text on the image, and output as result.png

![alt text](https://github.com/TomNong/learningpal_api/blob/master/result.png?raw=true)

