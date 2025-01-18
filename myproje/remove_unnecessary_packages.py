import subprocess

# Load the required packages
with open('required_packages.txt') as f:
    required_packages = {line.strip().lower() for line in f}

# Load the installed packages
with open('installed_packages.txt') as f:
    installed_packages = {line.strip().lower() for line in f}

# Identify unnecessary packages
unnecessary_packages = installed_packages - required_packages

# Uninstall unnecessary packages
for package in unnecessary_packages:
    subprocess.call(['pip', 'uninstall', package, '-y'])
<<<<<<< HEAD

=======
>>>>>>> origin/main
