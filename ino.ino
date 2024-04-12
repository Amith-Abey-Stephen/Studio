#include <Servo.h>

Servo servoMotor; // create servo object to control a servo

int servoPin = 9; // define the pin for the servo control

void setup() {
  servoMotor.attach(servoPin); // attaches the servo on pin 9 to the servo object
}

void loop() {
  // Move the servo to 240 degrees
  servoMotor.write(240); // tell servo to go to 240 degrees
  delay(1000); // wait for servo to reach the position
  
  // You can add more code here for other operations or movements
  
  // Move the servo back to 0 degrees
  servoMotor.write(0); // tell servo to go to 0 degrees
  delay(1000); // wait for servo to reach the position
  
  // You can add more code here for other operations or movements
}
