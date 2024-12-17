# ESP8266 Wi-Fi Mode Latency Research Project  

## 📄 Project Overview  

This repository contains the code and documentation for a research project analyzing the **latency and performance trade-offs** of the **ESP8266** microcontroller across different Wi-Fi PHY modes:  
- **802.11b**  
- **802.11g**  
- **802.11n**  

The project aims to measure and compare **round-trip times (RTT)** and **latency** for these Wi-Fi modes under varying conditions to determine their suitability for specific IoT and embedded systems applications.

---

## 🛠️ Hardware Requirements  

To replicate the project, you need:  

1. **ESP8266 NodeMCU** development board  
2. **Push-button switch** (to change modes dynamically)  
3. **Adafruit SSD1306 OLED display** (128x64 resolution, I2C)  
4. **Breadboard and jumper wires**  
5. **A computer with Arduino IDE installed**  

---

## 🔧 Software Setup  

### Libraries Required  
Install the following libraries using the Arduino Library Manager:  
1. **Adafruit SSD1306** (for OLED display)  
2. **Adafruit GFX** (graphics library)  
3. **ESP8266WiFi** (built-in with ESP8266 board support)  

### Board Setup  
1. Install the **ESP8266 Board Package** in the Arduino IDE:  
   - Go to `File -> Preferences`  
   - Add the URL: `http://arduino.esp8266.com/stable/package_esp8266com_index.json`  
   - Install the package via `Tools -> Board Manager`.  
2. Select **NodeMCU 1.0 (ESP-12E Module)** as the target board.

---

## 📊 Code Functionality  

### Main Features:  
- **Access Point Mode**: The ESP8266 acts as a Wi-Fi AP with a configurable SSID and password.  
- **Mode Switching**:  
   - A **push-button** connected to GPIO0 cycles through Wi-Fi PHY modes (**802.11b**, **802.11g**, **802.11n**).  
   - The current mode is displayed on the OLED screen in real-time.  
- **OLED Display**: Displays the SSID, Access Point IP, and current Wi-Fi mode.  
- **Latency and RTT Measurement**: The ESP8266's PHY mode is tested to measure latency and round-trip times using **ping tests**.  

---

## 💻 Code Structure  

- **`main.ino`**: The primary sketch implementing mode switching, OLED display updates, and AP configuration.  
- **`hardware_setup.md`**: Instructions for wiring the ESP8266, OLED, and push-button.  
- **`results/`**: Folder containing recorded RTT and latency measurements.  

---

## 🧪 How to Run the Project  

1. **Upload the Code**  
   - Connect the ESP8266 to your computer.  
   - Upload the sketch using Arduino IDE.  

2. **Connect to the AP**  
   - On your Wi-Fi-enabled device, connect to the SSID defined in the code (default: `pixel1234`).  

3. **Switch Wi-Fi Modes**  
   - Press the button to cycle through Wi-Fi modes (**802.11b**, **802.11g**, **802.11n**).  
   - The current mode will update on the OLED display.  

4. **Test Latency**  
   - Use a computer or tool to **ping** the ESP8266's Access Point IP address (default: `192.168.4.1`).  
   - Record RTT and calculate latency using the formula:  
     \[
     \text{Latency (ms)} = \frac{\text{RTT}}{2}
     \]

---

## 📈 Results and Analysis  

The `results/` folder includes all the RTT and latency measurements collected during the project. Analysis of the results focuses on:  
- **RTT differences** between Wi-Fi modes  
- Trade-offs in terms of **power consumption**, **throughput**, and **latency**  

---

## 🧑‍💻 Contributing  

Contributions to improve or extend the project are welcome! If you want to:  
- Add features like **throughput measurement**  
- Improve latency recording or visualization  

Please open a pull request or issue.  

---

## 🤝 Acknowledgments  

Special thanks to:  
- **Espressif** for the ESP8266 module  
- **Adafruit** for the OLED display libraries  

---

## 📬 Contact  

For any questions, feel free to reach out:  
- **Email**: sanitycs@proton.me 
- **GitHub**: sanit0x79  

