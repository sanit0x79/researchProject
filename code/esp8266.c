#include <Wire.h>
#include <Adafruit_SSD1306.h>
#include <ESP8266WiFi.h>

#define SCREEN_WIDTH 128 
#define SCREEN_HEIGHT 64

#define OLED_RESET    -1   
#define SCREEN_ADDRESS 0x3C 

#define OLED_SDA 14  // D2 (GPIO4)
#define OLED_SCL 12  // D1 (GPIO5)

const char* ssid = "SSID";  // Replace with your desired SSID
const char* password = "PASSWORD";  // Replace with your desired password
Adafruit_SSD1306 *display;
int c = 0;

const char* getCurrentMode() {
  switch (WiFi.getPhyMode()) {
    case WIFI_PHY_MODE_11B:
      return "802.11b";
    case WIFI_PHY_MODE_11G:
      return "802.11g";
    case WIFI_PHY_MODE_11N:
      return "802.11n";
    default:
      return "Unknown";
  }
}

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
  Serial.begin(115200);
  
  display = new Adafruit_SSD1306(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);
  Wire.begin(OLED_SDA, OLED_SCL);
  display->begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS);

  WiFi.mode(WIFI_AP);
  WiFi.softAP(ssid, password);  

  delay(1000);

  Serial.print("Access Point IP Address: ");
  Serial.println(WiFi.softAPIP());

  WiFi.setPhyMode(WIFI_PHY_MODE_11B); // Options: WIFI_PHY_MODE_11B, WIFI_PHY_MODE_11G, WIFI_PHY_MODE_11N
}

void loop() {
  const char* currentMode = getCurrentMode();

  handle_oled(c, currentMode);
  c++;
  delay(1000);  // Update every second if necessary

  if (c % 10 == 0) {
    WiFi.setPhyMode(WIFI_PHY_MODE_11G); // Switch to 802.11g
  } else if (c % 20 == 0) {
    WiFi.setPhyMode(WIFI_PHY_MODE_11N); // Switch to 802.11n
  } else if (c % 30 == 0) {
    WiFi.setPhyMode(WIFI_PHY_MODE_11B); // Switch back to 802.11b
  }
}
