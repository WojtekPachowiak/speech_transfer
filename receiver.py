from fileinput import filename
import socket
import tqdm
import os

# device's IP address
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5001
# receive 4096 bytes each time
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"

s = socket.socket()
s.bind((SERVER_HOST,SERVER_PORT))

#listen
s.listen(5)
print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

#accept
client_socket, address = s.accept()
print(f"[+] {address} is connected.")

#receive the name and size of the transfered file
received = client_socket.recv(BUFFER_SIZE).decode()
filename, filesize = received.split(SEPARATOR) 
filename = os.path.basename(filename)
filesize = int(filesize)

#progress bar
progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)

with open("received_file", "wb") as f:
    while True:
        bytes = client_socket.recv(BUFFER_SIZE)
        #break if no more data to receive
        if not bytes:
            break
        f.write(bytes)
        progress.update(len(bytes))

#we're done with client. Bye, client...
client_socket.close()

#...I'm leaving
s.close()