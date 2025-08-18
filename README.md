🛡️ Password Manager

A simple and secure Password Manager built with Python and Tkinter.
This tool allows you to generate strong passwords, save them securely to a file, search for saved passwords, and copy them to your clipboard for easy use.

📌 Features

Random Password Generator – Generates strong passwords with letters, numbers, and symbols.

Clipboard Copy – Automatically copies the generated password to your clipboard.

Data Storage – Saves your credentials (Website, Email/Username, and Password) into a data.json file.

Search Functionality – Quickly find saved credentials by website name.

User-Friendly Interface – Simple Tkinter GUI for easy usage.

Exception Handling – Gracefully handles missing or corrupt data files, and empty input fields.

Confirmation Dialogs – Ensures you confirm before saving any password.

🖥️ How It Works

Enter the website name.

Enter your email or username (pre-filled with your default email).

Either type your own password or click "Generate Password" to create a strong one automatically.

Click "Add" to save the credentials into data.json.

To retrieve saved credentials, enter a website name and click "Search".

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
