

int a, b, c, d, e;

void setup() {
  Serial.begin(9600);
}

void loop() {
  a = analogRead(A0);
  b = analogRead (A1);
  c = analogRead (A2);
  d = analogRead (A3);
  e = analogRead (A4);
  Serial.print("#");
  Serial.print(a);
  Serial.print("#");
  Serial.print(b);
  Serial.print("#");
  Serial.print(c);
  Serial.print("#");
  Serial.print(d);
  Serial.print("#");
  Serial.print(e);
  Serial.println ("#");
  delay(500);
}
