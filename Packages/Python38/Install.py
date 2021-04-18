import os
import sys


def install(package, path):
    os.system(f"echo ****************************************************")
    os.system(f"echo {package}")
    os.system(f"echo ****************************************************")
    if "pip" in package:
        os.system(f"python -m pip install --upgrade pip --no-index --find-links {path}")
    else:
        os.system(f"pip install --no-index --find-links {path} {package}")


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        for line in f:
            install(line, sys.argv[2])