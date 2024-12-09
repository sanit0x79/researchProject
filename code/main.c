#include <WiFi.h>
#include "secret.h"

const char* ssid = SSID;
const char* password = PASSWORD;

void setup() {
  Serial.begin(115200);

  WiFi.mode(WIFI_MODE_AP);
  WiFi.softAP(ssid, password);

  WiFi.softAPsetProtocol(WIFI_PROTOCOL_11B);  // change to 11G or 11N for different Wi-Fi modes 
  Serial.print("Access Point IP Address: ");
  Serial.println(WiFi.softAPIP());
}

void loop() {
}
