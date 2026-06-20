
#define LDR_PIN   34

void setup() {
  // put your setup code here, to run once:

  Serial.begin(230400);

  pinMode(LDR_PIN, INPUT);

  Serial.println("ADC and UART setup is done");
}

void loop() {
  // put your main code here, to run repeatedly:
  int value = analogRead(LDR_PIN);

  Serial.printf("LDR value = %d\n", value);

  delay(4000);
}





