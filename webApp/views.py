from django.http import HttpResponse
from django.shortcuts import render
from django.http.response import StreamingHttpResponse
import numpy as np
import cv2
from webApp.camera import VideoCamera

def index(request):
    return render(request, 'webApp/index.html')

def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def rendervideo(request):
    return StreamingHttpResponse(gen(VideoCamera()), content_type = 'multipart/x-mixed-replace; boundary=frame;')