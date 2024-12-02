// Shield-Bot Programming with Pixycam2
// Matching a Signature ID
#include <Pixy2.h>

// Macros for storing speaker port
#define speakerPort 4

// Creating a Pixy2 Pixycam object to utilize its functions
Pixy2 pixy;

void setup()                                // Built-in setup() initialization function runs once
{  
  pixy.init();                              // Initializing the pixycam 
}

void loop() {
  // put your main code here, to run repeatedly:
  pixy.ccc.getBlocks();
  if (pixy.ccc.blocks[0].m_signature == 1) // If the pixycam sees ID of signature 1
  {
    tone(speakerPort, 1000);               // Play a tone
  }
  else                                     //Else (signature 1 is not seen by the pixycam
  {
    noTone(speakerPort);                   // Stop playing tone
  }
}
