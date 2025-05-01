import board
import busio
from adafruit_pn532.i2c import PN532_I2C
import time

# Constants
DEFAULT_KEY = b"\xFF\xFF\xFF\xFF\xFF\xFF"
BLOCK = 4  # Default block to read/write/clone

# Set up I2C and PN532
i2c = busio.I2C(board.SCL, board.SDA)
pn532 = PN532_I2C(i2c, debug=False)

def read_card():
    uid = pn532.read_passive_target(timeout=0.5)
    if uid:
        uid_str = "-".join([hex(i) for i in uid])
        print(f"UID: {uid_str}")
        return uid_str
    return None

def write_card():
    print("Waiting for card to write to...")
    uid = pn532.read_passive_target(timeout=5)
    if uid:
        print(f"Card detected. Writing to block {BLOCK}")
        if pn532.mifare_classic_authenticate_block(uid, BLOCK, PN532_I2C.MIFARE_CMD_AUTH_A, DEFAULT_KEY):
            data = bytearray("HelloWorld123456", 'utf-8')[:16]  # Must be 16 bytes
            result = pn532.mifare_classic_write_block(BLOCK, data)
            print("Write successful!" if result else "Write failed.")
            return result
        else:
            print("Authentication failed!")
    return False

def clone_card():
    print("Scan source card...")
    src_uid = pn532.read_passive_target(timeout=5)
    if src_uid is None:
        print("No source card detected.")
        return False

    if not pn532.mifare_classic_authenticate_block(src_uid, BLOCK, PN532_I2C.MIFARE_CMD_AUTH_A, DEFAULT_KEY):
        print("Source card authentication failed.")
        return False

    data = pn532.mifare_classic_read_block(BLOCK)
    if not data:
        print("Failed to read block.")
        return False

    print(f"Cloning block {BLOCK} data: {data}")

    print("Scan target card...")
    tgt_uid = pn532.read_passive_target(timeout=5)
    if tgt_uid is None:
        print("No target card detected.")
        return False

    if not pn532.mifare_classic_authenticate_block(tgt_uid, BLOCK, PN532_I2C.MIFARE_CMD_AUTH_A, DEFAULT_KEY):
        print("Target card authentication failed.")
        return False

    result = pn532.mifare_classic_write_block(BLOCK, data)
    print("Cloning successful!" if result else "Clone failed.")
    return result

def dump_all_blocks():
    uid = pn532.read_passive_target(timeout=5)
    if not uid:
        print("No card detected.")
        return False

    uid_str = "-".join([hex(i) for i in uid])
    print(f"Dumping all readable blocks for UID: {uid_str}")

    with open("card_dump.txt", "w") as f:
        f.write(f"UID: {uid_str}\n")
        for block in range(1, 64):  # avoid block 0 (contains UID and is read-only)
            try:
                if pn532.mifare_classic_authenticate_block(uid, block, PN532_I2C.MIFARE_CMD_AUTH_A, DEFAULT_KEY):
                    data = pn532.mifare_classic_read_block(block)
                    f.write(f"Block {block}: {data}\n")
                else:
                    f.write(f"Block {block}: AUTH FAILED\n")
            except Exception as e:
                f.write(f"Block {block}: ERROR - {e}\n")

    print("Dump complete! Check card_dump.txt")
    return True

