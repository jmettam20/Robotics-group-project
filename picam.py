import picamera
import time

camera=picamera.PiCamera()
camera.hflip=True
camera.vflip=True
camera.capture('meme.jpg')