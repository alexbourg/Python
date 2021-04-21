import os
import sys


def install(package, path):
    print(path)
    print(package)
    return
    os.system(f"echo ****************************************************")
    os.system(f"echo {package}")
    os.system(f"echo ****************************************************")
    if "pip" in package:
        os.system(f"python -m pip install --upgrade pip --no-index --find-links {path}")
    elif "numpy==1.19.2" in package and sys.version_info.minor == 9:
        os.system(f"echo {package} is not compatible with current Python version")
    else:
        os.system(f"pip install --no-index --find-links {path} {package}")


if __name__ == "__main__":
    if len(sys.argv) == 3:
        try:
            path = sys.argv[2]
        except:
            path = r"C:\Program64\Python\Packages"

        try:
            req = sys.argv[1]
        except:
            req = fr"{path}\requirements.txt"

    else:
        path = r"C:\Program64\Python\Packages"
        req = fr"{path}\requirements.txt"

    with open(req) as f:
        for line in f:
            install(line, path)
