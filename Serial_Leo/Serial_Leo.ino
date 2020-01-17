String txt;
//byte var[3];
byte var = 0x31;

void setup() {
  Serial1.begin(9600);
  /*for (int i = 0; i < 3; i++) {
    var[i] = 0x31 + i;
  }*/
}

void loop() {
  delay(500);
  //Serial.println(sizeof(var)/sizeof(int));
  Serial1.write(0x02);
  //for (int i = 0; i < 1; i++) {
    Serial1.write(var);
    Serial1.write(0x32);
  //}
  Serial1.write(0x03);
}
