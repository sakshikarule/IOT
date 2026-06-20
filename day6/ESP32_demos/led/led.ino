// Built-in LED pin for NodeMCU ESP8266
#define LED_PIN 2

void setup() {
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  digitalWrite(LED_PIN, LOW);   // LED ON (active LOW)
  delay(1000);                  // Wait 1 second

  digitalWrite(LED_PIN, HIGH);  // LED OFF
  delay(1000);                  // Wait 1 second
}