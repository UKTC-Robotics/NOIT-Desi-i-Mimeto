void setup() {
  Serial.begin(9600);
}

void loop() {
  float voltage, in;
  int range= 10;     // goren obhvat na izmervane
  in= analogRead(A0);
  voltage = mapfloat(in, 0, 1023, 0, range);
  Serial.println(voltage);
  delay(50);
}


float mapfloat(long x, long in_min, long in_max, long out_min, long out_max)
{
 return (float)(x - in_min) * (out_max - out_min) / (float)(in_max - in_min) + out_min;
}
