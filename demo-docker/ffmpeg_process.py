import subprocess
import signal
import os
import time

cmd = [
    'ffmpeg',
    '-rtsp_transport', 'tcp',
    '-i', 'rtsp://admin:@10.8.0.3:5504',
    '-f', 'flv',
    '-vcodec', 'libx264',
    '-an',
    '-b:v', '400K',
    '-deadline', 'realtime',
    '-crf', '23',
    'rtmp://203.162.10.118:8000/show/live'
]

# Start the ffmpeg process
proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Store the process ID in the session
# request.session['ffmpeg_pid'] = proc.pid

print('Start ffmpeg process')
print(proc.pid)

# time.sleep(20)

# # os.killpg(int(proc.pid), signal.SIGTERM)
# os.kill(proc.pid, signal.SIGKILL)