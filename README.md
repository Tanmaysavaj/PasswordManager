# 🛡️ Password Manager

A simple and secure **Password Manager** built with **Python** and **Tkinter**.  
This tool allows you to generate strong passwords, save them securely to a file, and copy them to your clipboard for easy use.

---

## 📌 Features

- **Random Password Generator** – Generates strong passwords with letters, numbers, and symbols.
- **Clipboard Copy** – Automatically copies the generated password to your clipboard.
- **Data Storage** – Saves your credentials (Website, Email/Username, and Password) into a `data.txt` file.
- **User-Friendly Interface** – Simple Tkinter GUI for easy usage.
- **Confirmation Dialogs** – Ensures you confirm before saving any password.

---

## 🖥️ How It Works

1. Enter the **website name**.
2. Enter your **email or username** (pre-filled with your default email).
3. Either type your own password or click **"Generate Password"** to create a strong one automatically.
4. Click **"Add"** to save the credentials into `data.txt`.

---

## 📂 Project Structure

```
password-manager-start/
│
├── data.txt        # Stores saved credentials
├── logo.png        # App logo for the Tkinter window
├── main.py         # Main Python application
└── README.md       # Project documentation
```

---

## 🚀 Getting Started

### **Requirements**
- Python 3.x
- `tkinter` (comes pre-installed with Python)
- `pyperclip` (for clipboard copy)

### **Install dependencies**
```bash
pip install pyperclip
```

### **Run the application**
```bash
python main.py
```



## ✨ Author
**Tanmay Savaj**
