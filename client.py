import subprocess
import sys
camera_index = 0

command = [
    "ffmpeg",
    "-f", "v4l2",
    "-framerate", "60",  
    "-video_size", "640x480",  
    "-i", f"/dev/video{camera_index}",
    "-f", "mpegts",
    "-codec:v", "mpeg1video",
    "-s", "640x480",  
    "-"
]

try:
    camera_process = subprocess.Popen(command, stdout=subprocess.PIPE)
except FileNotFoundError:
    sys.exit("ffmpeg is not installed or not in your PATH")

