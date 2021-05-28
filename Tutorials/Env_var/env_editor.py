Env_editor_version = "0.0.1"
__author__ = "Alex BOURG"
__copyright__ = "Copyright 2021"
__license__ = "GPL"
__version__ = Env_editor_version
__email__ = "alex.bourg@outlook.com"
__status__ = "Production"


import subprocess


def run(cmd):
    completed = subprocess.run(["rundll32", "-Command", cmd])


if __name__ == '__main__':
    run("sysdm.cpl,EditEnvironmentVariables")
