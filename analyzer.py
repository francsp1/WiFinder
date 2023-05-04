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
from git import Repo


SCAN_TIME = 60
AIRCRACK_REPO_PATH = "/home/pi/projeto/aircrack-ng"
WIFI_ANALYZER_PATH = "/home/pi/projeto/wifi_analyzer"

def sigint_handler(sig, frame):
    time.sleep(3)
    

def main():

    signal.signal(signal.SIGINT, sigint_handler)    

    dependencies = ['iw', 'hcxtools', 'hcxdumptool', 'macchanger']
 
    try:
        subprocess.check_output(['which', 'ifconfig'])
    except:
        subprocess.check_call(['sudo', 'apt-get', 'install', '-y', 'net-tools'])

    #we will check if it has the dependencies to run wifite, if not, it will install them
    for dependency in dependencies:
        try:
            subprocess.check_output(['which', dependency])
        except subprocess.CalledProcessError:
            print(f'{dependency} is not installed. Installing...')
            subprocess.check_call(['sudo', 'apt-get', 'install', '-y', dependency])

   

    if not os.path.isfile(os.path.join(WIFI_ANALYZER_PATH, 'installed.txt')):
        # if the file doesn't exist, the program will remove the directory
        shutil.rmtree(AIRCRACK_REPO_PATH)

        # Install the libtool package
        os.system("sudo apt-get install -y libtool")

        # Clone the repository using python-git library
        repo_url = "https://github.com/francsp1/aircrack-ng.git"
        local_path = "/home/pi/projeto/aircrack-ng/"
        Repo.clone_from(repo_url, local_path)

        # Change the working directory to "/home/pi/projeto/aircrack-ng"
        os.chdir("/home/pi/projeto/aircrack-ng")

        # Run the autoreconf command
        os.system("autoreconf -i")

        # Run the configure command
        os.system("./configure")

        # Run the make command
        os.system("make")

        # Run the make install command
        os.system("sudo make install")

        file_path = os.path.join(WIFI_ANALYZER_PATH, "installed.txt")
        with open(file_path, "w") as f:
            f.write("Aircrack-ng for wifi analyzer is installed!")

        # Update the linker cache
        os.system("sudo ldconfig")
    else:
        print("Aircrack-ng for wifi analyzer is installed!")
        time.sleep(2)

    # Clear stdout 
    sys.stdout.flush()
 
    command = ["python3", "/home/pi/projeto/wifite2/wifite.py", "--all", "--kill", "--skip-crack", "--no-wps", "--no-pmkid", "--clients-only"]
    #command = ["python3", "/home/pi/projeto/wifite2/wifite.py", "--all", "--kill", "--skip-crack", "--no-wps", "--no-pmkid"]

    wifite_process = subprocess.Popen(command)
        
    # Wait for 3 minutes
    time.sleep(SCAN_TIME)
 
    # Copy the airodump-ng file created via wifite from tmp directory
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
