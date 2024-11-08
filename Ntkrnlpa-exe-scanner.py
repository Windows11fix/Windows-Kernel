import os
import hashlib
import ctypes
import tkinter as tk
from tkinter import messagebox

def file_exists(filepath):
    """Check if the file exists."""
    return os.path.exists(filepath)

def get_file_hash(filepath):
    """Calculate the SHA-256 hash of the file."""
    sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()

def scan_ntkrnlpa():
    """Scan Ntkrnlpa.exe for existence and verify integrity."""
    filepath = "C:\\Windows\\System32\\ntkrnlpa.exe"
    
    if not file_exists(filepath):
        messagebox.showerror("Error", "Ntkrnlpa.exe not found.")
        return

    # Step 1: Verify file existence
    result_text.set("Ntkrnlpa.exe found. Verifying file...")

    # Step 2: Hashing the file to check integrity
    file_hash = get_file_hash(filepath)
    result_text.set(f"File hash (SHA-256): {file_hash}")

    # Optional: Compare with known good hash (replace with a real hash if known)
    known_good_hash = "YOUR_KNOWN_GOOD_HASH_HERE"  # Replace this with the real hash for verification
    if file_hash == known_good_hash:
        result_text.set("Ntkrnlpa.exe file hash is valid.")
    else:
        result_text.set("Warning: File hash does not match. The file may be corrupted or tampered with.")

    # Step 3: Check file attributes for suspicious modifications
    file_attrs = os.stat(filepath)
    attributes_info = (
        f"File size: {file_attrs.st_size} bytes\n"
        f"Last modified: {file_attrs.st_mtime}"
    )
    result_text.set(result_text.get() + "\n" + attributes_info)

    # Step 4: Check for admin privileges
    if ctypes.windll.shell32.IsUserAnAdmin():
        result_text.set(result_text.get() + "\nRunning with admin privileges.")
    else:
        result_text.set(result_text.get() + "\nNot running as admin. Some checks may be limited.")

# GUI Setup
root = tk.Tk()
root.title("Ntkrnlpa.exe Scanner")
root.geometry("500x300")

result_text = tk.StringVar()
result_text.set("Click 'Scan' to start.")

# Layout
frame = tk.Frame(root)
frame.pack(pady=20)

scan_button = tk.Button(frame, text="Scan Ntkrnlpa.exe", command=scan_ntkrnlpa)
scan_button.pack()

result_label = tk.Label(root, textvariable=result_text, wraplength=450, justify="left")
result_label.pack(pady=20)

# Run the GUI
root.mainloop()
