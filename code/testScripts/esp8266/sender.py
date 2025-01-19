import socket
import time
import csv

receiverIp = '192.168.4.3'  # Replace with your receiver's IP address
udpPort = 5005
packetSize = 1024  # Size of each packet in bytes
testDuration = 10  # Duration of the test in seconds
csvFileName = "throughputResults.csv"

def runSender():
    print("Starting UDP Sender...")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Send START signal
    sock.sendto(b'START', (receiverIp, udpPort))
    print("Sent START signal.")

    totalBytes = 0
    endTime = time.time() + testDuration

    while time.time() < endTime:
        data = b'a' * packetSize
        sock.sendto(data, (receiverIp, udpPort))
        totalBytes += len(data)

    # Send END signal
    sock.sendto(b'END', (receiverIp, udpPort))
    print("Sent END signal.")

    elapsedTime = testDuration
    throughputMbps = (totalBytes * 8) / (elapsedTime * 1_000_000)

    print(f"Total Bytes Sent: {totalBytes} bytes")
    print(f"Elapsed Time: {elapsedTime:.2f} seconds")
    print(f"Throughput: {throughputMbps:.2f} Mbps")

    # Save results to CSV
    with open(csvFileName, 'w', newline='') as csvFile:
        csvWriter = csv.writer(csvFile)
        csvWriter.writerow(['TotalBytesSent', 'ElapsedTimeSeconds', 'ThroughputMbps'])
        csvWriter.writerow([totalBytes, elapsedTime, throughputMbps])
    
    print(f"Results saved to {csvFileName}")

if __name__ == "__main__":
    runSender()

