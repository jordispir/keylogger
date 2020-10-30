from pynput import keyboard
import os, sys

key_pressed = keyboard.Key

def on_release(key):
    print (key)

    if key == key_pressed.esc:
        sys.exit(0)

    txt = open("words.txt", "a")
    txt.write(str(key).replace("'", " "))
    txt.close()

# Collect events until released
with keyboard.Listener(on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(on_release=on_release)
listener.start()
