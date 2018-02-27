float value;

void setup() {
  Serial.begin(9600);
  pinMode(A1,INPUT) ;
}

void loop() {
  value = analogRead(A1);
  Serial.println(value);
  delay(250);
}
