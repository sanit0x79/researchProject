import pandas as pd
import matplotlib.pyplot as plt

esp32_data = pd.read_csv('esp32/latency1.csv')
esp8266_data = pd.read_csv('esp8266/latency1.csv')

# Plot the data
plt.figure(figsize=(10, 6))

plt.plot(esp32_data['PingNumber'], esp32_data['LatencyMs'], label='ESP32', marker='o')
plt.plot(esp8266_data['PingNumber'], esp8266_data['LatencyMs'], label='ESP8266', marker='s')

# Add labels and title
plt.title('Latency Comparison: ESP32 vs ESP8266', fontsize=14)
plt.xlabel('Ping Number', fontsize=12)
plt.ylabel('Latency (ms)', fontsize=12)
plt.legend()
plt.grid()

# Show the plot
plt.show()
