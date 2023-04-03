import cv2 
import base64
import requests
import json

path = r'vehicle-number-plates-to-be-auctioned.jpg'
  
# with open(path, "rb") as image_file:
#     image_base64 = base64.b64encode(image_file.read()).decode('utf-8')

img = cv2.imread(path)

image_base64 = base64.b64encode(cv2.imencode('.jpg', img)[1]).decode('utf-8')

url = "http://ptitsure.tk:9292/app/checkPlateVehicle"
payload = {"username": "ptit01", "password": "Ptit@321", "image_base64": image_base64}

response = requests.post(url, data=json.dumps(payload))

r = response.json()
print(r)

bbox = r['box']
label = r['label']

# Nếu có hình ảnh oto => có box và label 
if  bbox != [] and label != '':
  # crop image 
  print(type(bbox))
  
  plate_img = img[int(bbox[1]):int(bbox[3]), int(bbox[0]):int(bbox[2])]

  cv2.imshow('plate', plate_img)
  cv2.waitKey(0)
else: 
  print('Không có xe')