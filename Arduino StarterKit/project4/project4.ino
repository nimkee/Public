#include "arduino_secrets.h"

const int greenLEDPin = 9;
const int redLEDPin = 10;
const int blueLEDPin = 11;
const int redSensorPin = A0;
const int greenSensorPin = A1;
const int blueSensorPin = A2;

int redV = 0;
int greenV = 0;
int blueV = 0;

int redSensorV = 0;
int greenSensorV = 0;
int blueSensorV = 0;


void setup() {
  Serial.begin(9600);
  pinMode(greenLEDPin, OUTPUT);
  pinMode(redLEDPin, OUTPUT);
  pinMode(blueLEDPin, OUTPUT);
}

void loop() {
  redSensorV = analogRead(redSensorPin);
  delay(5);
  greenSensorV = analogRead(greenSensorPin);
  delay(5);
  blueSensorV = analogRead(blueSensorPin);
  
  Serial.print("Raw Sensor Values \t red: ");
  Serial.print(redSensorV);
  Serial.print("\t green: ");
  Serial.print(greenSensorV);
  Serial.print("\t blue: ");
  Serial.print(blueSensorV);
  redV = redSensorV/4;
  greenV = greenSensorV/4;
  blueV = blueSensorV/4;
  Serial.print('\n');
  Serial.print("Mapped Sensor Values \t red: ");
  Serial.print(redV);
  Serial.print("\t green: ");
  Serial.print(greenV);
  Serial.print("\t blue: ");
  Serial.print(blueV);
  Serial.println();
  delay(500);
  analogWrite(redLEDPin, redV);
  analogWrite(greenLEDPin, greenV);
  analogWrite(blueLEDPin, blueV);


}
