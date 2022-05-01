#from cv2 import *
import cv2
from clarifai.rest import ClarifaiApp
import serial
import os

#to load clarifai credentials from local machine
def load_clarifai_config():
	
	clarifai_client_id = '9c99aecdf7814a4a8d9d4505c2108793'
	clarifai_client_secret = '4cdc56503ae741fe901c17a96d4532e0'
	clarifai_model = '3a491e3640314f4b8bf81e6762ad28d71'
	return clarifai_client_id, clarifai_client_secret, clarifai_model

#takes a photo using your machine's camera and saves as a jpeg format
def photo(cam):
	
	s, img = get_image(cam)

	if s:    # frame captured without any errors
		cv2.namedWindow("cam-test")
		cv2.imshow("cam-test", img)
		cv2.waitKey(1)
		cv2.destroyWindow("cam-test")
		cv2.imwrite("test.jpg", img)

#helper function for above function
def get_image(camera):
	s, img = camera.read()
	return s, img

#calls Clarifai's API to predict labels of imagaes
def predict():
	
	CLIENT_ID, CLIENT_SECRET, clarifai_model = load_clarifai_config()
	app = ClarifaiApp(CLIENT_ID, CLIENT_SECRET)
	
	model = app.models.get(clarifai_model)

	prediction = model.predict_by_filename('test.jpg')

	outputs = prediction['outputs'][0]['data']['concepts']
	output = []
	for concept in outputs:
		if len(output) < 5:
			output.append({'name': concept['name'], 'value': concept['value']})
	return output	

def main():
	camera_port = 0
	ramp_frames = 30
	cam = cv2.VideoCapture(camera_port)
	
	for i in range(ramp_frames):
		s, temp = get_image(cam)

	ser = serial.Serial('COM3', 9600)

	#loop this indefinitely
	while True:
		arduino = True

		#loop here until arduino prints python
		while arduino:
			data = ser.readline()[:-2]
			if data == 'python':
				arduino = False
				print (arduino)

		photo(cam)
		prediction = predict()
	
		label = prediction[1]['name'].split(' ', 1)[0]
		print (label)

		if label == 'recyclable':
			ser.write('0')#left
		else:
			ser.write('1')#right


if __name__ == '__main__':
    main()