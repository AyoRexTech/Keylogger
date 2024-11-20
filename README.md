Keylogger - Educational Ethical Hacking Tool

Overview

This is an open-source keylogger built using Python, designed for educational purposes and ethical 
hacking/pentesting. The tool logs keystrokes to a hidden file and includes features such as email log 
delivery, file size management, and stealth mode.

Features

•	Logs keystrokes and saves them to a hidden directory.
•	Sends logs via email at specified intervals.
•	Automatically manages log file size to avoid excessive storage usage.
•	Simple, lightweight, and easily customizable for pentesting needs.

Ethics and Disclaimer

This tool is intended only for ethical and legal purposes:
•	It is for educational use, such as understanding how keylogging works in ethical hacking and pentesting.

⚠️ Disclaimer:
The author is not responsible for any misuse or illegal activity involving this tool. Use responsibly and in compliance with applicable laws and regulations.

Usage Instructions

1. Clone the Repository:

		git clone https://github.com/yourusername/keylogger.git
		cd keylogger

2. Install Dependencies:
Ensure you have Python installed, then install the required libraries:

		pip install pynput
		pip install smtplib

3.	Run the Keylogger:
Edit the code to include your email credentials for log delivery. Then, execute:

		python keylogger.py


License

This project is licensed under the MIT License, which allows for open-source usage, modification, 
and distribution while ensuring credit is given to the original author. See the LICENSE file for details.


Acknowledgments

This tool was developed as a learning project and is inspired by the principles of ethical hacking 
and cybersecurity.
