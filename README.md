# Screenshot Tool 📸

**Completed:** September 13, 2025

A lightweight Python utility that automatically captures a screenshot of the computer screen, saves it as a PNG image with a timestamp, and displays a Windows notification confirming where the screenshot was saved.

I developed this project to explore Python automation, file management, image processing, and Windows desktop notifications.

## Features

- **Automatic screenshot capture:** Takes a screenshot immediately when the program runs.
- **Timestamped filenames:** Names screenshots using the current date and time.
- **Automatic folder creation:** Creates a dedicated folder for storing screenshots if it doesn't already exist.
- **Portable file paths:** Uses the current user's home directory instead of hardcoded Windows paths.
- **Windows notifications:** Displays a notification confirming where the screenshot was saved.
- **Custom notification icon:** Generates a temporary icon from the captured screenshot.
- **Automatic cleanup:** Removes the temporary icon after the notification finishes.

## Requirements

- Python 3
- Windows 10 or Windows 11
- `pyautogui`
- `Pillow`
- `win10toast-click`

The program also uses Python's built-in `datetime`, `pathlib`, `os`, and `time` modules.

## Installation

1. Download `ScreenShot.py` from this repository.
2. Make sure Python 3 is installed.
3. Install the required libraries:

   ```bash
   pip install pyautogui pillow win10toast-click
   ```

4. Open a terminal in the directory containing `ScreenShot.py`.
5. Run the program:

   ```bash
   python ScreenShot.py
   ```

The program automatically captures a screenshot when executed.

## How to Use

The application requires no additional user input.

Once launched, it performs the following actions:

1. Creates the screenshot directory if necessary.
2. Captures the current screen.
3. Generates a filename using the current date and time.
4. Saves the screenshot as a PNG image.
5. Creates a temporary icon from the captured screenshot.
6. Displays a Windows notification showing the screenshot folder.
7. Waits for the notification to finish, removes the temporary icon, and exits.

### Screenshot Storage

Screenshots are automatically saved in:

```text
Pictures/Python-ScreenShot/
```

The program uses `Path.home()` to locate the current user's home directory.

This allows it to work with different Windows accounts without manually changing the file paths.

### File Naming

Each screenshot receives a timestamped filename using the following format:

```text
Posnetek zaslona YYYY-MM-DD HHMMSS.png
```

**Example:**

```text
Posnetek zaslona 2025-09-13 143025.png
```

This format makes screenshots easier to organize chronologically.

### Windows Notification

After capturing the screenshot, the program displays a Windows notification.

**Notification title:**

`Screenshot`

**Notification message:**

`Saved in: [Screenshot folder]`

The notification uses a small icon generated from the captured screenshot and is configured with a two-second duration.

## How It Works

### 1. Folder Management

The program uses Python's `pathlib` module to determine where screenshots should be stored.

```python
folder_path = Path.home() / "Pictures" / "Python-ScreenShot"
folder_path.mkdir(parents=True, exist_ok=True)
```

If the folder doesn't exist, Python automatically creates it.

### 2. Timestamp Generation

The `datetime` module generates a timestamp for the screenshot filename.

```python
name = datetime.now().strftime("%Y-%m-%d %H%M%S")
```

This helps distinguish screenshots taken at different times.

### 3. Screenshot Capture

The `pyautogui` library captures the screen and saves it as a PNG image.

```python
screenshot = pyautogui.screenshot()
screenshot.save(image)
```

### 4. Icon Generation

The `Pillow` library opens the screenshot, converts it to RGB, and generates a temporary ICO file.

```python
img_showing = Image.open(png_path).convert("RGB")
img_showing.save(ico_path, format="ICO", sizes=[(32, 32)])
```

The temporary icon is used for the Windows notification.

### 5. Notification System

The application uses `win10toast-click` to display a notification.

```python
toaster.show_toast(
    "Screenshot",
    f"Saved in: {folder_path}",
    duration=2,
    threaded=False,
    icon_path=str(ico_path)
)
```

Setting `threaded=False` makes the program wait until the notification finishes before continuing.

This is useful because the temporary icon is deleted afterward.

### 6. Temporary File Cleanup

After the notification finishes, the application removes the temporary icon:

```python
os.remove(ico_path)
```

The original PNG screenshot remains saved in the screenshot directory.

## Known Limitations

- **Windows-focused:** The notification functionality is designed for Windows.
- **Single screenshot:** Each execution captures only one screenshot.
- **No built-in keyboard shortcut:** The script must be launched manually or through an externally configured shortcut.
- **Full-screen capture:** Users cannot select a specific screen region.
- **Filename collisions:** Screenshots captured within the same second may receive identical filenames.
- **Notification compatibility:** Notifications depend on Windows settings and compatibility with the installed libraries.
- **Temporary icon cleanup:** Deleting the icon may fail if another process still has the file open.

## Development Note

This project was created as a personal Python programming exercise focused on desktop automation and working with external libraries.

It demonstrates file handling, timestamp generation, screenshot capture, image conversion, Windows notifications, and temporary file management.


**Author:** [Nik Berginc](https://github.com/nikberginc)
