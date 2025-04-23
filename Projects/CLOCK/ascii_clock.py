import time
import os 
from pyfiglet import Figlet
import argparse


parser = argparse.ArgumentParser(description="ASCII Clock with Verbose Mode")
parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose mode')
args = parser.parse_args()
VERBOSE = args.verbose


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    if VERBOSE:
        print("[*] Screen cleared.")

def get_current_time():
    t = time.strftime('%H:%M:%S')
    if VERBOSE:
        print(f"[+] Fetched current time: {t}")
    return t


def ascii_clock():
    figlet = Figlet(font='big')
    if VERBOSE:
        print("[*] ASCII font initialized: big")
        print("[*] Clock initializing... Press Ctrl+C to terminate")

    try:
        while True:
            clear_screen()
            current_time = get_current_time()
            ascii_time = figlet.renderText(current_time)
            print(ascii_time)
            if VERBOSE:
                print("[+] Clock running.\n")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[!] Clock terminated.")

if __name__ == '__main__':
    ascii_clock()
