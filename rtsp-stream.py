from flask import Flask, render_template, Response
import cv2
import threading

app = Flask(__name__)

def get_camera_url(camera_id):
    cameras = {
        1: 'rtsp://long:1mrbean3@192.168.1.81:554',
        2: 'rtsp://long:1mrbean3@192.168.1.81:554',
        3: 'rtsp://long:1mrbean3@192.168.1.81:554',
        4: 'rtsp://iocldg:iocldg123123@14.241.197.248:1518/profile1/media.smp',
        5: 'rtsp://iocldg:iocldg123123@14.241.197.248:1518/profile1/media.smp',
        6: 'rtsp://iocldg:iocldg123123@14.241.197.248:1518/profile1/media.smp',
        7: 'rtsp://long:123456@192.168.1.18:8080/h264_pcm.sdp',
        8: 'rtsp://long:123456@192.168.1.18:8080/h264_pcm.sdp',
        9: 'rtsp://long:123456@192.168.1.18:8080/h264_pcm.sdp',
        
    }

    return cameras[camera_id]

@app.route('/')
def index():
    return render_template('index.html')

def get_frame(url):
    # Use cv2.VideoCapture to capture the video from the RTSP IP camera
    cap = cv2.VideoCapture(url)

    while True:
        try:
            # Capture the video frame by frame
            ret, frame = cap.read()

            # If the connection to the camera is not active, try to re-establish the connection
            if not cap.isOpened():
                cap.open(url)

            # Encode the frame to JPEG format
            ret, jpeg = cv2.imencode('.jpg', frame)

            # Return the frame as a response
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')
        except Exception as e:
            print(e)
            # Close the video capture object
            cap.release()
            # Try to re-establish the connection to the camera
            cap = cv2.VideoCapture(url)

@app.route('/video_feed/<int:camera_id>')
def video_feed(camera_id):
    # Get the RTSP URL of the camera based on the camera ID
    url = get_camera_url(camera_id)

    return Response(get_frame(url), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run()
    # thread = threading.Thread(target=app.run)
    # thread.start()



