# wireless keyboard tester for windows
# windows 10
import pythoncom
import pyHook

def keystroke_pressed(key_pressed):
    # uncomment to see key pressed
    print key_pressed.Key
    print key_pressed.Ascii
    counter()

    # press 'Esc' key to quit
    if key_pressed.Ascii == 27:
        global running
        running = False

def counter():
    counter.count += 1

hookmanager = pyHook.HookManager()

hookmanager.KeyDown = keystroke_pressed

hookmanager.HookKeyboard()

# start counter at 0
# note pressing Esc counts as a key!
counter.count = 0

running = True

while running:
    pythoncom.PumpWaitingMessages()
else:
    hookmanager.UnhookKeyboard()

print "\n"
print "-------------------------"
print "Key have been pressed " + str(counter.count) + " times"
print "-------------------------"
