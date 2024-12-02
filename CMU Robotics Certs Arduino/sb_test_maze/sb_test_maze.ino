#include <Servo.h> // Include servo library

Servo leftMotor; // Declare "left" servo that will be the robot's left motor
Servo rightMotor; // Declare "right" servo that will be the robot's left motor


void setup() {

leftMotor.attach(10); // Left motor will be the one on port 10
rightMotor.attach(11); // Right motor will be the one on port 11

leftMotor.writeMicroseconds(1700); // Set left motor signal to 1700 microsecond pulse (full speed counterclockwise)
rightMotor.writeMicroseconds(1300); // Set right motor signal to 1700 microsecond pulse (full speed counterclockwise)
delay(4000); // Wait 1000 milliseconds (one second) while both motors are running

rightMotor.writeMicroseconds(1500);
delay(1100);

rightMotor.writeMicroseconds(1300);
delay(6000);

leftMotor.writeMicroseconds(1500); // Set right motor signal to 1500 microsecond pulse (stop spinning)
delay(1000);

leftMotor.writeMicroseconds(1700);
delay(3000);

leftMotor.writeMicroseconds(1500);
delay(1000);

leftMotor.writeMicroseconds(1700);
delay(3000);

leftMotor.writeMicroseconds(1500);
rightMotor.writeMicroseconds(1500);

// Trying to set the opposite commands to back out of the maze
delay(4000);

// This code backs it out and turns it around to face forward and start going back through the maze

leftMotor.writeMicroseconds(1700); // Set left motor signal to 1700 microsecond pulse (full speed counterclockwise)
rightMotor.writeMicroseconds(1700); // Set right motor signal to 1700 microsecond pulse (full speed counterclockwise)
delay(3000); // Wait 1000 milliseconds (one second) while both motors are running

rightMotor.writeMicroseconds(1500);
delay(1000);

leftMotor.writeMicroseconds(1500);
rightMotor.writeMicroseconds(1500);

}

void loop() {
// Can I just reverse the code above once it works to make it back out of the maze?

}
