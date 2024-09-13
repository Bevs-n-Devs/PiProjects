from flask import render_template, jsonify, url_for, Response, stream_with_context
from FlaskLiveCam_WebApp import app, scripts
from scripts.video_feed import CamFeed
import time

picam = None

@app.route("/")
def render_homepage():
	"""
	Starts homepage for the webapp.
	"""

	return render_template("index.html")

@app.route('/vid_feed')
def streamVideo():
	"""
	Handles constant refreshing of picam feed.  
	"""
	global picam
	if picam == None:
		picam = CamFeed()
	else:
		#del picam
		time.sleep(0.1)
		#picam = CamFeed()
		time.sleep(0.1)
	return Response(gen(picam), mimetype='multipart/x-mixed-replace; boundary=frame')

def gen(cam):
	"""
	Triggers the Pi Camera to begin generating the live video feed
	"""
	while (True):
		frame = cam.get_frame()
		yield(b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')