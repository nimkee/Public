#include <Servo.h> // Include servo library

Servo leftMotor; // Declare "left" servo that will be the robot's left motor
Servo rightMotor;

void setup() {
// put your setup code here, to run once:
leftMotor.attach(10); // Left motor will be the one on port 10
rightMotor.attach(11);

leftMotor.writeMicroseconds(1700); // Set left motor signal to 1700 microsecond pulse (full speed counterclockwise)
delay(1000); // Wait 1000 milliseconds (one second) while the motor runs
leftMotor.writeMicroseconds(1500); // Set left motor signal to 1500 microsecond pulse (stop spinning)
 // Left motor will be the one on port 10

rightMotor.writeMicroseconds(1700); // Set left motor signal to 1700 microsecond pulse (full speed counterclockwise)
delay(1000); // Wait 1000 milliseconds (one second) while the motor runs
rightMotor.writeMicroseconds(1500); // Set left motor signal to 1500 microsecond pulse (stop spinning)
}

void loop() {
// put your main code here, to run repeatedly:

}
