# Wireless Keyboard Testing for Batteroo Batterisers

It's quick and dirty right now! 

TODO: 
-------
- Focus on Linux version for use with Raspberry Pi
- Fix the broken Windows tester.py - it cannot do a 'live' update of keystrokes pressed. May have something to do with threads

Updates
--------
- Linux version now captures start time and time of last keystroke
- Linux version - space bar gives progress report without updating last keystroke time or counting a keystroke (useful when upi switch batteries with fresh ones - just press space bar to to report without updating the last keystroke time)

Thoughts
---------
- Hook up a wireless keyboard to a Raspberry Pi
- More discussion at EEVBlog Batteroo testing http://www.eevblog.com/forum/projects/batteroo-testing/

Windows
--------
Currently broken

A standalone .exe will be made once it's ready

For developers, to make life easier, use python 2.7 - 32 bit edition

Install pyhook for python 2.7 32 bit from http://www.lfd.uci.edu/~gohlke/pythonlibs/#pyhook or https://sourceforge.net/projects/pyhook/

Python extensions for windows https://sourceforge.net/projects/pywin32/?source=typ_redirect

It still complained, so I also ran: pip install pypiwin32


Linux
-------
Requires Python and Xlib

Download both files, put in same directory, from a terminal run: python tester.py

Written for Python 2.7

Mac
-----

I don't have a Mac. I have access to one now and then, so I can whip up something quick. But hard to maintain. 

Help is welcome!
