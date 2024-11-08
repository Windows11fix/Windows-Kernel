Ntkrnlpa.exe Scanner
This project provides a simple GUI-based tool to scan and verify the integrity of the Ntkrnlpa.exe file on Windows systems. Ntkrnlpa.exe is an essential Windows kernel file, and this tool checks its existence, calculates its hash, and verifies file attributes to detect potential corruption or tampering.

Features
Checks if Ntkrnlpa.exe exists in the System32 directory.
Calculates the SHA-256 hash of Ntkrnlpa.exe to verify integrity.
Compares the hash to a known good hash if available.
Displays file size, last modification date, and admin status.
Simple GUI interface for easy use.
Prerequisites
Python 3.x (if running from source)
Tkinter (Python’s standard GUI library; usually included with Python)
PyInstaller (for building the .exe file)
Installation
Clone the repository:


git clone https://github.com/yourusername/ntkrnlpa-scanner.git
cd ntkrnlpa-scanner
Install required packages (if running from source):


pip install -r requirements.txt
Replace the placeholder "YOUR_KNOWN_GOOD_HASH_HERE" in the code with a known good SHA-256 hash of Ntkrnlpa.exe for better verification.

Usage
Running from Source
Open a terminal or command prompt.
Navigate to the project directory.
Run the script:


python ntkrnlpa_scanner.py
Building the Executable
To create a standalone .exe file, follow these steps:

Install PyInstaller:


pip install pyinstaller
Use PyInstaller to package the script:


pyinstaller --onefile --windowed ntkrnlpa_scanner.py
--onefile: Packages everything into a single .exe file.
--windowed: Suppresses the console window for a cleaner GUI experience.
The .exe file will be created in the dist folder.

Running the Executable
Double-click the .exe file generated in the dist folder to open the Ntkrnlpa.exe Scanner GUI.

Screenshots

How It Works
File Existence Check: Verifies if Ntkrnlpa.exe is in the C:\Windows\System32\ directory.
Hash Calculation: Computes the SHA-256 hash of Ntkrnlpa.exe and displays it.
Hash Comparison: (Optional) Compares the hash with a known good hash, if provided.
File Attributes: Displays file size, last modification date, and admin privileges status.
Troubleshooting
Admin Privileges: For full functionality, run the executable as an administrator.
Missing Tkinter: Tkinter should be installed with Python by default, but if missing, you can install it via:
bash
Copy code
sudo apt-get install python3-tk  # For Linux
License
This project is licensed under the MIT License. See LICENSE for more details.

Disclaimer
This tool is intended for informational and educational purposes only. Always verify the integrity of essential system files from trusted sources and ensure you have reliable backups.
