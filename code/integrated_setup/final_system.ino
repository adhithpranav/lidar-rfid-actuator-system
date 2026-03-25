#include <Wire.h>
#include <TFLI2C.h>
#include <Servo.h>

TFLI2C tflI2C;
Servo actuator;

int16_t tfDist;
int16_t tfAddr = TFL_DEF_ADR;

int stopSignal = 90;
int upSignal   = 0;
int downSignal = 180;

int currentStep = 0;
int targetStep  = 0;

int maxSteps = 5;

// ---- Step functions ----
void moveUpStep() {
  actuator.write(upSignal);
  delay(180);
  actuator.write(stopSignal);
}

void moveDownStep() {
  actuator.write(downSignal);
  delay(180);
  actuator.write(stopSignal);
}

void setup() {
  Serial.begin(115200);
  Wire.begin();
  actuator.attach(9);

  Serial.println("System Ready (5-step mode)");
}

void loop() {

  bool ok = tflI2C.getData(tfDist, tfAddr);

  if (ok) {

    Serial.print("Distance: ");
    Serial.println(tfDist);

    // ---- Distance Mapping ----
    if (tfDist >= 20) {
      targetStep = 0;   // UP
    }
    else if (tfDist > 13) {
      targetStep = 3;   // MID
    }
    else {
      targetStep = 5;   // DOWN
    }

    // ---- Movement Logic ----
    if (currentStep < targetStep) {
      moveDownStep();
      currentStep++;
    }
    else if (currentStep > targetStep) {
      moveUpStep();
      currentStep--;
    }
  }

  delay(250);  // stability delay
}