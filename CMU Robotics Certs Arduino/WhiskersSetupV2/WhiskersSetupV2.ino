// Whisker Setup
// Test that the whiskers are correctly working by driving forward
// if the right whisker is not pressed in.

// Macros for storing various servomotor speeds
#define stopServo 1500
#define forward 1700
#define reverse 1300

// Macros for storing speaker port
#define speakerPort 4

// Macros for storing whisker data to improve code readibility
#define whiskerRight digitalRead(7)
#define pressed 0

//Servo Include Library and right and left servo definitions
#include <Servo.h>
Servo servoLeft;
Servo servoRight;

void setup()                                 // Built-in setup() initialization function runs once
{
  pinMode(7, INPUT);                         // Set right whisker to input pin 7

  servoLeft.attach(10);                      // Set left servo to pin 10
  servoRight.attach(11);                     // Set right servo to pin 11

  tone(speakerPort, 2000, 1000);             // Play tone for 1 second
  delay(1000);                               // Delay for tone to finish
}
 
void loop()                                  // Built-in loop repeats forever after setup() function finishes
{
  if(whiskerRight == pressed)                // If right whisker is pressed...
  {
    // ...stop.
    servoLeft.writeMicroseconds(stopServo);       
    servoRight.writeMicroseconds(stopServo);
  
  }
  else                                       // Else (right whisker is not pressed)...
  {
    // ...move forward. 
    servoLeft.writeMicroseconds(forward);    // Left wheel counterclockwise
    servoRight.writeMicroseconds(reverse);   // Right wheel clockwise
  }
}
