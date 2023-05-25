#!/usr/bin/env python3
import os
import subprocess
import tkinter as tk
from PIL import Image, ImageTk #(do the import of the ImageTk module)


process = None

# Function that will be called when the button is clicked
def start_program(root):
    global process
    # detect the default terminal emulator
    terminal = os.environ.get("XDG_TERMINAL", "x-terminal-emulator")

    # open a new terminal window and run the analizer script 
    process = subprocess.Popen([terminal, "-e", "bash", "-c", "python3 analyzer.py"])
    print("Programa iniciado!")
    
def show_details(root):
    # aqui você pode inserir o código para mostrar uma nova janela com o seu nome "Rodrigo"
    window = tk.Toplevel(root)
    label = tk.Label(window, text="Código desenvolvido por: Francisco Pedrosa e Rodrigo Vitorino \n" + 
                                "Desenvolvido no âmbito do Projeto Informático, no IPLeiria. \n \n" +
                                                        "2022/2023")
    label.pack()

def exit_program():
    global process
    if process:
        process.terminate()
    exit(0)


def main():
    # Create the GUI window
    root = tk.Tk()
    
    # Define o título da janela
    root.title("WiFinder")

    screen_width = root.winfo_screenwidth()
    screen_height = 415 #root.winfo_screenheight()

    # Calculate the dynamic window size based on the screen dimensions
    window_width = int(screen_width / 4)
    window_height = screen_height

    # Set the window size
    window_size = f"{window_width}x{window_height}"
    root.geometry(window_size)

    root.geometry(f"+0+0")

    # adiciona o logotipo
    logo_image = Image.open("assets/capturar.png")  # substitua "logo.png" pelo nome do seu arquivo de imagem
    logo_photo = ImageTk.PhotoImage(logo_image)
    logo_label = tk.Label(root, image=logo_photo)
    logo_label.pack(side="top", pady=10)

    start_button = tk.Button(root, text="Start", width=15, height=2, command=lambda: start_program(root))
    start_button.pack()


    #details_button = tk.Button(root, text="Detalhes", width=15, height=2, command=show_details(root))
    details_button = tk.Button(root, text="Detalhes", width=15, height=2, command=lambda: show_details(root))
    details_button.pack() # adiciona o botão "Detalhes" na janela
    
    details_button = tk.Button(root, text="Sair", width=15, height=2, command=lambda: exit_program())
    details_button.pack() # adiciona o botão "Sair" na janela
    
    # Run the GUI event loop
    root.mainloop()

if __name__ == "__main__":
    main()