
import os
from pyfiglet import Figlet
from playsound import playsound
cwd = os.getcwd()
# color 
black='\033[30m'
red='\033[31m'
green='\033[32m'
orange='\033[33m'
blue='\033[34m'
purple='\033[35m'
cyan='\033[36m'
lightgrey='\033[37m'
darkgrey='\033[90m'
lightred='\033[91m'
lightgreen='\033[92m'
yellow='\033[93m'
lightblue='\033[94m'
pink='\033[95m'
lightcyan='\033[96m'


command = 'clear'
if os.name in ('nt', 'dos'):
    command = 'cls'
    os.system(command)
f = Figlet(font='slant')
print (cyan+(f.renderText('''MP3 P l a y y e r'''))+cyan)
print(red+"+~+~+~+~+~+~+~+~+~+~+~~+~+~+~+ Created By Abhishek Gandre +~+~+~+~+~+~+~+~+~+~+~~+~+~+~+ "+red)
print(blue+"+~+~+~+~+~+~+~+~+~+~+~~+~+~+~+ Mp3 Files Only Supported.. +~+~+~+~+~+~+~+~+~+~+~~+~+~+~+ "+blue)
mp3=str(input(yellow+'Drag and Drop(example.mp3):'+yellow).strip())
playsound(mp3);
