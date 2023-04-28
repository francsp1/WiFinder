#!/usr/bin/env python3
import signal
import os
import sys
import subprocess
import time
import glob
import shutil
from pynput.keyboard import Controller, Key
import pandas as pd
import importlib

def signal_handler(sig, frame):
    time.sleep(2)
    

def main():

    signal.signal(signal.SIGINT, signal_handler)    
    print("Hello world")
    # Clear stdout 
    sys.stdout.flush()
 
    command = ["python3", "/home/pi/projeto/wifite2/wifite.py", "--all", "--kill", "--skip-crack", "--no-wps", "--no-pmkid", "--clients-only"]
    wifite_process = subprocess.Popen(command)
        
    # Wait for 3 minutes
    time.sleep(15)
 
    # Copy 
    shutil.copy2(glob.glob('/tmp/wifite*/airodump-01.csv')[0], './')
    time.sleep(2)  

    # Send the CTRL + C keystroke to stop scanning and "all" to attack all networks
    keyboard = Controller()
    keyboard.press(Key.ctrl)
    keyboard.press('c')
    keyboard.release('c')
    keyboard.release(Key.ctrl)
    time.sleep(3)
    keyboard.type('all\n')

    wifite_process.wait()
 

if __name__ == "__main__":
    main()
