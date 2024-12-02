// Camera Integration with Arduino (ShieldBot)
// LED Status Lights
#include <Pixy2.h>

// Macros for storing color signatures, replace 0 with the desginated values
#define redSig 0
#define blueSig 0
#define greenSig 0

// Macros for storing digital pins, replace 0 with the desginated values
#define redLED 0
#define blueLED 0
#define greenLED 0

// Creating a Pixy2 Pixycam object to utilize its functions
Pixy2 pixy;

void setup()                                // Built-in setup() initialization function runs once
{
  pinMode(redLED, OUTPUT);
  pinMode(blueLED, OUTPUT);
  pinMode(greenLED, OUTPUT);


  pixy.init();                              // Initializing the pixycam
}

void loop() {
  // put your main code here, to run repeatedly:
  pixy.ccc.getBlocks();
  if (pixy.ccc.blocks[0].m_signature == redSig) // If the pixycam sees ID of signature 1
  {
    digitalWrite(redLED, HIGH);
    digitalWrite(blueLED, LOW);
    digitalWrite(greenLED, LOW);
    

  }
  else if (pixy.ccc.blocks[0].m_signature == blueSig)                                    //Else (signature 1 is not seen by the pixycam
  {
    digitalWrite(blueLED, HIGH);
    digitalWrite(redLED, LOW);
    digitalWrite(greenLED, LOW);
  }
  else if (pixy.ccc.blocks[0].m_signature == greenSig)                                    //Else (signature 1 is not seen by the pixycam
  {
    digitalWrite(greenLED, HIGH);     
    digitalWrite(redLED, LOW);
    digitalWrite(blueLED, LOW);
  }
  else
  {
    digitalWrite(redLED, LOW);
    digitalWrite(blueLED, LOW);
    digitalWrite(greenLED, LOW);
  }
}
