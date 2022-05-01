#include<Servo.h>
#include<SPI.h>

//pins for sorting mechanism
#define echoObj 6
#define trigObj 7
#define servoPin 8

//constants to test conditions
#define bin_distance 18

int flag;
int distance;
Servo servo;

int usRead(int echo, int trig){
  long duration, distance;
  digitalWrite(trig, LOW);
  delayMicroseconds(2);
  digitalWrite(trig,HIGH);
  delayMicroseconds(10);
  digitalWrite(trig,LOW);
  duration = pulseIn(echo, HIGH);
  distance = (duration/2)/29.1;
  return distance;
}

void left(){
  servo.write(145);
  delay(2000);
  servo.write(90);
}

void right(){
  servo.write(35);
  delay(2000);
  servo.write(90);
}

void setup() {
  
  //initialize servo and set to horizontal
  servo.attach(servoPin);
  servo.write(90);

  //initialize ultrasonic sensor pins
  pinMode(trigObj, OUTPUT);
  pinMode(echoObj, INPUT);

  Serial.begin(9600);
  while(!Serial);
}

void loop() {
  
  //to detect trash being deposited
  distance = usRead(echoObj, trigObj);

  //if there is trash detected
  if (distance < bin_distance){
    Serial.println("python");

    //wait for python to send signal
    while(Serial.available() <= 0);
    
    while(Serial.available()>0){
      
      //sorts trash according to label assigned by clarifai
      flag = Serial.parseInt();
      if (flag == 0){
        left();
      }
      else{
        right();
      }
    }

    //delay to give time to sorting process
    delay(5000);
  }
  
  delay(1000);
}
