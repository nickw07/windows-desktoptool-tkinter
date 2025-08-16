# Windows Desktop Tool (Python & Tkinter)

An Application made with Python and Tkinter

It allows you to:
- View current time and date
- Read out system information
- Access common windows programs
- Launch three built-in applications (e.g. Calculator and password generator)

---

## 🖼️ | Preview

![Project Demo](graphics/github-preview-files/desktoptool-preview.gif)
![Application modes](graphics/github-preview-files/desktoptool-modes-preview.png)

---

## 🧠 | Concepts used
- Object-oriented design: Each UI frame is a class
- Frame switching mechanism
- Use of `Toplevel` windows for modular sub-apps
- Modular structure with reusable styles and themes

---

## 🛠️ | Technologies & Libraries

- `tkinter` – GUI framework
- `psutil` – System information
- `wmi` – Access Windows system details
- `pyautogui` – Interaction automation
- `Pillow` – Image handling
- `pyperclip` – Clipboard access

---

## 📁 | Project Structure

- `applications/` - Calculator, Password generator, Styles for these apps
- `graphics/` - Icons and UI-Images
- `root_ui/` - All UI frames
- `requirements.txt` - Python dependencies
- `ATTRIBUTION.md` - Icon sources
- `main_app.py` - Main window logic
- `main_styles.py` - Styling for main window
- `theme_manager.py` - Appearance mode management
- `start.py` - Initializing file

---

## 🧑‍⚖️ | Credits

- This project uses icons from [Flaticon](https://www.flaticon.com) - For detailed attributions, see [ATTRIBUTION.md](./ATTRIBUTION.md)
- The file [`graphics/system-frame/laptop-image.png`](./graphics/system-frame/laptop-image.png) is a placeholder laptop image and is only included for demonstration purposes due to copyright reasons
- The GIF was made using [ezgif](https://ezgif.com/maker)

---

## 🚀 | Installation

1. Clone the repository
```
git clone https://github.com/nickw07/windows-desktoptool-tkinter.git
cd windows-desktoptool-tkinter
```

2. Recommended: Create a virtual environment and activate it *(Example shows activation in CMD)*
```
python -m venv .venv
```
```
.venv\Scripts\activate.bat
```

3. Install required packages
```
pip install -r requirements.txt
```

4. Run the application (`start.py` in the project folder)
```
python start.py
```

---

## 📒 | Notes

- The application was developed using Python 3.12 and PyCharm
- It is designed specifically for Windows systems

---

## 🐛 | Bugs
- Feel free to report any bugs
- Widgets in the GUI may shift slightly depending on the environment (likely due to the `place` layout manager).
- ⚠️ There are currently known issues with the calculator top-level window. Problems will be fixed in a future update.