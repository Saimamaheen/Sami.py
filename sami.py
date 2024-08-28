import os,platform
os.system('git pull --quiet 2>/dev/null')
os.system("clear")
print('\033[92;1m [\033[97;1m•\033[92;1m] Join Whatsapp Group')
os.system('xdg-open https://chat.whatsapp.com/Cz1YNy1THc0GHnejXOZcID')
Sami=platform.architecture()[0]
if Sami=="32bit":
    os.system("clear");exit("\033[91;1m 32Bit Device Not Supported")
    __import__("s64")
elif Sami=="64bit":
    __import__("s64")