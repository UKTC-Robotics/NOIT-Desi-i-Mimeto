int R=10000;
int Uin=5;
float Rx = 0;



void setup() {
 Serial.begin(9600);
}

void loop() {
  int a = analogRead(A3);
  float Uout= mapfloat(a, 0, 1023, 0, 5);
  if(Uin == Uout)
    Rx = 0;
  else
    Rx= (Uout*R)/(Uin-Uout);
  Serial.println(Rx);
  delay(500);
}

float mapfloat(long x, long in_min, long in_max, long out_min, long out_max)
{
  return (float)(x - in_min) * (out_max - out_min) / (float)(in_max - in_min) + out_min;
}
