# 📦 Requirements

## 🔧 Hardware Components

* Arduino Uno (2 units)
* TF-Luna LiDAR Sensor (I2C)
* MG995 Servo Motor (continuous rotation)
* RC522 RFID Reader Module
* RFID Tags / Cards
* External Battery Pack (5–6V for servo)
* Breadboard
* Jumper Wires (Male-Male, Male-Female)
* Wooden Base Board / Frame Structure
* 3D Printed Linear Actuator (Gear + Rack system)

---

## 💻 Software Requirements

* Arduino IDE
* Python 3.x (for RFID database matching, optional)

---

## 📚 Arduino Libraries

Install the following libraries via Arduino IDE:

* Servo.h (built-in)
* Wire.h (built-in)
* TFLI2C (for TF-Luna LiDAR)
* MFRC522 (for RFID module)

---

## 🔌 System Requirements

* USB connection for Arduino programming
* Serial Monitor (115200 baud rate)
* External power supply for servo motor

---

## ⚠️ Important Notes

* Ensure common ground between Arduino and external battery
* Do NOT power servo directly from Arduino 5V pin
* RFID module must be powered using 3.3V
* Start system with actuator in home (UP) position
