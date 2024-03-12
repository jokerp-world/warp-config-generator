import os
from colorama import Fore
import time
os.system("chmod +x scan.sh")


BOLD = '\033[1m'
logo = Fore.GREEN+'''
██╗██████╗  █████╗ ███╗   ██╗
██║██╔══██╗██╔══██╗████╗  ██║'''+Fore.WHITE+'''
██║██████╔╝███████║██╔██╗ ██║
██║██╔══██╗██╔══██║██║╚██╗██║'''+Fore.RED+'''
██║██║  ██║██║  ██║██║ ╚████║
╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
''' +BOLD+Fore.BLUE +'''#Segaro #yusef_gobadi \n'''

os.system('cls' if os.name == 'nt' else 'clear')

print(logo+"\n"+Fore.YELLOW+"BY: "+Fore.RED+"JOKERP \n\n\n")

print(Fore.MAGENTA+BOLD+"------------------—------------- \n"+Fore.WHITE)
print(Fore.YELLOW+"1: "+Fore.GREEN+BOLD+"Config with license and IP \n"+Fore.WHITE)
print(Fore.YELLOW+"2: "+Fore.GREEN+BOLD+"Configuration only license and auto IP \n"+Fore.WHITE)
print(Fore.YELLOW+"3: "+Fore.GREEN+BOLD+"Configuration only IP \n"+Fore.WHITE)
print(Fore.YELLOW+"4: "+Fore.GREEN+BOLD+"Fully auto config \n"+Fore.WHITE)
print(Fore.YELLOW+"0: "+Fore.GREEN+BOLD+"Exit  \n"+Fore.WHITE)
print(Fore.MAGENTA+BOLD+"------------------—------------- \n"+Fore.WHITE)


inp = int(input(BOLD+"Please enter one of the numbers: "))


if inp == 1:
        os.system("./scan.sh")
        os.system("cat result.csv | grep -oE '[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+:[0-9]+' | head -n 1 > data.txt")
        print(BOLD+Fore.YELLOW+"Please Wait .....")
        os.system("python3 license.py")


        with open('data.txt', 'r') as file:
                license = file.readlines()


        license[1] = license[1].strip()
        license[0] = license[0].strip()


        print(BOLD+Fore.BLUE+"\n-------------------------------------------\n")
        print(Fore.YELLOW+"Your config ----> : "+BOLD+Fore.GREEN+f"warp://{license[1]}@{license[0]}/?ifp=5-10")
        print(BOLD+Fore.BLUE+"\n-------------------------------------------")
if inp == 2:
        print(BOLD+Fore.YELLOW+"Please Wait .....")
        os.system("python3 license2.py")

        with open('data.txt', 'r') as file:
                license = file.readlines

        license[0] = license[0].strip()


        print(BOLD+Fore.BLUE+"\n-------------------------------------------\n")
        print(Fore.YELLOW+"Your config ----> : "+BOLD+Fore.GREEN+f"warp://{license[0]}@auto")
        print(BOLD+Fore.BLUE+"\n-------------------------------------------")


if inp == 3:
        os.system("./scan.sh")
        os.system("cat result.csv | grep -oE '[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+:[0-9]+' | head -n 1 > data.txt")
        print(BOLD+Fore.YELLOW+"Please Wait .....")


        with open('data.txt', 'r') as file:
                license = file.readlines()



        license[0] = license[0].strip()


        print(BOLD+Fore.BLUE+"\n-------------------------------------------\n")
        print(Fore.YELLOW+"Your config ----> : "+BOLD+Fore.GREEN+f"warp://{license[0]}/?ifp=5-10")
        print(BOLD+Fore.BLUE+"\n-------------------------------------------")
if inp == 4:

        print(BOLD+Fore.BLUE+"\n---------------------------\n")
        print(Fore.YELLOW+"Your config ----> : "+BOLD+Fore.GREEN+f"warp://auto")
        print(BOLD+Fore.BLUE+"\n-----------------------------\n")
