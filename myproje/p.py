import subprocess

def run_command(command):
    try:
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        print("Command Output:\n", result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running command: {e.cmd}")
        print(f"Return code: {e.returncode}")
        print(f"Error Output:\n{e.stderr}")

# Example usage
run_command(["pip", "install", "your_package"])
