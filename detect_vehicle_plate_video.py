import requests
import json
import cv2 
import base64
import threading

cap = cv2.VideoCapture('detect_vehicle_plate.MOV')
fps = cap.get(cv2.CAP_PROP_FPS)

print(fps)

frame_interval = int(fps * 10)

frame_count = 0

url = "http://ptitsure.tk:9292/app/checkPlateVehicle"
payload = { "username": "ptit01", "password": "Ptit@321" }

while cap.isOpened():
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    frame_count += 1
    cv2.imshow('frame', frame)
    # waitKey nhỏ tốc độ video nhanh 
    if frame_count % (frame_interval) == 0:
        image_base64 = base64.b64encode(cv2.imencode('.jpg', frame)[1]).decode('utf-8')

        # set image_base64 string 
        payload['image_base64'] = image_base64
        
        response = requests.post(url, data=json.dumps(payload))

        bbox = response.json()['box']

        print(bbox)
        if response.status_code == 200:
            plate_img = frame[int(bbox[1]):int(bbox[3]), int(bbox[0]):int(bbox[2])]
            
            cv2.imwrite("plate_img_{}.jpg".format(frame_count), plate_img)

    if cv2.waitKey(25) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
