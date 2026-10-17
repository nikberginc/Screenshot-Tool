import pyautogui
from datetime import datetime
from pathlib import Path
from win10toast_click import ToastNotifier
import os
from PIL import Image
import time


#will get the location of the folder, if it doesnt exist it will create one
folder_path = Path.home() / "Pictures" / "Python-ScreenShot"
folder_path.mkdir(parents=True, exist_ok=True)



#will get the surent time
name = datetime.now().strftime("%Y-%m-%d %H%M%S")
#will add this time and folder path to "image"
image = folder_path / f"Posnetek zaslona {name}.png"


#will sceenshot the screen
screenshot = pyautogui.screenshot()
#it will save the screenshot
screenshot.save(image)


png_path = image
ico_path = folder_path / "screenshot.ico"

img_showing = Image.open(png_path)
# Convert and save as ICO
img_showing = Image.open(png_path).convert("RGB")  # convert to RGB
img_showing.save(ico_path, format='ICO', sizes=[(32,32)])
time.sleep(0.1)


#will add a pop up notivication in where the screenshot was saved
toaster = ToastNotifier()

toaster.show_toast("Screenshot", f"Saved in: {folder_path}", duration=2, threaded=False, icon_path=str(ico_path))

# Delete the file
os.remove(ico_path)