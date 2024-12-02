#include "arduino_secrets.h"

#include <Arduino.h>

void setup() {
  Serial.begin(9600);
  pinMode(8, OUTPUT);
}

void loop() {
  int val = analogRead(A0);
  int threshold = 900;

  if (val < threshold) {
    tone(8, map(val, 0, 1023, 2000, 4000));
  }
  else { noTone(8);}
  Serial.print("Potentiometer value: ");
  Serial.print(val);
  Serial.print("\tThreshold; ");
  Serial.println(threshold);
  
  delay(100);
    
}
