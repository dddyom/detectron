from Detector import *

detector = Detector(model_type="OD")
for i in range(1, 6):
    detector.onImage(f"images/{i}.jpg")
# detector.onImage("images/4.jpg")
