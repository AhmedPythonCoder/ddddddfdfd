import subprocess
import http.server
import socketserver
import sys
def hack_camera(cameraNumber):
    camera_index = cameraNumber
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

    # Choose a port for the HTTP server
    port = 8000

    Handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", port), Handler) as httpd:
        print(f"Serving at http://localhost:{port}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("Server stopped.")
            camera_process.kill()
            sys.exit(0)
hack_camera(cameraNumber=0)