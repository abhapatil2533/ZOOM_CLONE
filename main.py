import tkinter as tk
import socket
import threading
from vidstream import *

# Local IP Address nikalne ke liye
local_ip_address = socket.gethostbyname(socket.gethostname())

# Server aur Receiver instances
# Port numbers aap change kar sakte hain (e.g., 9999, 8888)
server = StreamingServer(local_ip_address, 9999)
receiver = AudioReceiver(local_ip_address, 8888)


def start_listening():
    # daemon=True add kiya hai
    t1 = threading.Thread(target=server.start_server, daemon=True)
    t2 = threading.Thread(target=receiver.start_server, daemon=True)
    t1.start()
    t2.start()

def start_camera_stream():
    target_ip = text_target_ip.get("1.0", "end-1c")
    camera_client = CameraClient(target_ip, 9999) # main2.py mein port alag hoga
    # daemon=True add kiya hai
    t3 = threading.Thread(target=camera_client.start_stream, daemon=True)
    t3.start()

def start_screen_sharing():
    target_ip = text_target_ip.get("1.0", "end-1c")
    screen_client = ScreenShareClient(target_ip, 9999)
    # daemon=True add kiya hai
    t4 = threading.Thread(target=screen_client.start_stream, daemon=True)
    t4.start()

def start_audio_stream():
    target_ip = text_target_ip.get("1.0", "end-1c")
    audio_sender = AudioSender(target_ip, 8888)
    # daemon=True add kiya hai
    t5 = threading.Thread(target=audio_sender.start_stream, daemon=True)
    t5.start()

# GUI Setup
window = tk.Tk()
window.title("NeuralNine Calls v0.1 Alpha")
window.geometry('300x200')

label_target_ip = tk.Label(window, text="Target IP Address:")
label_target_ip.pack()

text_target_ip = tk.Text(window, height=1)
text_target_ip.pack()

btn_listen = tk.Button(window, text="Start Listening", width=50, command=start_listening)
btn_listen.pack(anchor=tk.CENTER, expand=True)

btn_camera = tk.Button(window, text="Start Camera Stream", width=50, command=start_camera_stream)
btn_camera.pack(anchor=tk.CENTER, expand=True)

btn_screen = tk.Button(window, text="Start Screen Sharing", width=50, command=start_screen_sharing)
btn_screen.pack(anchor=tk.CENTER, expand=True)

btn_audio = tk.Button(window, text="Start Audio Stream", width=50, command=start_audio_stream)
btn_audio.pack(anchor=tk.CENTER, expand=True)

window.mainloop()