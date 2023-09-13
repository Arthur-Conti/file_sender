import os
import platform

so = platform.system()
if so == "Windows":
    comando = "cls"
else:
    comando = "clear"

def welcome():
    os.system(comando)
    print("Welcome to your personal file sender")
    input("Press ENTER to start")
    