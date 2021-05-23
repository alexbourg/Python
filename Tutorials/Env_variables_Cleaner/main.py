Python_Env_Var_cleaner_version = "0.0.1"
__author__ = "Alex BOURG"
__copyright__ = "Copyright 2021"
__license__ = "GPL"
__version__ = Python_Env_Var_cleaner_version
__email__ = "alex.bourg@outlook.com"
__status__ = "Production"


import subprocess
import time
import os, sys


def powershell(cmd):
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    return completed


def clean_old_dir():
    if enable_kill_python:
        try:
            powershell('Stop-Process -Name "python" -Force')
            powershell('Stop-Process -Name "pythonw" -Force')
        except:
            pass

    try:
        print("*************************************************")
        print("Action: cleaning old python directories")
        print("*************************************************")
        powershell('Remove - Item - Force $ENV: UserProfile\AppData\Local\Microsoft\WindowsApps\python.exe')
        powershell('Remove - Item - Force $ENV: UserProfile\AppData\Local\Microsoft\WindowsApps\python3.exe')
        powershell('Remove-Item -Recurse -Force "C:\Program64\Python\Python"')
        powershell('Remove-Item -Recurse -Force "C:\Program64\Python\Python39"')
        powershell('Remove-Item -Recurse -Force "C:\Program64\Python38"')


    except:
        pass


def clean_all_env():
    print()
    print("*************************************************")
    print("Action: cleaning all environment items")
    print("*************************************************")
    print()
    whitelist = ["PYTHONIOENCODING", "PYTHONUNBUFFERED", "PYTHONPATH"]
    for item, value in os.environ.items():
        if (
            "python" in item.lower()
            or "anaconda" in item.lower()
            or "poppler" in item.lower()
        ):
            if item not in whitelist:
                print()
                print(f"Cleaning... {item}")
                print(value)
                print("*************************")
                powershell(
                    f'[Environment]::SetEnvironmentVariable("{item}", $null, "User")'
                )
                powershell(
                    f'[Environment]::SetEnvironmentVariable("{item}", $null, "Machine")'
                )


def clean_path_env():
    print()
    print("*************************************************")
    print('Action: cleaning "PATH" environment items')
    print("*************************************************")
    print()
    profiles = ['"User"', '"Machine"']
    blacklist = ["python", "anaconda", "poppler"]
    for profile in profiles:
        new_env = []
        old_env = powershell(
            f'[Environment]::GetEnvironmentVariable("PATH", {profile})'
        )

        old_env = old_env.stdout.decode("utf-8")

        if len(old_env) > 0:
            print()
            old_env = old_env.replace("\n", "")
            old_env = old_env.replace("\r", "")
            old_env = old_env.replace(";;", ";")
            old_env = old_env.replace(";;;", ";")

            if old_env[-1] == ";":
                old_env = old_env[:-1]

            old_env = old_env.split(";")

            for env in old_env:
                if any(s in env.lower() for s in blacklist):
                    print()
                    print(f"Cleaning... {env}")

                else:
                    new_env.append(env)

            new_env = set(new_env)
            new_env = f"'{';'.join(new_env)}'"
            powershell(
                f'[System.Environment]::SetEnvironmentVariable("Path", {new_env},[System.EnvironmentVariableTarget]::{profile})'
            )


def clean_path_ext():
    print()
    print("*************************************************")
    print('Action: cleaning "PATHEXT"')
    print("*************************************************")
    profiles = ['"User"', '"Machine"']
    blacklist = [".PY"]

    for profile in profiles:
        new_env = []
        old_env = powershell(
            f'[Environment]::GetEnvironmentVariable("PATHEXT", {profile})'
        )
        old_env = old_env.stdout.decode("utf-8")
        if len(old_env) > 0:
            old_env = old_env.replace("\n", ";")
            old_env = old_env.replace("\r", ";")
            old_env = old_env.replace(";;", ";")
            old_env = old_env.replace(";;;", ";")

            if old_env[-1] == ";":
                old_env = old_env[:-1]

            old_env = old_env.split(";")

            for env in old_env:
                if any(s in env for s in blacklist):
                    print()
                    print(f"Cleaning... {env}")
                else:
                    new_env.append(env)

            new_env = set(new_env)
            new_env = f"'{';'.join(new_env)}'"
            powershell(
                f'[System.Environment]::SetEnvironmentVariable("PathEXT", {new_env},[System.EnvironmentVariableTarget]::{profile})'
            )


if __name__ == "__main__":
    options = sys.argv
    for i in range(len(options)):
        options[i] = options[i].lower()
    print("*************************************************")
    print("Python installation is starting ... please wait!")
    print("*************************************************")
    print()
    time.sleep(4)

    if 'kill_python' in options or '/kill_python' in options or '-kill_python' in options:
        enable_kill_python = True
    else:
        enable_kill_python = False

    if 'clean_old_dir' in options or '-clean_old_dir' in options or '/clean_old_dir' in options:
        enable_clean_old_dir = True
    else:
        enable_clean_old_dir = False

    if 'clean_all_env' in options or '-clean_all_env' in options or '/clean_all_env' in options:
        enable_clean_all_env = True
    else:
        enable_clean_all_env = False

    if 'clean_path_env' in options or '-clean_path_env' in options or '/clean_path_env' in options:
        enable_clean_path_env = True
    else:
        enable_clean_path_env = False

    if 'clean_path_ext' in options or '-clean_path_ext' in options or '/clean_path_ext' in options:
        enable_clean_path_ext = True
    else:
        enable_clean_path_ext = False

    if enable_clean_old_dir:
        try:
            clean_old_dir()
        except:
            pass

    if enable_clean_all_env:
        try:
            clean_all_env()
        except:
            pass

    if enable_clean_path_env:
        try:
            clean_path_env()
        except:
            pass

    if enable_clean_path_ext:
        try:
            clean_path_ext()
        except:
            pass