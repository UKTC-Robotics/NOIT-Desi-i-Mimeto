int R=10000;
int Uin=5;
float Rx;
int Uout= map (A3, 0, 1023, 0, 5);


void setup() {
Serial.begin(9600);
}

void loop() {
int a = analogRead(A3);
Rx= (Uout*R)/(Uin-Uout);
Serial.println(a);
delay(500);
}
