# LINUX VERSION
# Counts the total number of keystrokes 
# Designed to compare battery performance wireless keyboards for Batteroo / Batteriser
# Just a quick implementation of pyxhook
# Most of this code is from the example file https://github.com/JeffHoogland/pyxhook
# Requires pyxhook module 
# Visit GitHub https://github.com/JeffHoogland/pyxhook
# Just Download the raw pyxhook.py file and put it in the same folder as this script
# and run this script with python 
# Press Esc at any time to Quit and show the count - remember Esc counts as a key! 

import pyxhook
import time

def keystroke_pressed(key_pressed):
    # uncomment below to see the key pressed
    #print key_pressed
    counter()

    # press 'Esc' key to quit
    if key_pressed.Ascii == 27:
        global running
        running = False

def counter():
    counter.count += 1

hookmanager = pyxhook.HookManager()

hookmanager.KeyDown = keystroke_pressed

hookmanager.HookKeyboard()

hookmanager.start()

# start counter at 0
# note pressing the escape key counts as a key!
counter.count = 0

running = True

while running:
    time.sleep(0.1)

hookmanager.cancel()

print "\n"
print "-------------------------------------"
print "Keys have been pressed " + str(counter.count) + " times"
print "-------------------------------------"
