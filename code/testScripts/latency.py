import subprocess
import csv
import re

targetIp = '192.168.4.2'  # Replace with the IP address of the other device
pingCount = 10
csvFile = 'latencyResults.csv'

def testLatency():
    print(f"Pinging {targetIp} {pingCount} times...")
    pingCommand = ['ping', '-c', str(pingCount), targetIp]
    try:
        output = subprocess.check_output(pingCommand, universal_newlines=True)
    except subprocess.CalledProcessError as e:
        print("Ping failed. Make sure the target IP is correct and reachable.")
        return

    # Extract latency values using regular expressions
    latencyValues = re.findall(r'time=(\d+\.\d+)', output)
    latencies = [float(value) for value in latencyValues]

    if not latencies:
        print("No latency data was found.")
        return

    avgLatency = sum(latencies) / len(latencies)
    print(f"Average Latency: {avgLatency:.2f} ms")

    with open(csvFile, 'w', newline='') as csvFile:
        csvWriter = csv.writer(csvFile)
        csvWriter.writerow(['PingNumber', 'LatencyMs'])
        for i, latency in enumerate(latencies, 1):
            csvWriter.writerow([i, latency])
        csvWriter.writerow(['Average', avgLatency])
    print(f"Latency results saved to {csvFile}")

if __name__ == "__main__":
    testLatency()
