import os
import platform

def add_to_startup(file_path):
    if platform.system() == "Windows":
        startup_dir = os.path.join(os.getenv('APPDATA'), 'Microsoft\\Windows\\Start Menu\\Programs\\Startup')
        startup_file = os.path.join(startup_dir, os.path.basename(file_path))
        os.system(f'copy "{file_path}" "{startup_file}"')
    elif platform.system() == "Linux":
        autostart_dir = os.path.expanduser('~/.config/autostart/')
        os.makedirs(autostart_dir, exist_ok=True)
        startup_file = os.path.join(autostart_dir, os.path.basename(file_path))
        os.system(f'cp {file_path} {startup_file}')
    else:
        print("Unsupported OS for persistence")
