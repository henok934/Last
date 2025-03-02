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
    # Replace 'your_package' with the actual package you want to install
    command = ["pip", "install", "your_package"]
    run_command(command)

if __name__ == "__main__":
    main()
