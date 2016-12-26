# wireless keyboard tester for windows
# windows 10
import Tkinter
import pythoncom
import pyHook
import time

class WKB_Tester(Tkinter.Tk):
    def __init__(self, parent):
        Tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        self.count = 0

        self.title_image_src = Tkinter.PhotoImage(file="title.gif")

        self.title_image = Tkinter.Label(self, image=self.title_image_src, bd=0)
        self.title_image.grid(row=0, column=0, columnspan=3, padx=20, pady=14)

        self.num_of_keystrokes_label = Tkinter.Label(self, text="Number of Keystrokes: ", bg="#ffffff", font=("Helvetica", 12))
        self.num_of_keystrokes_label.grid(row=1, column=0, padx=20, sticky=Tkinter.W)

        self.num_of_keystrokes_var = Tkinter.StringVar()
        self.num_of_keystrokes = Tkinter.Label(self, textvariable=self.num_of_keystrokes_var, bg="#ffffff", font=("Helvetica", 12))
        self.num_of_keystrokes.grid(row=1, column=2, columnspan=2, padx=20)

        self.start_label = Tkinter.Label(self, text="Start date and time: ", bg="#ffffff", font=("Helvetica", 12))
        self.start_label.grid(row=2, column=0, padx=20, sticky=Tkinter.W)

        self.start_time_var = Tkinter.StringVar()
        self.start_time = Tkinter.Label(self, textvariable=self.start_time_var, bg="#ffffff", font=("Helvetica", 12))
        self.start_time.grid(row=2, column=1, columnspan=2, padx=20)

        self.last_keystroke_label = Tkinter.Label(self, text="Last keystroke date and time:", bg="#ffffff", font=("Helvetica", 12))
        self.last_keystroke_label.grid(row=3, column=0, padx=20, sticky=Tkinter.W)

        self.grid_rowconfigure(4, pad=15)

        self.start_button = Tkinter.Button(self, text="Start", bg="lightgreen", command=self.start_counting, width=15)
        self.start_button.grid(row=4, column=1)

        self.stop_button = Tkinter.Button(self, text="Stop", command=self.stop_counting, width=15)
        self.stop_button.grid(row=4, column=2, padx=10)

    def on_keyboard_event(self, event):
        print event.Key
        #print key_pressed.Ascii

        def counter(self):
            self.count += 1
            print self.count
            # *****  this function causes the program to lock up *****
            self.num_of_keystrokes_var.set(str(self.count))

        counter(self)

        return True

    # this works if I just remove the hookmanager stuff and call this function
    def my_kb_event_test(self):
        def counter(self):
            self.count += 1

        counter(self)
        self.num_of_keystrokes_var.set(str(self.count))

    def start_counting(self):
        print "Starting counting..."
        self.start_time_var.set(time.strftime("%b %d %Y %H:%M:%S", time.localtime()))
        self.hookmanager = pyHook.HookManager()
        self.hookmanager.KeyDown = self.on_keyboard_event
        self.hookmanager.HookKeyboard()

    def stop_counting(self):
        print "Stopping counting..."
        self.hookmanager.UnhookKeyboard()

if __name__ == "__main__":
    top = WKB_Tester(None)
    top.title("Wireless Keyboard Battery Tester")
    top.wm_iconbitmap("favicon.ico")
    top.configure(background="#ffffff")

    top.mainloop()
