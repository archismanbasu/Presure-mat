int Rmux1[4] = {9,10,11,12};
int Cmux1[4] = {4,5,6,7};
int sensorPin1 = A0;
int sigRmux1 = 13;
int sensorValue = 0;
float result = 0;

int muxChannel[10][4]={
    {0,0,0,0}, //channel 0
    {1,0,0,0}, //channel 1
    {0,1,0,0}, //channel 2
    {1,1,0,0}, //channel 3
    {0,0,1,0}, //channel 4
    {1,0,1,0}, //channel 5
    {0,1,1,0}, //channel 6
    {1,1,1,0}, //channel 7  
    {0,0,0,1}, //channel 8
    {1,0,0,1}, //channel 9
};

void setup() {
  for(int i = 0; i < 4; i++) {
    pinMode(Rmux1[i], OUTPUT);
    pinMode(Cmux1[i], OUTPUT);
  }
  pinMode(sensorPin1, INPUT);
  pinMode(sigRmux1, OUTPUT);
  Serial.begin(9600);  
}

void loop() {
  digitalWrite(sigRmux1, 1);
  for(int row = 0; row < 10; row++) {
    for(int temp = 0; temp < 4; temp++) {
      digitalWrite(Rmux1[temp], muxChannel[row][temp]);
    }
    for(int col = 0; col < 10; col++) {
      for(int temp = 0; temp < 4; temp++) {
        digitalWrite(Cmux1[temp], muxChannel[col][temp]);
      }
      sensorValue = analogRead(sensorPin1);
      result = (5.0 / 1023.0) * sensorValue;
      Serial.print(result*4);
      if (col < 9) Serial.print(","); // Comma between values in a row
    }
    Serial.println(); // New line after each row
  }
  digitalWrite(sigRmux1, 0);
  Serial.println("End of Loop");
  delay(1000); // Delay to avoid flooding the serial output
}
