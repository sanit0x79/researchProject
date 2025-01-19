import socket
import time
import csv

udpIp = ''  # Bind to all interfaces
udpPort = 5005  # Port to listen on
bufferSize = 65507  # Maximum UDP packet size

def runReceiver():
    print("Starting UDP Receiver...")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((udpIp, udpPort))
    print(f"Listening on port {udpPort}")

    totalBytes = 0
    startTime = None
    endTime = None

    with open('throughputResults.csv', 'w', newline='') as csvFile:
        csvWriter = csv.writer(csvFile)
        csvWriter.writerow(['Timestamp', 'BytesReceived'])

        while True:
            data, addr = sock.recvfrom(bufferSize)
            if data:
                if data == b'START':
                    print("Received START signal.")
                    startTime = time.time()
                    totalBytes = 0
                    continue
                elif data == b'END':
                    print("Received END signal.")
                    endTime = time.time()
                    break
                else:
                    totalBytes += len(data)
                    csvWriter.writerow([time.time(), len(data)])

    elapsedTime = endTime - startTime if endTime and startTime else 0
    throughputMbps = (totalBytes * 8) / (elapsedTime * 1_000_000) if elapsedTime > 0 else 0

    print(f"Total Bytes Received: {totalBytes} bytes")
    print(f"Elapsed Time: {elapsedTime:.2f} seconds")
    print(f"Throughput: {throughputMbps:.2f} Mbps")

if __name__ == "__main__":
    runReceiver()
