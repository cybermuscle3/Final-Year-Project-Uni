#provides pin definitions for Raspberry Pi
import board
#Handles SPi and I2C communication
import busio
import time
#interfacing with the PN532 NFC module over SPI
from adafruit_pn532.i2c import PN532_I2C

print('Using I2C mode - Checking connections ...')
# Set up SPI connection

i2c = busio.I2C(board.SCL, board.SDA)

# Initialize PN532 NFC module
pn532 = PN532_I2C(i2c, debug=False)

# Check and print firmware version
try:
    ic, ver, rev, support = pn532.firmware_version
    print('Success! Found PN532 NFC module (Firmware version: {ver}.{rev}')
except Exception as e:
    print('Sorry, PN532 NFC module not detected - {e}.Check your writing, I2C settings and DIP switch positions (PIN1: ON, PIN2: OFF).')
    exit()

# Configure PN532 for reading cards
pn532.SAM_configuration()

print(' Waiting for NFC card...')
while True:
    uid = pn532.read_passive_target(timeout=0.5)
    if uid is not None:
        print('Success! NFC card detected! UID: ', [hex(i) for i in uid])
    time.sleep(1)

