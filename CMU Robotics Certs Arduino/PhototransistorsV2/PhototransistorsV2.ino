// Phototransistor Demo
// Demo Program to view what analog values the phototransistor provides

#define phototransistor analogRead(A3)

void setup()                  // Built-in setup() initialization function runs once
{
  //Set the Serial Monitor to run
  Serial.begin(9600);
}

void loop()                   // Built-in loop repeats forever after setup() function finishes
{
  //Display the value from the phototransistor on the Serial Monitor
  Serial.println(phototransistor);
  //delay(500);
}
