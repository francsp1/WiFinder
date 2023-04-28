#!/usr/bin/env python3
import os
import subprocess
import tkinter as tk

# Function that will be called when the button is clicked
def analyzer():
    # detect the default terminal emulator
    terminal = os.environ.get("XDG_TERMINAL", "x-terminal-emulator")

    # open a new terminal window and run the analizer script 
    #subprocess.Popen([terminal, "-e", "bash", "-c", "python3 analyzer.py"])
    subprocess.Popen([terminal, "-e", "bash", "-c", "python3 analyzer.py"])


def main():
    # Create the GUI window
    root = tk.Tk()

    # Create a button and add it to the window
    button = tk.Button(root, text="Click me!", command=analyzer)
    button.pack()

    # Run the GUI event loop
    root.mainloop()

if __name__ == "__main__":
    main()


