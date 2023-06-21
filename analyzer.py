#!/usr/bin/env python3
import os
import subprocess
import time
import glob
import shutil
from git import Repo
import threading

SCAN_TIME = 60
HOME_PI_PROJETO = "/home/pi/projeto"
AIRCRACK_REPO_PATH = HOME_PI_PROJETO + "/aircrack-ng"
WIFINDER_PATH = HOME_PI_PROJETO + "/WiFinder"
CSV_DIRECTORY = WIFINDER_PATH + "/csv"

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

def remove_empty_lines(file_path):
    # Read the file and store its content in a list
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Remove empty lines from the list
    lines = [line for line in lines if line.strip() != '']

    # Write the modified lines back to the file
    with open(file_path, 'w') as file:
        file.writelines(line.rstrip() + '\n' for line in lines)


def remove_clients_info_csv_file(file_path):
    target_line = 'Station MAC, First time seen, Last time seen, Power, # packets, BSSID, Probed ESSIDs'
    temp_file_path = file_path + '.tmp'

    with open(file_path, 'r') as file_in, open(temp_file_path, 'w') as file_out:
        found_target_line = False
        for line in file_in:
            if line.strip() == target_line:
                found_target_line = True
                break
            file_out.write(line)

    if found_target_line:
        os.replace(temp_file_path, file_path)
        # Content removed successfully
    else:
        os.remove(temp_file_path)
        # Target line not found in the file
    
    remove_empty_lines(file_path)

def main():

    #Banner of our programm
    print(" ___       ___    _____   _________    _____      __      _   ______      _____   ______    \n" + 
          "(  (       )  )  (_   _) (_   _____)  (_   _)    /  \    / ) (_  __ \    / ___/  (   __ \   \n" +
          " \  \  _  /  /     | |     ) (___       | |     / /\ \  / /    ) ) \ \  ( (__     ) (__) )  \n" + 
          "  \  \/ \/  /      | |    (   ___)      | |     ) ) ) ) ) )   ( (   ) )  ) __)   (    __/   \n" + 
          "   )   _   (       | |     ) (          | |    ( ( ( ( ( (     ) )  ) ) ( (       ) \ \  _  \n" + 
          "   \  ( )  /      _| |__  (   )        _| |__  / /  \ \/ /    / /__/ /   \ \___  ( ( \ \_)) \n" + 
          "    \_/ \_/      /_____(   \_/        /_____( (_/    \__/    (______/     \____\  )_) \__/  \n" ) 

    install_dependencies()

    if not os.path.exists(CSV_DIRECTORY):
        os.makedirs(CSV_DIRECTORY)


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
        os.system("make install")

        file_path = os.path.join(WIFINDER_PATH, "installed.txt")
        with open(file_path, "w") as f:
            f.write("Aircrack-ng for WiFinder is installed!")

        # Update the linker cache
        os.system("sudo ldconfig")
    else:
        print("Aircrack-ng for WiFinder is installed!")
        time.sleep(2)
 
    command = ["wifite", "--all", "--kill", "-i", "wlan1", "--skip-crack", "--no-wps", "--no-pmkid", "--clients-only", "-pow", "25", "--wpat", "180", "-p", str(SCAN_TIME)]
    # command = [WIFITE_PATH, "--all", "--kill", "--skip-crack", "--no-wps", "--no-pmkid", "--clients-only", "-pow", "25", "--wpat", "180", "-p", str(SCAN_TIME)]

    wifite_process = subprocess.Popen(command)
    
    # Wait for 3 minutes
    time.sleep(SCAN_TIME)
 
    # Copy the airodump-ng file created via wifite from tmp directory
    shutil.copy2(glob.glob('/tmp/wifite*/airodump-01.csv')[0], './')
    filename = time.strftime("%d-%m-%Y_%H:%M:%S.csv")
    os.rename("airodump-01.csv", filename)
      
    # Create a thread to remove unnecessary info (clients) from the csv file
    thread = threading.Thread(target=remove_clients_info_csv_file(filename))
    thread.start()

    time.sleep(3)

    wifite_process.wait()
 

if __name__ == "__main__":
    main()
