import os
import requests
from pystyle import Colors, Center
import time
import check_module

# GitHub 저장소의 최신 버전 파일 URL
REPO_URL = "https://raw.githubusercontent.com/username/repository/main/latest_version.py"

def check_for_update():
    try:
        response = requests.get(REPO_URL)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error checking for update: {e}")
        return None

def update_program(latest_code):
    with open("latest_version.py", "w") as f:
        f.write(latest_code)
    print("Update downloaded successfully.")

def main():
    jimini_ascii_art = """
         ██╗██╗███╗   ███╗██╗███╗  ██╗██╗  ████████╗ █████╗  █████╗ ██╗
         ██║██║████╗ ████║██║████╗ ██║██║  ╚══██╔══╝██╔══██╗██╔══██╗██║
         ██║██║██╔████╔██║██║██╔██╗██║██║     ██║   ██║  ██║██║  ██║██║
    ██╗  ██║██║██║╚██╔╝██║██║██║╚████║██║     ██║   ██║  ██║██║  ██║██║
    ╚█████╔╝██║██║ ╚═╝ ██║██║██║ ╚███║██║     ██║   ╚█████╔╝╚█████╔╝███████╗
     ╚════╝ ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚══╝╚═╝     ╚═╝    ╚════╝  ╚════╝ ╚══════╝
    """
    
    time.sleep(1)
    print("Checking Modules...")
    check_module.main()
    time.sleep(1)

    print("Checking for updates...")
    latest_code = check_for_update()

    if latest_code:
        update_program(latest_code)

    print("Starting Program...")
    time.sleep(1)
    os.system('cls')
    print(Colors.light_blue, Center.XCenter(jimini_ascii_art))

    os.system('pause')

if __name__ == "__main__":
    main()
