// Light Level Pitch
// Adjust the frequency of the speaker tone based on the phototransistor value.

// Macros for storing speaker and phototransistor ports
#define speakerPort 4
#define phototransistor analogRead(A3)

void setup()                  // Built-in setup() initialization function runs once
{
  //Set the Serial Monitor to run
  Serial.begin(9600);
}

void loop()                   // Built-in loop repeats forever after setup() function finishes
{
  // Integer Variable declared to store the frequency for the speaker
  int calculatedTone;
  // Calculate the frequency to send to the speaker by multiplying the phototransistor value by 2
  // Store the result in the calculatedTone Integer Variable
  calculatedTone = phototransistor * 2;
  
  //Display the calculated value on the Serial Monitor
  Serial.println(calculatedTone);

  if(calculatedTone < 100)    // If the calculatedTone variable is less than 100...
  {
    noTone(speakerPort);      // ...play no sound.
  }
  else                        // Else...
  {
    tone(speakerPort, calculatedTone);   // ...play the tone stored in the calculatedTone variable.
  }
}
