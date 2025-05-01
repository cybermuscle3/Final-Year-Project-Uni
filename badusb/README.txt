Advanced BadUSB Attack Scenarios – Final Year Cybersecurity Project

This project explores advanced USB-based attack techniques using a Raspberry Pi Zero W emulating a Human Interface Device (HID). The goal is to simulate real-world penetration testing tactics in a controlled, ethical environment using physical access vectors.


Objective

To create an extensible BadUSB framework that can:
- Inject HID-based PowerShell payloads
- Perform reverse shells, keylogging, credential harvesting
- Extract saved browser credentials
- Maintain persistence on target machines
- Exfiltrate data silently over Wi-Fi

Folder Structure

badusb_project/
├── launcher/
│   └── auto_payload.sh               # Main HID launcher script
├── payloads/                         # HID-based text payloads
│   ├── keylogger_payload.txt
│   ├── fake_login_payload.txt
│   └── reverse_shell_payload.txt
├── scripts/                          # PowerShell payloads fetched by victim
│   ├── keylogger.ps1
│   ├── fake_prompt.ps1
│   ├── payload.ps1                   # Reverse shell
│   └── persist.ps1
├── server/                           # Python servers for data collection
│   ├── receiver.py                   # For pass.json
│   ├── fake_receiver.py              # For creds.txt
│   └── keylog_receiver.py            # For klog.txt
├── data/                             # Received logs and output
│   ├── received_pass.json
│   ├── received_creds.txt
│   └── received_klog.txt
├── tools/                            # Local analysis tools
│   └── dashboard.py                  # Viewer for received data
└── README.md                         # Project summary & documentation


Implemented Attack Scenarios

1. Stealth Reverse Shell
- PowerShell payload triggered via HID
- Creates a reverse shell to attacker's Netcat listener
- Hidden execution with `-w hidden -nop`
- Optional: persistence using Task Scheduler

2. Wireless Keylogger
- PowerShell keylogger using WinAPI
- Logs to `klog.txt`, exfiltrates on stop
- Controlled manually, auto-runs via `persist.ps1`

3. Credential Harvesting (Fake Login Prompt)
- PowerShell GUI (XAML) mimicking Windows Update
- Captures username and password
- Sends credentials to attacker's Pi via HTTP POST

4. Saved Password Extraction
- Uses LaZagne via PowerShell
- Extracts credentials from Chrome, Firefox, Edge
- Sends results (`pass.json`) back to Pi silently

5. Persistence
- `persist.ps1` creates hidden scheduled task
- Launches any PowerShell script at login
- Used for reverse shell, keylogger, etc.

Monitoring Tools

 - `dashboard.py`
 - Menu-based viewer (terminal) for:
 - LaZagne pass.json
 - Keylogger logs
 - Phished credentials
 - Clean exit using `Ctrl+C` (KeyboardInterrupt handled)

 Tools Used

- Raspberry Pi Zero W – HID emulation via `/dev/hidg0`
- PowerShell– payload scripting, stealth execution
- Python (http.server)– hosting scripts
- Python POST servers – for receiving data
- Netcat– for reverse shell listener
- LaZagne – password extraction

Ethical Disclaimer

 This project is intended **only for educational and ethical penetration testing** in fully authorized environments.  
 It demonstrates how easily USB-based attacks can occur with physical access and aims to raise awareness.  
 **Do not use this code on unauthorized systems. You are responsible for your actions.**
