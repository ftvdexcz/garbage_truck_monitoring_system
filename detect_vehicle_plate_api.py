import cv2 
import base64
import requests
import json

path = r'C:\Users\NC.DESKTOP-8TG1B6T\Desktop\330071431_913456939673393_4231523450069196821_n.png'
  
# with open(path, "rb") as image_file:
#     image_base64 = base64.b64encode(image_file.read()).decode('utf-8')

img = cv2.imread(path)

image_base64 = base64.b64encode(cv2.imencode('.jpg', img)[1]).decode('utf-8')

url = "http://ptitsure.tk:9292/app/checkPlateVehicle"
payload = {"username": "ptit01", "password": "Ptit@321", "image_base64": image_base64}

response = requests.post(url, data=json.dumps(payload))

print(response.json())
print(response.status_code)

# crop image 
bbox = response.json()['box']

print(bbox)

plate_img = img[int(bbox[1]):int(bbox[3]), int(bbox[0]):int(bbox[2])]

cv2.imshow('plate', plate_img)
cv2.waitKey(0)