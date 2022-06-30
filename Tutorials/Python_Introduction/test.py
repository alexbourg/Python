import time
from random import randint
try:
    import pyautogui as auto
except:
    def install(package):
        import subprocess, sys
        subprocess.check_call(['lpip', "install", package])
    install('pyautogui')
    import pyautogui as auto

auto.FAILSAFE = False
auto.hotkey("win", "d")

def startx():
    auto.moveTo(1204, 334)
    auto.moveTo(522, 396)
    time.sleep(1)
    auto.click()
    auto.moveTo(1204, 334)
    auto.moveTo(522, 396)
    time.sleep(1)
    auto.click()
    auto.moveTo(1204, 334)
    auto.moveTo(522, 396)
    time.sleep(1)
    t = randint(500, 720)
    time.sleep(t)

while True:
    startx()
