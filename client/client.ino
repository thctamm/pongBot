#include <Servo.h> 

#define STEPS 512

#define ARM_PIN 7
#define RACK_A 8
#define RACK_B 9

Servo armServo;

void setup(void)
{
    Serial.begin(9600);
    pinMode(RACK_A, OUTPUT);
    pinMode(RACK_B, OUTPUT);
    armServo.attach(ARM_PIN);
    armServo.write(90);
    digitalWrite(RACK_A, HIGH);
    digitalWrite(RACK_B, HIGH);
}
 
int read_message() {
    if (Serial.available() == 0) {
        return 0;
    }

    int inChr;
    inChr = Serial.read();
    Serial.println(inChr);
    return inChr;
}

void shoot() {
    armServo.write(180);
    delay(400);
    armServo.write(90);
    delay(500);
    armServo.write(0);
    delay(1000);
    armServo.write(90);
}

void turn_left() {
  digitalWrite(RACK_B, LOW);
  delay(500);
  digitalWrite(RACK_B, HIGH);
}

void turn_right() {
  digitalWrite(RACK_A, LOW);
  delay(500);
  digitalWrite(RACK_A, HIGH);
}

void loop(void) {
  if (Serial.available() > 0) {
    int cmd = Serial.parseInt();
    switch (cmd) {
      case 1:
        shoot();
        break;
      case 2:
        turn_left();
        break;
      case 3:
        turn_right();
        break;
      default:
        break;
    }
  }
  delay(500);
}
