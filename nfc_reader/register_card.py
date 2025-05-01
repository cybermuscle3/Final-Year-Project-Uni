import sqlite3
import time
import board
import busio
from adafruit_pn532.i2c import PN532_I2C

# Initialize I2C connection to PN532
i2c = busio.I2C(board.SCL, board.SDA)
pn532 = PN532_I2C(i2c, debug=False)

# Connect to SQLite database
db = sqlite3.connect("nfc_logs.db")
cursor = db.cursor()

print(" Scan a new NFC card to register...")

while True:
    uid = pn532.read_passive_target(timeout=0.5)
    if uid:
        uid_str = "-".join([hex(i) for i in uid])
        print(f"Detected NFC Card! UID: {uid_str}")

        # Check if card is already in the database
        cursor.execute("SELECT name FROM scans WHERE uid=?", (uid_str,))
        result = cursor.fetchone()

        if result:
            print(f"ℹ️ Card already registered as: {result[0]}")
        else:
            name = input("🔹 Enter the user name for this card: ")
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute("INSERT INTO scans (uid, name, timestamp) VALUES (?, ?, ?)", (uid_str, name, timestamp))
            db.commit()
            print("Success! Card added to the database!")

    time.sleep(1)
