#!/usr/bin/env python3
import os
import sys
import subprocess
import time
import glob
import shutil
from pynput.keyboard import Controller, Key
import pandas as pd
import importlib
#from git import Repo

def main():
    """
    dependencies = ['iwconfig', 'iw', 'wash', 'hcxtools', 'hcxdumptool', 'macchanger']

    #iremos verificar se tem as dependências para executar o wifite, se não tiver, ele instála-as
    for dependency in dependencies:
        try:
            subprocess.check_output(['which', dependency])
        except subprocess.CalledProcessError:
            print(f'{dependency} não está instalado. Instalando...')
                
            subprocess.check_call(['sudo', 'apt-get', 'install', '-y', dependency])


    #aqui temos de instalar o libtool e fazer o pull do código do francisco
    subprocess.call(["sudo", "apt-get", "install", "-y", "libtool"])

        #subprocess.call(["sudo", "git", "clone", "https://github.com/francsp1/aircrack-ng.git"])
    Repo.clone_from("https://github.com/francsp1/aircrack-ng.git", "/home/pi")

    subprocess.call(["cd", "/home/pi/aircrack-ng"])
    subprocess.call(["autoreconf", "-i"])
    subprocess.call(["./configure"])
    subprocess.call(["make")
    subprocess.call(["make", "install")
    subprocess.call(["ldconfig"])
    """
    print("Hello world")
    #clear stdout 
    sys.stdout.flush()
 
    command = ["/home/pi/projeto/wifite2/wifite.py", "--all", "--kill", "--skip-crack", "--no-wps", "--no-pmkid", "--clients-only"]
    wifite_proces = subprocess.Popen(command)


    # wait for 3 minutes
    time.sleep(15)  
    
    
    shutil.copy2(glob.glob('/tmp/wifite*/airodump-01.csv')[0], './')

    # send the CTRL + C keystroke to stop Wifite
    keyboard = Controller()
    keyboard.press(Key.ctrl)
    keyboard.press('c')
    keyboard.release('c')
    keyboard.release(Key.ctrl)
    
    time.sleep(4)  

    keyboard.type('all\n')

if __name__ == "__main__":
    main()

