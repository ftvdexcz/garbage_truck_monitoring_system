from flask import Flask, Response
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <video controls>
          <source src="http://localhost:5000/video_feed" type="video/mp4">
          Your browser does not support the video tag.
        </video>
    '''

def gen():
    ffmpeg = subprocess.Popen(['ffmpeg', '-i', 'rtsp://admin:@192.168.1.82:554',
                               '-c:v', 'libx264', '-b:v', '1000k',
                               '-c:a', 'aac', '-b:a', '128k', '-'],
                              stdout=subprocess.PIPE)
    while True:
        data = ffmpeg.stdout.read(1024)
        if not data:
            break
        yield data

@app.route('/video_feed')
def video_feed():
    return Response(gen(),
                    mimetype='video/mp4')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)