import os
import importlib
import sys
import requests

REPO_URL = "https://raw.githubusercontent.com/UncensoredUsers/Jimini-Tool-Py/refs/heads/main/check_module.py"

def check_and_install(module_name):
    try:
        importlib.import_module(module_name)
    except ImportError:
        print(f"{module_name} is not installed. Installing...")
        os.system(f"{sys.executable} -m pip install {module_name}")

def check_for_update():
    try:
        response = requests.get(REPO_URL)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error checking for update: {e}")
        return None

def update_program(latest_code):
    with open("main.py", "w") as f:
        f.write(latest_code)
    print("Update downloaded successfully.")

def main():
    modules_to_check = ['requests', 'pystyle']

    for module in modules_to_check:
        check_and_install(module)

    print("All Modules Checked")

    latest_code = check_for_update()

    if latest_code:
        update_program(latest_code)

if __name__ == "__main__":
    main()
