import os
import sys


path = r"C:\Program64\Python\Packages"
req = fr"{path}\requirements.txt"


def install(package, path):
    os.system(f"echo ****************************************************")
    os.system(f"echo {package}")
    os.system(f"echo ****************************************************")
    if "pip" in package:
        os.system(f"python -m pip install --upgrade pip --no-index --find-links {path}")
    elif "numpy==1.19.2" in package and sys.version_info.minor == 9:
        os.system(f"echo Package is not compatible with current Python version")
    else:
        os.system(f"pip install --no-index --find-links {path} {package}")


if __name__ == "__main__":
    with open(req) as f:
        for line in f:
            install(line, path)