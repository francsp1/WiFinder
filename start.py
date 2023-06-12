#!/usr/bin/env python3
import time
import os
import subprocess
import tkinter as tk
from PIL import Image, ImageTk #(do the import of the ImageTk module)
import RPi.GPIO as GPIO 

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

switch_pin = 14  #GPIO pin number of the switch 
GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

red_pin = 22 #GPIO pin number of the red pin
green_pin = 27 #GPIO pin number of the green pin
blue_pin = 17 #GPIO pin number of the blue pin

#set the GPIO pin out
GPIO.setup(red_pin, GPIO.OUT) 
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(blue_pin, GPIO.OUT)

#used to exit program
process = None


def set_led_red():
    GPIO.output(red_pin, GPIO.HIGH)  # Turn on red color
    GPIO.output(green_pin, GPIO.LOW)  # Turn off green color
    GPIO.output(blue_pin, GPIO.LOW)  # Turn off blue color

def set_led_yellow():
    GPIO.output(red_pin, GPIO.HIGH)  # Turn on red color
    GPIO.output(green_pin, GPIO.HIGH)  # Turn on green color
    GPIO.output(blue_pin, GPIO.LOW)  # Turn off blue color
    
def set_led_green():
    GPIO.output(red_pin, GPIO.LOW)  # Turn off red color
    GPIO.output(green_pin, GPIO.HIGH)  # Turn on green color
    GPIO.output(blue_pin, GPIO.LOW)  # Turn off blue color

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

    # Adds the WiFInder Logo
    logo_image = Image.open("assets/capturar.png")
    logo_photo = ImageTk.PhotoImage(logo_image)
    logo_label = tk.Label(root, image=logo_photo)
    logo_label.pack(side="top", pady=10)
    

    # create and add a button labeled "Start"
    start_button = tk.Button(root, text="Start", width=15, height=2, command=lambda: start_program(root))
    start_button.pack()

    # create and add a button labeled "About"
    details_button = tk.Button(root, text="About", width=15, height=2, command=lambda: show_details(root))
    details_button.pack() 
    
    # create and add a button labeled "Exit"
    details_button = tk.Button(root, text="Exit", width=15, height=2, command=lambda: exit_program())
    details_button.pack()
    
    #if the switch's on, led's green and the programm starts, else the programm doesn't start and the led stays red
    if GPIO.input(switch_pin) == GPIO.HIGH: # ON 
        start_program(root)
        #set_led_green()
    else: 
        set_led_red()
        

    # Run the GUI event loop
    root.mainloop()

if __name__ == "__main__":
    main()
