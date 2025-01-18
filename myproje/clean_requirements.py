import subprocess

# List of necessary packages for your Django project
necessary_packages = {
    'django',
    'djangorestframework',
    'psycopg2',
    'Pillow',
    # Add any other necessary packages here
}

def load_requirements(file_path):
    """Load the packages from requirements.txt."""
    with open(file_path) as f:
        return {line.strip().lower() for line in f if line.strip()}

def identify_unnecessary_packages(installed_packages):
    """Identify packages that are not necessary."""
    return installed_packages - necessary_packages

def uninstall_packages(unnecessary_packages):
    """Uninstall unnecessary packages."""
    for package in unnecessary_packages:
        print(f'Uninstalling: {package}')
        subprocess.call(['pip', 'uninstall', package, '-y'])

def clean_requirements(file_path):
    """Clean the requirements file by removing unnecessary packages."""
    installed_packages = load_requirements(file_path)
    unnecessary_packages = identify_unnecessary_packages(installed_packages)

    if unnecessary_packages:
        uninstall_packages(unnecessary_packages)
        print("Uninstallation complete.")
    else:
        print("No unnecessary packages found.")

if __name__ == "__main__":
    requirements_file = 'requirements.txt'
    clean_requirements(requirements_file)

