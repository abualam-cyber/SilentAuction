
import os  
from time import sleep

def screen_clear():
    if os.name == 'posix':
        _ = os.system("clear")
    else:
        _ = os.system("cls")