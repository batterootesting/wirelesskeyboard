# wireless keyboard battery tester for windows
# windows 10
import Tkinter
import tkMessageBox
import pyHook
import time
from threading import Thread

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

        self.last_time_var = Tkinter.StringVar()
        self.last_time = Tkinter.Label(self, textvariable=self.last_time_var, bg="#ffffff", font=("Helvetica", 12))
        self.last_time.grid(row=3, column=1, columnspan=2, padx=20)

        self.grid_rowconfigure(4, pad=15)

        self.start_button = Tkinter.Button(self, text="Start", bg="lightgreen", command=self.start_counting, width=15)
        self.start_button.grid(row=4, column=1)

        self.pause_button = Tkinter.Button(self, text="Pause", command=self.toggle_pause, width=15)
        self.pause_button.grid(row=4, column=2, padx=10)

        self.bind("<<counter>>", lambda event: self.counter())

    def counter(self):
        self.count += 1
        print self.count
        self.num_of_keystrokes_var.set(str(self.count))
        self.last_time_var.set(time.strftime("%b %d %Y %H:%M:%S", time.localtime()))

    def on_keyboard_event(self, event):
        print event.Key
        #print key_pressed.Ascii

        thread = Thread(target = lambda self: self.event_generate("<<counter>>", when="tail"), args= (self, ))
        thread.start()

        return True

    def start_counting(self):
        print "Starting counting..."
        self.start_button.config(state=Tkinter.DISABLED, bg="grey")
        self.start_time_var.set(time.strftime("%b %d %Y %H:%M:%S", time.localtime()))
        self.last_time_var.set("")
        self.num_of_keystrokes_var.set("")
        self.hookmanager = pyHook.HookManager()
        self.hookmanager.KeyDown = self.on_keyboard_event
        self.hookmanager.HookKeyboard()

    def toggle_pause(self):
       if self.pause_button.config("text")[-1] == "Pause":
          print "Pausing counting..."
          self.hookmanager.UnhookKeyboard()
          self.pause_button.config(text="Resume")
       else:
          print "Resuming counting..."
          self.hookmanager.HookKeyboard()
          self.pause_button.config(text="Pause")

    def close_program_warning(self):
       if tkMessageBox.askokcancel("Really quit?", "Are you sure you want to quit?"):
           self.quit()

if __name__ == "__main__":
    top = WKB_Tester(None)
    top.title("Wireless Keyboard Battery Tester")
    top.wm_iconbitmap("icon.ico")
    top.configure(background="#ffffff")
    top.protocol("WM_DELETE_WINDOW", top.close_program_warning)

    top.mainloop()
