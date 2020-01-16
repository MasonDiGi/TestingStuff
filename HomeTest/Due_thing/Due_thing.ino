/*

Serial1 - Leo
Serial2 - Pi

*/


#include <Joystick.h>
#include <HID.h>
#include <iostream>

int data;

void setup() {
    Serial.begin(9600);
    Serial1.begin(9600);
    Serial2.begin(9600);
}

void loop() {
    if (Serial1.available()) {    
        Serial.println("Hello there is a thing here");
        data = Serial1.read();
    }

    Joystick.clearstate();

    Joystick.state.x.axis = 100;
}