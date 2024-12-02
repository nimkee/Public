// #include <Servo.h>              // Servo Library
#include <Pixy2.h>              // PixyCam Library

// Servo leftMotor;                // Servo object for left servomotor
// Servo rightMotor;               // Servo object for right servomotor
Pixy2 pixy;                     // PixyCam object

#define forward 1700            // Servo forward macro
#define backward 1300           // Servo backward macro
#define stopServo 1500          // Servo stop macro

void setup() {
  leftMotor.attach(10);         // Attach left servomotor
  rightMotor.attach(11);        // Attach right servomotor
  Serial.begin(115200);         // Serial Monitor setup
  Serial.print("Starting..\n"); // Initial print
  pixy.init();                  // Initialize PixyCam
}

void loop() { 
  // Iterator variable 
  int i;
  
  // Grab signature blobs             
  pixy.ccc.getBlocks();         

  // If signatures blobs are detected..
  if (pixy.ccc.numBlocks) {   
       
    // ..run servomotors      
    leftMotor.writeMicroseconds(stopServo);
    rightMotor.writeMicroseconds(stopServo);

    // Print blob data ot Serial Monitor
    Serial.print("Detected ");
    Serial.println(pixy.ccc.numBlocks);
    for (i=0; i<pixy.ccc.numBlocks; i++) {
      Serial.print("  block ");
      Serial.print(i);
      Serial.print(": ");
      pixy.ccc.blocks[i].print();
    }
    
  } else {
    // ..stop servomotors      
    leftMotor.writeMicroseconds(forward);
    rightMotor.writeMicroseconds(backward);
  }
}
