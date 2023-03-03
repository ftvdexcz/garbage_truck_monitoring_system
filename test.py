import subprocess
import os 
import time 
import signal

cmd = [
    'ffmpeg',
    '-rtsp_transport', 'tcp',
    '-i', 'rtsp://admin:@192.168.1.81:554',
    '-f', 'flv',
    '-vcodec', 'libx264',
    '-an',
    '-b:v', '400K',
    '-deadline', 'realtime',
    '-crf', '23',
    'rtmp://203.162.10.118:8000/show/live'
]

proc = subprocess.Popen(cmd, creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)

time.sleep(20)

os.killpg(int(proc.pid), signal.SIGTERM)
