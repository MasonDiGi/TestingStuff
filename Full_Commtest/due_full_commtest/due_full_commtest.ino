// Serial1 should be replaced with Serial2 on the actual due

String input;

void setup() {
    Serial.begin(9600);
}

void loop() {
    //Serial.println('This is a test');
    if (Serial.available()) {
        input = Serial.readString();
        Serial.println(input);
    }
}
