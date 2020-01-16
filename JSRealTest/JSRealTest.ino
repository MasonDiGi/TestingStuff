#include <Joystick.h>
#include <HID.h> 


int VRXPin = A1;
int VRYPin = A0;;
int SWPin = 2;
int VRX;
int VRY;
int SW;


String txt;
String val;

void setup () {
    Joystick.clearState();
    Serial.begin(9600);
    pinMode(SWPin, INPUT_PULLUP);
}

void loop() { 
    VRX = analogRead(VRXPin);
    VRY = analogRead(VRYPin);
    SW = !digitalRead(SWPin);

    Serial.println(VRX);

    Joystick.state.buttons.data1 = SW;
    Joystick.state.x.axis = VRX;
    Joystick.state.y.axis = VRY;
    Joystick.sendState();
    Joystick.clearState();
    
}
