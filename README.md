# Wireless Keyboard Testing for Batteroo Batterisers

It's quick and dirty right now! 

TODO: 
-------
- Capture the time of keystroke, so we can display the time the last keystroke was pressed, which will be useful for unattended tests.
- Add a very simple GUI for Windows using Tkinter

Thoughts
---------
Can we hook up a wireless keyboard to a Raspberry Pi or Arduino, and do tests that way?

Windows
--------

A standalone .exe will be made once I add a couple of features

For developers, to make life easier, use python 2.7 - 32 bit edition

Install pyhook for python 2.7 32 bit from http://www.lfd.uci.edu/~gohlke/pythonlibs/#pyhook or https://sourceforge.net/projects/pyhook/

Python extensions for windows https://sourceforge.net/projects/pywin32/?source=typ_redirect

It still complained, so I also ran: pip install pypiwin32


Linux
-------
Requires Python and Xlib

Download both files, put in same directory, from a terminal run: python tester.py

Written for Python 2.7
