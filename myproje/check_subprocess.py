import subprocess

def run_command(command):
    try:
        # Run the command and capture output
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        print("Command output:\n", result.stdout)
    except subprocess.CalledProcessError as e:
        # Handle the subprocess error (e.g., command not executed correctly)
        print("An error occurred while running the command:")
        print("Return code:", e.returncode)
        print("Error output:\n", e.stderr)
    except FileNotFoundError:
        # Handle the case where the command is not found
        print(f"Error: Command '{command[0]}' not found.")

if __name__ == "__main__":
    print("Testing valid command:")
    run_command(['ls', '-l'])  # Should succeed

    print("\nTesting non-existent command:")
    run_command(['non_existent_command'])  # Should fail with a custom message

    print("\nTesting command that might fail due to permissions:")
    run_command(['mkdir', '/root/test_directory'])  # Should fail if not run as root
