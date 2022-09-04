from importlib.metadata import files
import socket
import tqdm
import os 

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096 # send 4096 bytes each time step

host = "127.0.0.1"
port = 5001
filename = "output.wav"
filesize = os.path.getsize(filename)

s = socket.socket()

print(f"[+] Connecting to {host}:{port}")
s.connect((host, port))
print("[+] Connected.")
s.send(f"{filename}{SEPARATOR}{filesize}".encode())

progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
with open(filename, "rb") as f:
    while True:
        bytes = f.read(BUFFER_SIZE)
        if not bytes:
            break
        s.sendall(bytes)
        progress.update(len(bytes))

s.close()