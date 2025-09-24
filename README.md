# 📱 QR Code Generator (Tkinter + pyqrcode)

A simple desktop application built with Python and Tkinter that generates QR codes from user-provided links. The app uses the `pyqrcode` and `Pillow` libraries to create and display QR codes in real time.

---

## 🚀 Features

- 🔗 Input any URL or text to generate a QR code
- 🖼️ Automatically saves the QR code as a `.png` file
- 👁️ Displays the generated QR code within the app
- 🎨 Clean and intuitive Tkinter interface

---

## 🛠️ Installation

### Requirements

- Python 3.10+
- Required libraries:
  - `tkinter` (built-in)
  - `pyqrcode`
  - `Pillow`

Install dependencies via pip:

```bash
pip install pyqrcode pillow
```

📦 Usage
1. Clone or download the project.
2. Run the script:
python qr_generator.py

3. Enter a Link Name (used as filename).
4. Enter the Link or text to encode.
5. Click Generate QR Code.
6. The QR code will be saved as <LinkName>.png and displayed in the app.

📁 Project Structure
QR_Code_Generator/

```bash
├── qr_code.py
├── README.md
├── PhilipsTech.png
```

🧠 Notes
QR codes are saved in the same directory as the script.
The app uses a fixed canvas size (400x600) and places widgets using create_window.
You can modify the scale parameter in url.png(file_name, scale=8) to adjust image resolution.

👤 Author
Tabong Python Developer | GUI Designer
 📍 Kumba, Cameroon


📜 License
This project is open-source and free to use for educational and personal purposes.
