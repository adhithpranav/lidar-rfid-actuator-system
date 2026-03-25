#include <Wire.h>
#include <TFLI2C.h>

TFLI2C tflI2C;

int16_t tfDist;    
int16_t tfAddr = TFL_DEF_ADR;  

void setup() {
  Serial.begin(115200);
  Wire.begin();           // UNO: SDA = A4, SCL = A5
  Serial.println("Starting TF-Luna I2C test...");
}

void loop() {

  bool ok = tflI2C.getData(tfDist, tfAddr);

  if (ok) {
    Serial.print("Distance: ");
    Serial.print(tfDist);
    Serial.print(" cm / ");
    Serial.print(tfDist / 2.54);
    Serial.println(" inches");
  } else {
    Serial.println("getData() FAILED (no reply on I2C)");
    // If your TFLI2C lib has it:
    // tflI2C.printStatus();
  }

  delay(100);
}
