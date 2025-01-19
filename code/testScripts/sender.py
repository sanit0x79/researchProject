import socket
import time
import csv

SERVER_IP = "192.168.4.3"  # Replace with the server's IP address
UDP_PORT = 5005
PACKET_SIZE = 1024
REPEAT_COUNT = 10
CSV_FILE = "download_speed_results.csv"

def run_client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(10)

    total_speeds = []

    # Open the CSV file for writing
    with open(CSV_FILE, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["TestNumber", "DownloadSpeedMbps"])  # Header row

        for i in range(REPEAT_COUNT):
            print(f"Starting file download {i+1}/{REPEAT_COUNT}...")
            sock.sendto(b"START", (SERVER_IP, UDP_PORT))  # Request file

            start_time = time.time()
            total_bytes = 0

            while True:
                try:
                    data, addr = sock.recvfrom(PACKET_SIZE)
                    if data == b"END":
                        break
                    total_bytes += len(data)
                except socket.timeout:
                    print("Timeout occurred!")
                    break

            end_time = time.time()
            elapsed_time = end_time - start_time

            if elapsed_time > 0:
                speed_mbps = (total_bytes * 8) / (elapsed_time * 1_000_000)
                total_speeds.append(speed_mbps)
                print(f"Download {i+1}: {speed_mbps:.2f} Mbps")

                # Save this iteration's result to the CSV
                csv_writer.writerow([i + 1, speed_mbps])

    # Calculate average speed
    if total_speeds:
        avg_speed = sum(total_speeds) / len(total_speeds)
        print(f"\nAverage Download Speed: {avg_speed:.2f} Mbps")

        # Save the average to the CSV
        with open(CSV_FILE, "a", newline="") as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow([])
            csv_writer.writerow(["Average", avg_speed])
    else:
        print("No valid downloads recorded.")

if __name__ == "__main__":
    run_client()

