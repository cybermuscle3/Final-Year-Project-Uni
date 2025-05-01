#!/bin/bash

echo "[1] Hello World"
echo "[2] Reverse Shell"
read -p "Select a payload: " choice

case "$choice" in
  1) payload="hello.txt" ;;
  2) payload="reverse_shell.txt" ;;
  *) echo "Invalid"; exit 1 ;;
esac

PAYLOAD="/home/kali/badusb/payloads/$payload"

while IFS= read -r line; do
  echo "$line" | sudo tee /dev/hidg0
  sleep 0.2
done < "$PAYLOAD"
