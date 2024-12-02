#include <Servo.h> // Include servo library

Servo leftMotor; // Declare "left" servo that will be the robot's left motor
Servo rightMotor; // Declare "right" servo that will be the robot's left motor


void setup() {
// put your setup code here, to run once:
leftMotor.attach(10); // Left motor will be the one on port 10
rightMotor.attach(11); // Right motor will be the one on port 11

leftMotor.writeMicroseconds(1700); // Set left motor signal to 1700 microsecond pulse (full speed counterclockwise)
rightMotor.writeMicroseconds(1300); // Set right motor signal to 1700 microsecond pulse (full speed counterclockwise)
delay(1000); // Wait 1000 milliseconds (one second) while both motors are running

leftMotor.writeMicroseconds(1500);
//leftMotor.writeMicroseconds(1700);
//rightMotor.writeMicroseconds(1300);
delay(1000);

rightMotor.writeMicroseconds(1500); // Set right motor signal to 1500 microsecond pulse (stop spinning)

}

void loop() {
// put your main code here, to run repeatedly:

}
