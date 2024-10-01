import subprocess
import sys
import os

def install_linux_dependencies():
    try:
        print("Mise à jour des paquets système...")
        subprocess.check_call(['sudo', 'apt', 'update'])
        
        print("Installation de pip3 et des autres dépendances système...")
        subprocess.check_call(['sudo', 'apt', 'install', '-y', 'python3-pip', 'python3-venv', 'build-essential'])
        
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'installation des dépendances système : {e}")
        sys.exit(1)

def install_macos_dependencies():
    try:
        print("Assurez-vous que Homebrew est installé.")
        subprocess.check_call(['brew', 'install', 'python@3'])
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'installation des dépendances Homebrew : {e}")
        sys.exit(1)

def install_windows_dependencies():
    try:
        print("Installation de Python et pip via le gestionnaire de packages Windows.")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'installation des dépendances Python : {e}")
        sys.exit(1)

def install_python_packages():
    try:
        with open('requirements.txt') as f:
            required = f.read().splitlines()

        print("Installation des packages Python...")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])

        print("Toutes les dépendances ont été installées avec succès.")

    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'installation des packages Python : {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Erreur inattendue : {e}")
        sys.exit(1)

def install_packages():
    if sys.platform.startswith('linux'):
        install_linux_dependencies()
    elif sys.platform.startswith('darwin'):
        install_macos_dependencies()
    elif sys.platform.startswith('win'):
        install_windows_dependencies()
    else:
        print("Système d'exploitation non supporté.")
        sys.exit(1)

    install_python_packages()

if __name__ == "__main__":
    install_packages()
