// #include <Servo.h>           // Servo Library
#include <Pixy2.h>              // PixyCam Library

// Servo leftMotor;             // Servo object for left servomotor
// Servo rightMotor;            // Servo object for right servomotor
Pixy2 pixy;                     // PixyCam object

#define forward 410             // Servo forward macro
#define slowForward 490         // Servo slow forward macro
#define backward 590            // Servo backward macro
#define slowBackward 510        // Servo slow forward macro
#define stopServo 500           // Servo stop macro
#define centerX 0               // Center-of-view X pixel coordinate 
#define offsetX 0               // Center-of-view pixel offset 

void setup() {
  // leftMotor.attach(10);      // Attach left servomotor
  // rightMotor.attach(11);     // Attach right servomotor
  Serial.begin(115200);         // Serial Monitor setup
  Serial.print("Starting..\n"); // Initial print
  pixy.init();                  // Initialize PixyCam
}

void loop() { 
  // Iterator variable 
  int i;
  
  // Grab signature blobs             
  pixy.ccc.getBlocks();   

  // Print blob data ot Serial Monitor
  Serial.print("Detected ");
  Serial.println(pixy.ccc.numBlocks);
  for (i=0; i<pixy.ccc.numBlocks; i++) {
    Serial.print("  block ");
    Serial.print(i);
    Serial.print(": ");
    pixy.ccc.blocks[i].print();
  }
  
  // If the signature is towards right of view..
  if (pixy.ccc.blocks[0].m_x > centerX + offsetX) {
    
    // ..robot moves right 
    pixy.setServos(stopServo, stopServo);

  // If the signature is towards left of view..
  } else if (pixy.ccc.blocks[0].m_x < centerX - offsetX) {
    
    // ..robot moves left 
    pixy.setServos(stopServo, stopServo);

  } else {
    
    // ..robot moves straight
    pixy.setServos(stopServo, stopServo);
  }
}
