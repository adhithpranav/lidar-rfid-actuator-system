# LiDAR-Based Adjustable RFID System

## 📌 Overview

This project implements a smart system that dynamically adjusts the height of an RFID reader using LiDAR-based distance detection. It is designed to handle vehicles of varying heights (cars, trucks) by positioning the RFID reader appropriately using a servo-driven linear actuator.

---

## 🚀 Features

* LiDAR-based distance sensing
* Step-controlled linear actuator (safe motion)
* Dynamic RFID positioning
* Multi-level detection (no vehicle, car, truck)
* Safe mechanical limits (no over-travel)

---

## 🧠 Working Principle

1. LiDAR measures distance to object
2. Distance is mapped to actuator steps
3. Servo moves actuator step-by-step
4. RFID reader is positioned accordingly

---

## 📏 Calibration Values

* Ground: 22 cm
* Car: 17 cm
* Truck: 10 cm

---

## ⚙️ Hardware Used

* Arduino Uno
* TF-Luna LiDAR (I2C)
* MG995 Servo Motor
* RC522 RFID Reader
* External Battery Pack
* Custom Linear Actuator (3D printed)

---

## 🧩 System Architecture

LiDAR → Arduino → Servo Actuator → RFID Positioning

---

## 📸 Project Images

![Setup](images/setup.jpg)
![Actuator](images/actuator.jpg)

---

## 🛠️ Code Structure

* `lidar_reading/` → LiDAR test code
* `actuator_control/` → Step-based servo control
* `integrated_system/` → Final working system
* `rfid/` → RFID tag reading
* `experimental/` → Advanced actuator logic

---

## ⚠️ Safety Notes

* Always start from home (UP position)
* Use step-based control to avoid gear damage
* Maintain common ground across all components

---

## 🔮 Future Improvements

* Multi-lane detection system
* Automatic homing mechanism
* Database-based RFID identification
* Wireless communication (ESP32)

---

## 👨‍💻 Author

Adhith Pranav
