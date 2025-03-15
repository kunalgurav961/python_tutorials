from picamera import PiCamera
from datetime import datetime

camera = PiCamera()
camera.capture(f'/home/pi/Pictures/image_{datetime.now().strftime("%Y%m%d_%H%M%S")}.jpg')
print("Image Captured!")
