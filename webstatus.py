# Developed by GhostXinn
# Team : XiNN
# WebStatus / Check website status code

# Importing modules
import requests
from colorama import *
import os
import time
init(convert=True)
s = time.sleep

g = Fore.GREEN
r = Fore.RED
w = Fore.WHITE
y = Fore.YELLOW

# Banner
print(f'''
██╗    ██╗███████╗████████╗ WebStatus Information
██║    ██║██╔════╝╚══██╔══╝ Author : gh0stxinn
██║ █╗ ██║███████╗   ██║    Team : xinn Exploit
██║███╗██║╚════██║   ██║   
╚███╔███╔╝███████║   ██║   
 ╚══╝╚══╝ ╚══════╝   ╚═╝   
                           
''')

# Functions
url = input("Website (require https://) : ")
page = requests.get(url) # Get URL

# Waiting
print(f"[{y}PROCESS{w}] Getting status code from {url} please wait...") 
s(5)

# Result
print(f"[{g}STATUS{w}] {url} Status : {page.status_code}") 

# Last Code
print(f"[{r}EXIT{w}] Do you wish to exit?", end='') 
input()