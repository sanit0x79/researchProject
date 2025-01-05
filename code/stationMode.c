#include <Wire.h>
#include <Adafruit_SSD1306.h>
#include <ESP8266WiFi.h>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64   
#define OLED_RESET -1  
#define SCREEN_ADDRESS 0x3C 

#define OLED_SDA 14  
#define OLED_SCL 12 

const char* ssid = "ssid here";   
const char* password = "password here";   

Adafruit_SSD1306* display;
int c = 0;

void handle_oled(int counter, const char* mode) {
  display->clearDisplay();
  display->setTextSize(1);
  display->setTextColor(SSD1306_WHITE);
  display->setCursor(0, 0);

  display->print("SSID: ");
  display->println(ssid);

  display->print("IP:   ");
  display->println(WiFi.localIP());

  display->print("MODE: ");
  display->println(mode);

  display->display();
}

void setup() {
  Serial.begin(115200);

  // setup display
  display = new Adafruit_SSD1306(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);
  Wire.begin(OLED_SDA, OLED_SCL);
  display->begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS);

  WiFi.setPhyMode(WIFI_PHY_MODE_11B);

  // station mode, this will make sure there is a bridge between the hotspot on the phone and the actual AP of the ESP
  WiFi.mode(WIFI_STA);

  WiFi.begin(ssid, password);

  Serial.println("Connecting to Wi-Fi...");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nConnected!");

  Serial.print("Station IP Address: ");
  Serial.println(WiFi.localIP());
}

void loop() {
  const char* currentMode = "802.11b";  // Need to change this, filler const for testing purposes 

  // Update the OLED display
  handle_oled(c, currentMode);
  c++;
  delay(1000);  
}
