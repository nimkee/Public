// ShieldBot Navigation with Whiskers
// Robot plays different tones based on whether
// both, one, or neither of the whiskers are pressed in.

// Macros for storing whisker data to improve code readibility
#define whiskerRight digitalRead(7)
#define whiskerLeft digitalRead(5)
#define pressed 0
#define released 1

// Macros for storing speaker port
#define speakerPort 4

void setup()                                 // Built-in setup() initialization function runs once
{
  pinMode(7, INPUT);                         // Set right whisker to input pin 7
  pinMode(5, INPUT);                         // Set left whisker to input pin 5

  tone(speakerPort, 2000, 1000);             // Play tone for 1 second
  delay(1000);                               // Delay for tone to finish
}

void loop()                                  // Built-in loop repeats forever after setup() function finishes
{
  if (whiskerLeft == pressed && whiskerRight == pressed)  // If both whiskers are pressed...
  {
    tone(speakerPort, 2000);                 // Play tone
  }
  else if (whiskerLeft == pressed)              // If only left whisker is pressed...
    {
      tone(speakerPort, 1000);               // Play tone
    }
  else if (whiskerRight == pressed)           // If only right whisker contact...
      {
        tone(speakerPort, 500);              // Play tone
      }
  else                                   // Else (no whisker is pressed)...
      {
        noTone(speakerPort);                 // Stop Playing tones
      }
    }
  }
}
