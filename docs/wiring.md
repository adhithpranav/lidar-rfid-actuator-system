# 🔌 Wiring Connections

## 🔧 Servo Motor (MG995)
- Red → External Battery (+)
- Brown → GND (Common Ground)
- Yellow → Arduino D9

---

## 📡 LiDAR Sensor to Arduino1 (TF-Luna I2C)
- Pin 1 → Arduino 5V
- Pin 2 → Arduino SDA
- Pin 3 → Arduino SCL
- Pin 4 → GND
- Pin 5 → GND
- Pin 6 → Disconnected

---

## 🏷️ RFID Reader (MFRC522) to Arduino2
- VCC → 3.3V
- GND → GND
- RST → D9
- SDA → D10
- MOSI → D11
- MISO → D12
- SCK → D13
- IRQ → Not connected

---
## ⚡ Power Connections
- Arduino powered via USB
- Servo powered via external battery
- All grounds are connected together (common ground)

---

## ⚠️ Notes
- Do NOT connect RFID to 5V (use 3.3V only)
- Ensure common ground between Arduino and battery
- Servo should NOT be powered from Arduino 5V