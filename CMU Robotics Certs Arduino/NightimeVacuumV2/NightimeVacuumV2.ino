// Nighttime Vacuume
// Robot drives through an environment and moves differently based on whether
// both, one, or neither of the whiskers are pressed in, WHILE the lights in 
// the room are turned off (or low).

// Macros for storing various servomotor speeds
#define stopServo 1500
#define forward 1700
#define reverse 1300

// Macros for storing whisker data to improve code readibility
#define whiskerRight digitalRead(7)
#define whiskerLeft digitalRead(5)
#define pressed 0
#define released 1

// Macros for storing speaker and phototransistor ports
#define speakerPort 4
#define phototransistor analogRead(A3)

//Servo Include Library and right and left servo definitions
#include <Servo.h>
Servo servoLeft;
Servo servoRight;

void setup()                                 // Built-in setup() initialization function runs once
{
  pinMode(7, INPUT);                         // Set right whisker to input pin 7
  pinMode(5, INPUT);                         // Set left whisker to input pin 5

  servoLeft.attach(10);                      // Set left servo to pin 10
  servoRight.attach(11);                     // Set right servo to pin 11
  
  Serial.begin(9600);
  tone(speakerPort, 2000, 1000);             // Play tone for 1 second
  delay(1000);                               // Delay for tone to finish
}

void loop()                                  // Main loop auto-repeats
{
  Serial.println(phototransistor);           // Prints phototransistor level
  
  if (phototransistor < 120)
  {
    if (whiskerLeft == pressed && whiskerRight == pressed)  // If both whiskers are pressed...
    {
      // ...Move Backwards
      servoLeft.writeMicroseconds(reverse);    // Left wheel clockwise
      servoRight.writeMicroseconds(forward);   // Right wheel counterclockwise
      delay(1000);                             // Back up 1 second

      // Turn Left
      servoLeft.writeMicroseconds(reverse);    // Left wheel clockwise
      servoRight.writeMicroseconds(reverse);   // Right wheel clockwise
      delay(800);                              // Turn left about 120 degrees
    }
    else if (whiskerLeft == pressed)           // Else, If only left whisker is pressed...
    {
      // ...Move Backwards
      servoLeft.writeMicroseconds(reverse);    // Left wheel clockwise
      servoRight.writeMicroseconds(forward);   // Right wheel counterclockwise
      delay(1000);                             // Back up 1 second

      // Turn Right
      servoLeft.writeMicroseconds(forward);    // Left wheel counterclockwise
      servoRight.writeMicroseconds(forward);   // Right wheel counterclockwise
      delay(400);                              // Maneuver for time ms
    }
    else if (whiskerRight == pressed)          // Else, If only right whisker contact...
    {
      // ...Move Backwards
      servoLeft.writeMicroseconds(reverse);    // Left wheel clockwise
      servoRight.writeMicroseconds(forward);   // Right wheel counterclockwise
      delay(1000);                             // Back up 1 second

      // Turn Left
      servoLeft.writeMicroseconds(reverse);    // Left wheel clockwise
      servoRight.writeMicroseconds(reverse);   // Right wheel clockwise
      delay(400);
    }
    else                                       // Else (no whisker is pressed)...
    {
      // ...Move Forward
      servoLeft.writeMicroseconds(forward);    // Left wheel counterclockwise
      servoRight.writeMicroseconds(reverse);   // Right wheel clockwise
    }
  }
  else
  {
    // Stop Motors
    servoLeft.writeMicroseconds(stopServo);    
    servoRight.writeMicroseconds(stopServo);
  }

}
