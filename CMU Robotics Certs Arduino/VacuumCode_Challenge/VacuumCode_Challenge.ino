// ShieldBot Navigation with Whiskers
// Robot plays different tones based on whether both, one, or neither of the whiskers are pressed in.
// Robot will also reverse or back up in a direction opposite to the whisker(s) touched
#include <Servo.h>

Servo servoLeft;
Servo servoRight;

#define stopServo 1500
#define forward 1700
#define reverse 1300

#define whiskerR digitalRead(7)
#define whiskerL digitalRead(5)
#define pressed 0
#define released 1

// Macros for storing speaker port
#define speakerPort 4

void setup()                                 // Built-in setup() initialization function runs once
{
  pinMode(7, INPUT);                         // Set right whisker to input pin 7
  pinMode(5, INPUT);                         // Set left whisker to input pin 5
  servoLeft.attach(10);
  servoRight.attach(11);

  tone(speakerPort, 3000, 1000);             // Play tone for 1 second
  delay(500);                               // Delay for tone to finish
}

void loop()                                  // Built-in loop repeats forever after setup() function finishes
{
  if (whiskerL == pressed && whiskerR == pressed)  // If both whiskers are pressed...
  {
    tone(speakerPort, 2000);                 // Play tone
    servoLeft.writeMicroseconds(reverse);
    servoRight.writeMicroseconds(forward);
    delay(500);
    servoLeft.writeMicroseconds(reverse);
    servoRight.writeMicroseconds(reverse);
    delay(500);
  }
  else if (whiskerL == pressed)              // If only left whisker is pressed...
    {
      tone(speakerPort, 1000);               // Play tone
      servoLeft.writeMicroseconds(reverse);
      delay(1000);
    }
  else if (whiskerR == pressed)           // If only right whisker contact...
      {
        tone(speakerPort, 500);              // Play tone
        servoRight.writeMicroseconds(forward);
      delay(1000);
      }
  else                                   // Else (no whisker is pressed)...
      {
        noTone(speakerPort);                 // Stop Playing tones
        servoLeft.writeMicroseconds(forward);
        servoRight.writeMicroseconds(reverse);
      }
    }

