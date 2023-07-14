#!/usr/bin/env python3
import time
import os
import subprocess
import tkinter as tk
from PIL import Image, ImageTk #(do the import of the ImageTk module)
import RPi.GPIO as GPIO 
import requests
import shutil

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

SWITCH_PIN = 14  #GPIO pin number of the switch 
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

RED_PIN = 22 #GPIO pin number of the red pin
GREEN_PIN = 27 #GPIO pin number of the green pin
BLUE_PIN = 17 #GPIO pin number of the blue pin

#set the GPIO pin out
GPIO.setup(RED_PIN, GPIO.OUT) 
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)

#used to exit program
process = None

API_IP = '192.168.233.231' 
API_PORT = 3000  
API_URL_CHECK = f'http://{API_IP}:{API_PORT}/check'
API_URL_UPLOAD = f'http://{API_IP}:{API_PORT}/upload'
API_TIMEOUT = 5
CSV_DIR      = '/home/pi/projeto/WiFinder/csv'
SENT_CSV_DIR = '/home/pi/projeto/WiFinder/sent_csv'


def set_led_red():
    GPIO.output(RED_PIN, GPIO.HIGH)  # Turn on red color
    GPIO.output(GREEN_PIN, GPIO.LOW)  # Turn off green color
    GPIO.output(BLUE_PIN, GPIO.LOW)  # Turn off blue color

def set_led_yellow():
    GPIO.output(RED_PIN, GPIO.HIGH)  # Turn on red color
    GPIO.output(GREEN_PIN, GPIO.HIGH)  # Turn on green color
    GPIO.output(BLUE_PIN, GPIO.LOW)  # Turn off blue color
    
def set_led_green():
    GPIO.output(RED_PIN, GPIO.LOW)  # Turn off red color
    GPIO.output(GREEN_PIN, GPIO.HIGH)  # Turn on green color
    GPIO.output(BLUE_PIN, GPIO.LOW)  # Turn off blue color

# Function that will be called when the button START is clicked
def start_program(root):
    global process
    
    time.sleep(3)
    
    #Turn on yellow led
    set_led_yellow()
        
    # detect the default terminal emulator
    terminal = os.environ.get("XDG_TERMINAL", "x-terminal-emulator")

    # open a new terminal window and run the analizer script 
    process = subprocess.Popen([terminal, "-e", "bash", "-c", "python3 analyzer.py 2> stderr.txt"])
    print("Programa iniciado!")

def send_csvs():
    try:
        # Check if the API is running 
        response = requests.get(API_URL_CHECK, timeout=API_TIMEOUT)
        if response.status_code == 200: # If the script has connectivity with the API the csv files will be sent
            for file_name in os.listdir(CSV_DIR): # For each file in csv directory
                file_path = os.path.join(CSV_DIR, file_name)
                if os.path.isfile(file_path):
                    files = {
                        'file': (file_name, open(file_path, 'rb'), 'text/csv')
                    }
                    response = requests.post(API_URL_UPLOAD, files=files) #Send file
                    if response.status_code == 200:
                        print(f"CSV file '{file_name}' uploaded successfully")
                        # Move the file to the sent CSV directory
                        shutil.move(file_path, os.path.join(SENT_CSV_DIR, file_name)) # Move file to sent_csv directory
                    else:
                        print(f"Error uploading CSV file '{file_name}'. Status Code:", response.status_code)
        else:
            print("API is not running or returned an error")
    except requests.exceptions.RequestException as e:
        print("Error occurred while connecting to the API:", e)


    
# Shows a window with the info about who develop the code
def show_details(root):
    window = tk.Toplevel(root)
    label = tk.Label(window, text="Código desenvolvido por: Francisco Pedrosa e Rodrigo Vitorino \n" + 
                                  "Desenvolvido no âmbito do Projeto Informático, no IPLeiria. \n \n" +
                                  "2022/2023")
    label.pack()

# Function that will exit the program
def exit_program():
    global process
    if process:
        process.terminate()
    set_led_red()
    exit(0)


def main():

    # CREATE csv directory if it does not exists
    if not os.path.exists(CSV_DIR):
        os.makedirs(CSV_DIR)

    # CREATE sent_csv directory if it does not exists
    if not os.path.exists(SENT_CSV_DIR):
        os.makedirs(SENT_CSV_DIR)

    # Create the GUI window
    root = tk.Tk()
    
    # Define the window name
    root.title("WiFinder")

    screen_width = root.winfo_screenwidth()
    screen_height = 415 

    # Calculate the dynamic window size based on the screen dimensions
    window_width = int(screen_width / 4)
    window_height = screen_height

    # Set the window size
    window_size = f"{window_width}x{window_height}"
    root.geometry(window_size)

    # set the initial position 
    root.geometry(f"+0+35")

    # Adds the WiFinder Logo
    logo_image = Image.open("assets/capturar.png")
    logo_photo = ImageTk.PhotoImage(logo_image)
    logo_label = tk.Label(root, image=logo_photo)
    logo_label.pack(side="top", pady=10)
    

    # create and add a button labeled "Start"
    start_button = tk.Button(root, text="Start", width=15, height=2, command=lambda: start_program(root))
    start_button.pack()

    # create and add a button labeled "Send CSV's"
    send_csvs_button = tk.Button(root, text="Send CSV's", width=15, height=2, command=lambda: send_csvs())
    send_csvs_button.pack()

    # create and add a button labeled "About"
    about_button = tk.Button(root, text="About", width=15, height=2, command=lambda: show_details(root))
    about_button.pack() 
    
    # create and add a button labeled "Exit"
    exit_button = tk.Button(root, text="Exit", width=15, height=2, command=lambda: exit_program())
    exit_button.pack()
    
    #if the switch's on, led's green and the programm starts, else the programm doesn't start and the led stays red
    if GPIO.input(SWITCH_PIN) == GPIO.HIGH: # ON 
        start_program(root)
        #set_led_green()
    else: 
        set_led_red()
        
    send_csvs()

    # Run the GUI event loop
    root.mainloop()

if __name__ == "__main__":
    main()
