# your_script.py

import subprocess

def run_command(command):
    try:
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        print("Command Output:\n", result.stdout)
        
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running command: {e.cmd}")
        print(f"Return code: {e.returncode}")
        print(f"Error Output:\n{e.stderr}")

def main():
    command = ["ls", "-l"]  # Change this to any command you want to test
    run_command(command)

if __name__ == "__main__":
    main()
