from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import numpy as np
import cv2
import os
import cvlib as cv
import pyautogui
import pycurl
from io import StringIO
import json
import urllib.parse
from pushbullet import PushBullet

token = 'o.lCR99YIOa6GW6PaMEwU9ZjRQuwUDlBrb'
p= PushBullet(token)
devices = p.getDevices()
contacts = p.getContacts()

                    
# load model
model = load_model('gender_detection.model')

# open webcam
webcam = cv2.VideoCapture(0)
    
classes = ['laki-laki','perempuan']

inc = 0
label = "Init"
now = "unknown"

# loop through frames
while webcam.isOpened():

    # read frame from webcam 
    status, frame = webcam.read()

    # apply face detection
    face, confidence = cv.detect_face(frame)


    # loop through detected faces
    for idx, f in enumerate(face):

        # get corner points of face rectangle        
        (startX, startY) = f[0], f[1]
        (endX, endY) = f[2], f[3]

        # draw rectangle over face
        cv2.rectangle(frame, (startX,startY), (endX,endY), (0,255,0), 2)

        # crop the detected face region
        face_crop = np.copy(frame[startY:endY,startX:endX])

        if (face_crop.shape[0]) < 10 or (face_crop.shape[1]) < 10:
            continue

        # preprocessing for gender detection model
        face_crop = cv2.resize(face_crop, (96,96))
        face_crop = face_crop.astype("float") / 255.0
        face_crop = img_to_array(face_crop)
        face_crop = np.expand_dims(face_crop, axis=0)

        # apply gender detection on face
        conf = model.predict(face_crop)[0] # model.predict return a 2D matrix, ex: [[9.9993384e-01 7.4850512e-05]]

        # get label with max accuracy
        idx = np.argmax(conf)
        label = classes[idx]
        
        if now == label:
            inc += 1
        else:
            inc = 0
            now = label

        # pyautogui.click(720, 805, 1, 1, button='left')

        print(inc)

        if (inc == 3) and (label=="perempuan"):
            # p.pushNote(devices[0]["iden"], 'Test', 'Coba')
            cv2.imwrite('C:/Users/ROG/Desktop/FP_SDI/Gender-Detection/Capture.JPG', frame)
            p.pushFile(devices[0]["iden"], "Capture.JPG", "INI PENYUSUP TOILETNYA", open("C:/Users/ROG/Desktop/FP_SDI/Gender-Detection/Capture.JPG", "rb"))


        label = "{}: {:.2f}%".format(label, conf[idx] * 100)

        Y = startY - 10 if startY - 10 > 10 else startY + 10

        # write label and confidence above face rectangle
        cv2.putText(frame, label, (startX, Y),  cv2.FONT_HERSHEY_SIMPLEX,
                    0.7, (0, 255, 0), 2)

    if label == "Kosong":
        inc = 0

    label = "Kosong"

    # display output
    cv2.imshow("gender detection", frame)

    # press "Q" to stop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release resources

webcam.release()
cv2.destroyAllWindows()