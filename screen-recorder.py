import pyautogui #a package in python used to take screenshots of the entire window
import time
from datetime import datetime

while True:
    # Take a screenshot of the entire screen
    screenshot = pyautogui.screenshot()

    # Generate a file name with the current date and time
    file_name = datetime.now().strftime('screenshot-%Y%m%d-%H%M%S.png')

    # Save the screenshot to a file
    screenshot.save('.//all-things//screen-shots//'+file_name)

    # Pause for 3 seconds
    time.sleep(3)
