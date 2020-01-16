#include <Joystick.h>
#include <HID.h> 


int VRXPin = A0;
int VRYPin = A1;
int SWPin = 51;
int VRX;
int VRY;
int SW;


String txt;
String val;

void setup () {
    //Joystick.clearState();
    Serial.begin(9600); 
    SerialUSB.begin(9600);
    pinMode(VRXPin, INPUT);
    pinMode(VRYPin, INPUT);
    pinMode(SWPin, INPUT_PULLUP);
    val = "HEllo";
}

void loop() { 
    VRX = analogRead(VRXPin);
    VRY = analogRead(VRYPin);
    SW = digitalRead(SWPin);
    Serial.println(val);
    SerialUSB.println(val);
    if (Serial.available()) {
      txt = Serial.readString();
    }
    if (txt.equals("VRX")) {
      val = "VRX";
    } else if (txt.equals("VRY")) {
      val = "VRY";
    } else if (txt.equals("SW")) {
      val = "SW";
    }
    
}
