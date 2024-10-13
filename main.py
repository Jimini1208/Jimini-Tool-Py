import os
import importlib
import sys
import requests
from pystyle import Colors, Center
import time

REPO_URL_MAIN = "https://raw.githubusercontent.com/UncensoredUsers/Jimini-Tool-Py/refs/heads/main/main.py"

def check_and_install(module_name):
    try:
        importlib.import_module(module_name)
    except ImportError:
        print(f"{module_name} is not installed. Installing...")
        os.system(f"{sys.executable} -m pip install {module_name}")

def check_for_update(url):
    """Check for updates from the given URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error checking for update: {e}")
        return None

def update_program(latest_code, filename):
    with open(filename, "w", encoding='utf-8') as f:
        f.write(latest_code)
    print("Update downloaded successfully.")

def display_ascii_art():
    jimini_ascii_art = """
         ██╗██╗███╗   ███╗██╗███╗  ██╗██╗  ████████╗ █████╗  █████╗ ██╗
         ██║██║████╗ ████║██║████╗ ██║██║  ╚══██╔══╝██╔══██╗██╔══██╗██║
         ██║██║██╔████╔██║██║██╔██╗██║██║     ██║   ██║  ██║██║  ██║██║
    ██╗  ██║██║██║╚██╔╝██║██║██║╚████║██║     ██║   ██║  ██║██║  ██║██║
    ╚█████╔╝██║██║ ╚═╝ ██║██║██║ ╚███║██║     ██║   ╚█████╔╝╚█████╔╝███████╗
     ╚════╝ ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚══╝╚═╝     ╚═╝    ╚════╝  ╚════╝ ╚══════╝
    """
    os.system('cls')
    print(Colors.light_blue, Center.XCenter(jimini_ascii_art))

def main():
    modules_to_check = ['requests', 'pystyle']

    for module in modules_to_check:
        check_and_install(module)

    print("All Modules Checked")
    time.sleep(1)

    # Check for updates
    print("Checking for updates...")
    latest_code = check_for_update(REPO_URL_MAIN)

    if latest_code:
        update_program(latest_code, "main.py")

    time.sleep(1)
    display_ascii_art()
    os.system('pause')

if __name__ == "__main__":
    main()
