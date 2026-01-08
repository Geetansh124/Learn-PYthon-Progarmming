import pyautogui
import pyperclip
import time

# Give you time to switch to the correct window
time.sleep(3)

# 1️⃣ Click on the icon
pyautogui.click(1039, 1060)
time.sleep(0.5)

# 2️⃣ Drag to select text
pyautogui.moveTo(763, 147)
pyautogui.dragTo(1867, 905, duration=0.5, button='left')
time.sleep(0.3)

# 3️⃣ Copy selected text (Ctrl + C)
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.3)

# 4️⃣ Get text from clipboard into a variable
copied_text = pyperclip.paste()

print("Copied Text:")
print(copied_text)
