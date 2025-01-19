import socket
import os
import time

UDP_IP = "0.0.0.0"  # Listen on all interfaces
UDP_PORT = 5005
FILE_PATH = "testfile.bin"  # Replace with the file you want to send
PACKET_SIZE = 1024  # UDP packet size in bytes

def run_server():
    # Create a test file if it doesn't exist
    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, "wb") as f:
            f.write(os.urandom(1024 * 100))  # Create a 100 KB random binary file
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))

    print(f"UDP Server listening on {UDP_IP}:{UDP_PORT}")
    
    while True:
        # Wait for a client to request the file
        data, addr = sock.recvfrom(1024)
        if data.decode() == "START":
            print(f"Received START from {addr}. Sending file...")
            
            with open(FILE_PATH, "rb") as f:
                while chunk := f.read(PACKET_SIZE):
                    sock.sendto(chunk, addr)
                    time.sleep(0.001)  # Avoid overwhelming the client
            
            sock.sendto(b"END", addr)  # Send END signal
            print(f"File sent to {addr}")

if __name__ == "__main__":
    run_server()
