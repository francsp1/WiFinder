#!/usr/bin/env python3
import os
import subprocess
import tkinter as tk
from PIL import Image, ImageTk #(do the import of the ImageTk module)

# Function that will be called when the button is clicked
def analyzer():
    # detect the default terminal emulator
    terminal = os.environ.get("XDG_TERMINAL", "x-terminal-emulator")

    # open a new terminal window and run the analizer script 
    subprocess.Popen([terminal, "-e", "bash", "-c", "python3 analyzer.py"])


def main():
    # Create the GUI window
    root = tk.Tk()

    # Create a button and add it to the window
    button = tk.Button(root, text="Click me!", command=analyzer)
    button.pack()

    # Run the GUI event loop
    root.mainloop()




    #My code to create a window and a button
    def start_program():
        # aqui você pode inserir o código para iniciar o programa "wifindier.py"
        print("Programa iniciado!")

    def show_details():
        # aqui você pode inserir o código para mostrar uma nova janela com o seu nome "Rodrigo"
        window = tk.Toplevel(root)
        label = tk.Label(window, text="Código desenvolvido por: Francisco Pedrosa e Rodrigo Vitorino \n" + 
                                    "Desenvolvido no âmbito do Projeto Informático, no IPLeiria. \n \n" +
                                                            "2022/2023")
        label.pack()


    root = tk.Tk()
    #define o título da janela
    root.title("WiFinder")
    root.geometry("300x400") # define o tamanho da janela

    # adiciona o logotipo
    logo_image = Image.open("Capturar.JPG")  # substitua "logo.png" pelo nome do seu arquivo de imagem
    logo_photo = ImageTk.PhotoImage(logo_image)
    logo_label = tk.Label(root, image=logo_photo)
    logo_label.pack(side="top", pady=10)

    start_button = tk.Button(root, text="Start", width=15, height=2, command=start_program)
    start_button.pack(pady=20) # adiciona o botão "Start" na janela

    details_button = tk.Button(root, text="Detalhes", width=15, height=2, command=show_details)
    details_button.pack() # adiciona o botão "Detalhes" na janela

if __name__ == "__main__":
    main()


