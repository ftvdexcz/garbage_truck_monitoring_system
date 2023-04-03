import requests
import json
import cv2 
import base64
import threading
import os
import time

interval = 10 # đặt thời gian sau x giây lấy ra frame để xử lý 
url = "http://ptitsure.tk:9292/app/checkPlateVehicle"
flag = False

def processImage(frame, frame_count):
  try:
    image_base64 = base64.b64encode(cv2.imencode('.jpg', frame)[1]).decode('utf-8')
    payload = { "username": "ptit01", "password": "Ptit@321" }
    payload['image_base64'] = image_base64
    
    response = requests.post(url, data=json.dumps(payload))

    r = response.json()
    bbox = r['box']
    label = r['label']

    if bbox != [] and label != '':
        plate_img = frame[int(bbox[1]):int(bbox[3]), int(bbox[0]):int(bbox[2])]
        
        cv2.imwrite("plate_img_{}.jpg".format(frame_count), plate_img)
  except Exception as e:
    pass

def run():
  cap = cv2.VideoCapture('test.MOV')
  fps = cap.get(cv2.CAP_PROP_FPS)
  frame_interval = int(fps * interval) 
  frame_count = 0
  global flag
  flag = False

  while True:
    try:
      ret, frame = cap.read()
      # if not ret:
      #     print("Can't receive frame (stream end?). Exiting ...")
      #     break

      frame_count += 1
      cv2.imshow('frame', frame)
    
      if frame_count % (frame_interval) == 0:
        t = threading.Thread(target=processImage, args=(frame,frame_count,))
        t.start()
        
      if cv2.waitKey(25) == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break

    except cv2.error:
      flag = True
      print('Restarting...')
      cap.release()
      cv2.destroyAllWindows()
      time.sleep(10)
      break

while True:
  run()

  if flag == False: 
    break

# os.system("python detectPlate.py")  