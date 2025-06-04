from BitHide.encoder import hide_data_in_image
from BitHide.decoder import decode_image
import tkinter as tk
from tkinter import filedialog
from colorama import init, Fore, Style
import time
import os

# Init colorama
init(autoreset=True)

VALID_EXTENSIONS = ('.png', '.jpg', '.jpeg', '.bmp', '.gif')
DEFAULT_OUTPUT_PATH = "BitHide_output.png"

def browse_files():
    root = tk.Tk()
    root.withdraw()
    root.lift()
    root.attributes('-topmost', True)
    root.update()
    file_path = filedialog.askopenfilename(
        title="Select an Image File",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp *.gif")]
    )
    root.destroy()
    return file_path

def print_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = f"""{Fore.CYAN}{Style.BRIGHT}
 _______  ___   _______  __   __  ___   ______   _______ 
|  _    ||   | |       ||  | |  ||   | |      | |       |
| |_|   ||   | |_     _||  |_|  ||   | |  _    ||    ___|
|       ||   |   |   |  |       ||   | | | |   ||   |___ 
|  _   | |   |   |   |  |       ||   | | |_|   ||    ___|
| |_|   ||   |   |   |  |   _   ||   | |       ||   |___ 
|_______||___|   |___|  |__| |__||___| |______| |_______|  

{Style.RESET_ALL}{Fore.CYAN}BitHide - Steganography Tool by Itamar
{Style.RESET_ALL}
"""
    print(banner)


if __name__ == "__main__":
    print_banner()

    opt = input(
        Fore.CYAN + "Welcome!\n\n" +
        "What would you like to do?\n\n" + Style.RESET_ALL +
        Fore.CYAN + "1) " + Style.RESET_ALL + "Embed text into image\n" +
        Fore.CYAN + "2) " + Style.RESET_ALL + "Extract text from image\n\n" +
        Fore.BLUE + "-> " + Style.RESET_ALL
    ).strip()

    if opt == '1':
        time.sleep(0.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        msg = input(Fore.CYAN + "Enter the message to embed: " + Style.RESET_ALL).strip()

        file_path = browse_files()
        if not file_path or not file_path.lower().endswith(VALID_EXTENSIONS):
            print(Fore.RED + "[ERROR] Invalid or unsupported input file.")
            exit()

        special_output_path = input(Fore.BLUE + "\nEnter an output image path (press enter to use default): " + Fore.RESET).strip()
        if special_output_path == "":
            special_output_path = DEFAULT_OUTPUT_PATH
        elif os.path.isdir(special_output_path):
            special_output_path = os.path.join(special_output_path, "BitHide.png")

        if not special_output_path.lower().endswith(VALID_EXTENSIONS):
            print(Fore.RED + "[ERROR] Output file must have a valid image extension.")
            exit()

        try:
            hide_data_in_image(file_path, msg, special_output_path)
            print(Fore.GREEN + f"Message successfully embedded into {special_output_path}")
        except Exception as e:
            print(Fore.RED + "[ERROR] Failed to embed message: " + str(e))

    elif opt == '2':
        time.sleep(0.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        pth = browse_files()
        if not pth or not pth.lower().endswith(VALID_EXTENSIONS):
            print(Fore.RED + "[ERROR] Unsupported or missing image for decoding.")
            exit()
        try:
            hidden = decode_image(pth)
            if hidden:
                print(Fore.GREEN + "Hidden message: " + hidden)
            else:
                print(Fore.YELLOW + "No hidden message found.")
        except Exception as e:
            print(Fore.RED + "[ERROR] Failed to decode message: " + str(e))

    else:
        print(Fore.RED + "That's not an option :(")
