# LINUX VERSION
# Counts the total number of keystrokes 
# Designed to compare battery performance wireless keyboards for Batteroo / Batteriser
# Just a quick implementation of pyxhook
# Most of this code is from the example file https://github.com/JeffHoogland/pyxhook
# Requires pyxhook module 
# Visit GitHub https://github.com/JeffHoogland/pyxhook
# Just Download the raw pyxhook.py file and put it in the same folder as this script
# and run this script with python 
# Press Space Bar to get a progress update, it won't count the Space Bar as a keystroke
# Press Esc at any time to Quit, it won't count the Esc as a keystroke


import pyxhook
import time

start_time = 0
last_keystroke_time = 0

def on_keyboard_event(event):
    #print event
    global last_keystroke_time
    # print report 'Space Bar' - 
    if event.Ascii == 32:
        global start_time
        print_report(start_time, last_keystroke_time)
    # press 'Esc' key to quit
    elif event.Ascii == 27:
        global running
        running = False
    else: 
        # do these LAST
        last_keystroke_time = time.localtime()
        counter()


def counter():
    counter.count += 1

def print_report(start_time, last_keystroke_time):
    print "\n"
    print "-------------------------------------"
    print "Start time: " + time.strftime("%b %d %Y %H:%M:%S", start_time)
    print "-------------------------------------"
    print "Keys have been pressed " + str(counter.count) + " times"
    print "-------------------------------------"
    print "Last keystroke: " + time.strftime("%b %d %Y %H:%M:%S", last_keystroke_time)
    print "-------------------------------------"
    print "\n"

hookmanager = pyxhook.HookManager()
hookmanager.KeyDown = on_keyboard_event
hookmanager.HookKeyboard()
hookmanager.start()

# note pressing the escape key counts as a key!
counter.count = 0

start_time = time.localtime()

running = True

while running:
    time.sleep(0.1)

hookmanager.cancel()

print_report(start_time, last_keystroke_time)
