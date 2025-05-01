#!/bin/bash

# Folder with all payloads
PAYLOAD_DIR="/home/kali/badusb/payloads"

# Find all .txt payloads
mapfile -t PAYLOADS < <(find "$PAYLOAD_DIR" -type f -name "*.txt")

# Pick one at random
RANDOM_INDEX=$(( RANDOM % ${#PAYLOADS[@]} ))
SELECTED="/home/pi/badusb/payloads/fake_login_payload.txt"

echo "[INFO] Selected payload: $SELECTED"

# Send it to /dev/hidg0
while IFS= read -r line; do
  echo "$line" > /dev/hidg0
  sleep 0.2
done < "$SELECTED"
