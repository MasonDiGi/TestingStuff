String input;

void setup() {
    Serial.begin(9600);
}

void loop() {
    //Serial.println('This is a test');
    if (Serial.available()) {
        input = Serial.read();
        Serial.print(input);
    }
}
