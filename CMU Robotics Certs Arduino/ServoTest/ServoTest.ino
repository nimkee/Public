#include <Servo.h> // Include servo library

Servo leftMotor; // Declare "left" servo that will be the robot's left motor
Servo rightMotor;

void setup() {
// put your setup code here, to run once:
leftMotor.attach(11); // Left motor will be the one on port 10
rightMotor.attach(10); // Left motor will be the one on port 11
leftMotor.writeMicroseconds(1700); // Set left motor signal to 1300 microsecond pulse (full speed clockwise)
rightMotor.writeMicroseconds(1300);
}

void loop() {
// put your main code here, to run repeatedly:

}
