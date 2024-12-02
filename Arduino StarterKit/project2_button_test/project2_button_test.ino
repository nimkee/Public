#include "arduino_secrets.h"

int switchState = 0;
void setup() {
  // put your setup code here, to run once:
  pinMode(7, OUTPUT);
  //pinMode(4, OUTPUT);
  //pinMode(5, OUTPUT);
  pinMode(5, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  switchState = digitalRead(2);
  if(switchState == LOW) {
    //the button is not pressed
    digitalWrite(7, HIGH); //Green led
    //digitalWrite(4, LOW); //Red LEDs
    //digitalWrite(5, LOW);
  }
  else{ //BUTTON IS PRESSED
    digitalWrite(3, LOW);
    digitalWrite(4, HIGH);
    digitalWrite(5, HIGH);

    delay(250); // wait for a quarter second
    //toggle the LEDs
    digitalWrite(4, HIGH);
    digitalWrite(5, HIGH);
    delay(500); // wait half a second
  }
} // go back to beginning of the loop
