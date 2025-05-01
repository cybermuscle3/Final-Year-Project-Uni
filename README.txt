 SmartPiPentest: NFC Penetration Testing Toolkit with Raspberry Pi
 
Overview
SmartPiPentest is a practical security testing toolkit that turns a Raspberry Pi into a low-cost NFC pentesting device.  
It allows you to **read**, **write**, **clone**, and **log** NFC card data using a **PN532 reader**, and also control a **physical door lock** for access control simulations.

This project demonstrates how affordable hardware can be used for ethical hacking, red teaming, and educational purposes within legal boundaries.

Features:
-  Web-based NFC control panel (`Flask`)
-  UID reading and logging
-  Write test data to card memory (block 4)
-  Clone card data from one to another
-  Dump full card contents to file
-  Control a door lock relay (GPIO)
-  SQLite logging for all access events
-  Unknown card alert system (log)
-  Unit testing (`unittest`)


Requirements
Install required Python libraries:

pip install -r requirements.txt

Disclaimer
This tool is built strictly for ethical hacking and academic purposes.
All testing must be conducted in controlled environments with full permission from system owners.
