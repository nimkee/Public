// Piezospeaker Demo
// Use the piezo speaker to play a tone at one frequency during the setup() function, and
// then separate frequencies after each forward and turn robot behavior in the loop() function.

// Macros for storing various servomotor speeds
#define stopServo 1500
#define forward 1700
#define reverse 1300

// Macros for storing speaker port
#define speakerPort 4

//Servo Include Library and right and left servo definitions
#include <Servo.h>
Servo servoLeft;
Servo servoRight;

void setup()                                 // Built-in setup() initialization function runs once
{
  servoLeft.attach(10);                      // Set left servo to pin 10
  servoRight.attach(11);                     // Set right servo to pin 11

  tone(speakerPort, 2000, 1000);             // Play tone for 1 second
  delay(1000);                               // Delay for tone to finish
}

void loop()                                  // Built-in loop repeats forever after setup() function finishes
{
    // Move Forward for 1 second
    servoLeft.writeMicroseconds(forward);
    servoRight.writeMicroseconds(reverse);
    delay(1000);
    servoLeft.writeMicroseconds(stopServo);
    servoRight.writeMicroseconds(stopServo);

    tone(speakerPort, 500, 1000);             // Play tone for 1 second
    delay(1000);  

    // Turn Right for 0.4 seconds
    servoLeft.writeMicroseconds(forward);
    servoRight.writeMicroseconds(forward);
    delay(550);
    servoLeft.writeMicroseconds(stopServo);
    servoRight.writeMicroseconds(stopServo);

    tone(speakerPort, 1500, 1000);             // Play tone for 1 second
    delay(1000);  
}
