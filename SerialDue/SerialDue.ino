int ser2Data;
int ser3Data;

void setup() {
  Serial1.begin(9600);
  Serial2.begin(9600);
  Serial3.begin(9600);
  SerialUSB.begin(9600);
}

void loop() {
  if (Serial2.available()) {
    ser2Data = Serial2.read();
    while (ser2Data != 0x02) {
      delay(1);
      ser2Data = Serial2.read();
    }
      while (ser2Data != 0x03) {
        delay(1);
        ser2Data = Serial2.read();
        if (ser2Data != 0x03 && ser2Data != 0x02 && ser2Data != -1) {
          SerialUSB.print("LEO - ");
          SerialUSB.println(ser2Data);
        }
      }
  }
  if (Serial3.available()) {
    ser3Data = Serial3.read();
    while (ser3Data != 0x02) {
      delay(1);
      ser3Data = Serial3.read();
    }
      while (ser3Data != 0x03) {
        delay(1);
        ser3Data = Serial3.read();
        if (ser3Data != 0x03 && ser3Data != 0x02 && ser3Data != -1) {
          SerialUSB.print("PI - ");
          SerialUSB.println(ser3Data);
        }
    }
  }
}
