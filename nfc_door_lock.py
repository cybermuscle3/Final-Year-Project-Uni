import time
import board
import busio
import sqlite3
import RPi.GPIO as GPIO
from adafruit_pn532.i2c import PN532_I2C

# GPIO setup for Relay (Lock Control)
RELAY_PIN = 17  # Use GPIO 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY_PIN, GPIO.OUT)
GPIO.output(RELAY_PIN, GPIO.HIGH)  # Default: lock closed

# Initialize I2C for PN532
i2c = busio.I2C(board.SCL, board.SDA)
pn532 = PN532_I2C(i2c, debug=False)

# Connect to SQLite database
db = sqlite3.connect("nfc_logs.db")
cursor = db.cursor()

def alert_unknown_card(uid_str):
    with open("alerts.log", "a") as f:
        f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Unknown UID: {uid_str}\n")
print(" Scan an NFC card...")

while True:
    uid = pn532.read_passive_target(timeout=0.5)
    if uid:
        uid_str = "-".join([hex(i) for i in uid])
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        print(f" NFC Card Detected! UID: {uid_str}")

        # Check if card is in the database
        cursor.execute("SELECT name FROM scans WHERE uid=?", (uid_str,))
        result = cursor.fetchone()

        if result:
            print(f" Access Granted! Welcome: {result[0]}")
            GPIO.output(RELAY_PIN, GPIO.LOW)  # Unlock
            time.sleep(5)  # Keep lock open for 5 seconds
            GPIO.output(RELAY_PIN, GPIO.HIGH)  # Lock again
            print (" Lock Closed.")
        else:
            print(" Opps!  Access Denied! Unknown Card.")

        # Log scan to database
        cursor.execute("INSERT OR IGNORE INTO scans (uid, name, timestamp) VALUES (?, NULL, ?)", (uid_str, timestamp))
        db.commit()
        print(" Scan logged in the database!")

    time.sleep(1)
