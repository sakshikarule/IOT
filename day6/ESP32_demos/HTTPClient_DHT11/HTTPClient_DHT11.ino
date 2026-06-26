#include<WiFi.h>
#include<HTTPClient.h>
#include "DHT.h"

#define DHT_PIN   5
#define DHT_TYPE  DHT11

DHT dht(DHT_PIN, DHT_TYPE);

const char *ssid = "HEARTBEAT-403_5G";
const char *password = "heartbeat403";

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);

  dht.begin();

  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  Serial.print("Connecting to WiFi");
  while(WiFi.status() != WL_CONNECTED)
  {
    Serial.print(".");
    delay(500);
  }
  Serial.print("\nConnected to WiFi");
  Serial.print("IP Address : ");
  Serial.println(WiFi.localIP());

}

void loop() {
  // put your main code here, to run repeatedly:
  float temp = dht.readTemperature();
  float humidity = dht.readHumidity();
  
  String body = "{\"location\":\"Nira\",\"temperature\":" + String(temp) + ",\"humidity\":" + String(humidity) + "}";

  //Serial.println(body);

  WiFiClient wifiClient;
  HTTPClient httpClient;
  httpClient.begin(wifiClient, "http://127.0.0.1:5000/sensorslog");
  httpClient.addHeader("Content-Type", "application/JSON");

  int status = httpClient.POST(body);

  Serial.printf("Status = %d\n", status);
  httpClient.end();

  delay(5000);

}










