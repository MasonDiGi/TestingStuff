String input;
int inputPin = 13;
boolean currentVal;
void setup() {
    Serial1.begin(9600);
    Serial.begin(9600);
    pinMode(inputPin, INPUT_PULLUP);
}

void loop() {
    //Serial.println('This is a test');
    currentVal  = digitalRead(inputPin);
    Serial1.write(currentVal);
    Serial.println(currentVal);
}
