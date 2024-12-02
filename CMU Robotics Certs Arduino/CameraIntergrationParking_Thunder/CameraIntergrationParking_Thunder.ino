#include <Pixy2.h>              // PixyCam Library
Pixy2 pixy;                     // PixyCam object

// Macros for storing color signatures, replace 0 with the desginated values
#define redSig 1
#define yellowSig 2
#define greenSig 3

// Macros for storing digital pins, replace 0 with the desginated values
#define redLED 9
#define yellowLED 7
#define greenLED 5

//Macros from the Approach Configuration
#define blockWidth 20           // Block width

//Macros from theh Centering Configuration
#define centerX 158               // Center-of-view X pixel coordinate 
#define offsetX 25               // Center-of-view pixel offset 


//Pixy Servo Speed Macros (do not change)
#define forward 410             // Servo forward macro
#define slowForward 490         // Servo slow forward macro
#define backward 590            // Servo backward macro
#define slowBackward 510        // Servo slow forward macro
#define stopServo 500           // Servo stop macro


void setup() {
  pinMode(redLED, OUTPUT);
  pinMode(yellowLED, OUTPUT);
  pinMode(greenLED, OUTPUT);
  Serial.begin(115200);         // Serial Monitor setup
  Serial.print("Starting..\n"); // Initial print
  pixy.init();                  // Initialize PixyCam
}

void loop() {
  // Grab signature blobs
  pixy.ccc.getBlocks();

  //LED Status Lights
  if (pixy.ccc.blocks[0].m_signature == redSig)
  {
    digitalWrite(redLED, HIGH);
    digitalWrite(yellowLED, LOW);
    digitalWrite(greenLED, LOW);
  }
  else if (pixy.ccc.blocks[0].m_signature == yellowSig)
  {
    digitalWrite(yellowLED, HIGH);
    digitalWrite(redLED, LOW);
    digitalWrite(greenLED, LOW);
  }
  else if (pixy.ccc.blocks[0].m_signature == greenSig)
  {
    digitalWrite(greenLED, HIGH);
    digitalWrite(redLED, LOW);
    digitalWrite(yellowLED, LOW);
  }
  else
  {
    digitalWrite(redLED, LOW);
    digitalWrite(yellowLED, LOW);
    digitalWrite(greenLED, LOW);
  }
  
  //Approach and Centering 
  // If signatures blobs are smaller than the width
  if (pixy.ccc.blocks[0].m_width < blockWidth) {

    // If the signature is towards right of view..
    if (pixy.ccc.blocks[0].m_x > centerX + offsetX) {

      // ..robot moves right
      pixy.setServos(backward, stopServo);

      // If the signature is towards left of view..
    } else if (pixy.ccc.blocks[0].m_x < centerX - offsetX) {

      // ..robot moves left
      pixy.setServos(stopServo, forward);

    } else {

      // ..robot moves straight
      pixy.setServos(backward, forward);
    }
  } else {
    // ..stop servomotors
    pixy.setServos(stopServo, stopServo);
  }
}
