import board
import busio
from adafruit_pn532.i2c import PN532_I2C

# Connect to PN532
i2c = busio.I2C(board.SCL, board.SDA)
pn532 = PN532_I2C(i2c, debug=False)

print(" Scan a card to clone...")

key = b"\xFF\xFF\xFF\xFF\xFF\xFF"  # Default MIFARE key
block = 4  # Block to clone

while True:
    uid = pn532.read_passive_target(timeout=0.5)
    if uid:
        print(f" Card detected! UID: {[hex(i) for i in uid]}")
        
        # Read block data
        data = pn532.mifare_classic_read_block(block)
        if data:
            print(f" Read block {block}: {data}")

            # Attempt to write data to a new card
            success = pn532.mifare_classic_write_block(block, data)
            if success:
                print("Congratulations! Data successfully cloned!")
            else:
                print(" Clone failed.")
    time.sleep(1)
