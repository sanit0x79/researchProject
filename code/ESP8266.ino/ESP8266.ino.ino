#include <Wire.h>
#include <Adafruit_SSD1306.h>
#include <ESP8266WiFi.h>

#define SCREEN_WIDTH 128  // OLED display width, in pixels
#define SCREEN_HEIGHT 64 // OLED display height, in pixels

#define OLED_RESET    -1   // Reset pin # (or -1 if sharing Arduino reset pin)
#define SCREEN_ADDRESS 0x3C // Change if needed

// Default I2C pins for ESP8266 (D1 -> SCL, D2 -> SDA)
#define OLED_SDA 14  // D2 (GPIO4)
#define OLED_SCL 12  // D1 (GPIO5)

// SSID and PASSWORD for the AP
const char* ssid = "pixel1234";  // Replace with your desired SSID
const char* password = "test1234";  // Replace with your desired password
Adafruit_SSD1306 *display;
int c = 0;

void handle_oled(int c, const char* mode) {
  display->clearDisplay();
  display->setTextSize(1);
  display->setTextColor(SSD1306_WHITE);
  display->setCursor(0, 0);
  display->println("Access Point");
  display->print("SSID: ");  // Display the SSID of the AP
  display->println(ssid);
  display->print("IP: ");
  display->println(WiFi.softAPIP());  // Display the AP's IP address
  display->print("MODE: ");
  display->println(mode);  // Display the current Wi-Fi mode
  display->display();
}

void setup() {
  // Start the serial communication
  Serial.begin(115200);
  
  display = new Adafruit_SSD1306(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);
  Wire.begin(OLED_SDA, OLED_SCL);
  display->begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS);

  // Initialize the ESP8266 as an Access Point
  WiFi.mode(WIFI_AP);
  WiFi.softAP(ssid, password);  // Set up the AP with SSID and password

  // Wait for the AP to start up
  delay(1000);

  // Print the AP's IP address to the serial monitor
  Serial.print("Access Point IP Address: ");
  Serial.println(WiFi.softAPIP());

  // Set the Wi-Fi mode (here using 802.11b for demonstration)
  WiFi.setPhyMode(WIFI_PHY_MODE_11B); // Set PHY mode to 802.11b (other options: WIFI_PHY_MODE_G, WIFI_PHY_MODE_N)
}

void loop() {
  // Current mode string for display
  const char* currentMode = "802.11b";  // Adjust this based on the current Wi-Fi mode

  // Call the function to update OLED
  handle_oled(c, currentMode);
  c++;
  delay(1000);  // Update every second if necessary
}
