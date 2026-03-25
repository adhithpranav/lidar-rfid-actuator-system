import serial
import csv
import os
from datetime import datetime
import time

# -------------------------------
# 🔌 SERIAL CONNECTION
# -------------------------------
ser = serial.Serial('COM11', 9600, timeout=1)

# -------------------------------
# 🚗 VEHICLE DATABASE
# -------------------------------
vehicles = {
    "5586944": "TN 32 AB 2435",
    "f912ab33": "TN 67 BJ 9866",
    "c8aa7721": "TN 67 BG 2356"
}

# -------------------------------
# 📁 CSV SETUP
# -------------------------------
file_name = "attendance.csv"

if not os.path.exists(file_name):
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Vehicle No", "UID", "Date", "Time", "Status"])

# -------------------------------
# 🧾 DISPLAY HEADER
# -------------------------------
print("=" * 50)
print("🚀 RFID TOLL COLLECTION SYSTEM")
print("=" * 50)

# -------------------------------
# 🔁 MAIN LOOP
# -------------------------------
while True:
    try:
        uid = ser.readline().decode().strip().lower()

        if uid:
            now = datetime.now()
            date = now.strftime("%Y-%m-%d")
            time_now = now.strftime("%H:%M:%S")

            # -------------------------------
            # 🔍 CHECK VEHICLE
            # -------------------------------
            if uid in vehicles:
                vehicle_no = vehicles[uid]
                status = "AUTHORIZED"
                alert = "✅ Access Granted"
            else:
                vehicle_no = "UNKNOWN"
                status = "UNAUTHORIZED"
                alert = "🚨 ALERT! Unauthorized Vehicle Detected 🚨"

            # -------------------------------
            # 🖥️ CLEAN OUTPUT DISPLAY
            # -------------------------------
            print("\n" + "-" * 50)
            print(f"📡 UID          : {uid}")
            print(f"🚗 Vehicle No   : {vehicle_no}")
            print(f"📅 Date         : {date}")
            print(f"⏰ Time         : {time_now}")
            print(f"📊 Status       : {status}")
            print("-" * 50)
            print(alert)
            print("-" * 50 + "\n")

            # -------------------------------
            # 💾 SAVE TO CSV
            # -------------------------------
            with open(file_name, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([vehicle_no, uid, date, time_now, status])

            # Delay to avoid duplicate scans
            time.sleep(2)

    except Exception as e:
        print("⚠️ Error:", e)