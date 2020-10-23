import pyautogui
import time
from random import randint
from time import sleep
from colorama import init
from colorama import Fore, Back, Style

class bot:
    def __init__(self):
        self.exp = 0

    def lobby(self):
        time.sleep(10)
        print(Fore.YELLOW + "-----> Waiting lobby detection")
        print(Style.RESET_ALL)
        while True:
            lobby = pyautogui.locateOnScreen("1080/lobby.png")
            lobby2 = pyautogui.locateOnScreen("1080/lobby.png", confidence=0.6)
            if lobby is not None or lobby2 is not None:
                print(Fore.GREEN + "    Lobby detected")
                print(Style.RESET_ALL)
                if lobby != None:
                    pyautogui.click(lobby)   
                if lobby2 != None:
                    pyautogui.click(lobby2)    
                time.sleep(1)
                self.ingame()

    def ingame(self):
        print(Fore.YELLOW + "-----> Waiting ingame detection")
        print(Style.RESET_ALL)
        while True:
            ingame = pyautogui.locateOnScreen("1080/ingame.png")
            ingame2 = pyautogui.locateOnScreen("1080/ingame.png", confidence=0.6)
            if ingame is not None or ingame2 is not None:
                print(Fore.GREEN + "    Ingame detected")
                print(Style.RESET_ALL)
                time.sleep(1)
                print(Fore.YELLOW + "-----> Waiting end of the game detection")
                print(Style.RESET_ALL)
                time.sleep(2)
                self.endofthegame()

    def endofthegame(self):
        while True:
            compteur = pyautogui.locateOnScreen("1080/confirm2.png")
            compteur2 = pyautogui.locateOnScreen("1080/confirm2.png", confidence=0.6)
            if compteur is not None or compteur2 is not None:
                print(Fore.GREEN + "    End of the game detected")
                print(Style.RESET_ALL)
                time.sleep(2)
                self.result()
            else:
            	self.antiafk()

    def antiafk(self):
        time.sleep(5)
        pyautogui.keyDown('w',)
        sleep(randint(2, 6)/10)
        pyautogui.keyUp('w')
        pyautogui.keyDown('d')
        pyautogui.click()
        sleep(randint(1, 3)/10)
        pyautogui.click()
        sleep(randint(2, 4)/10)
        pyautogui.keyUp('d')
        pyautogui.keyDown('s')
        sleep(randint(2, 5)/10)
        pyautogui.keyUp('s')
        pyautogui.keyDown('a')
        sleep(randint(4, 6)/10)
        pyautogui.keyUp('a')
        pyautogui.keyDown('w',)
        sleep(randint(2, 4)/10)
        pyautogui.keyUp('w')
        self.endofthegame()

    def result(self):
        print(Fore.YELLOW + "-----> Waiting XP results detection")
        print(Style.RESET_ALL)
        time.sleep(10)
        while True:
            results = pyautogui.locateOnScreen("1080/confirm.png")
            results2 = pyautogui.locateOnScreen("1080/confirm.png", confidence=0.6)
            if results is not None or results2 is not None:
                print(Fore.GREEN + "    XP Results Detected")
                print(Style.RESET_ALL)
                time.sleep(2)
                self.exp += 900
                print(Fore.MAGENTA + " You have won", self.exp, "exp")
                print(Style.RESET_ALL)
                print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
                print("")
                time.sleep(2)
                pyautogui.click(x=980, y=30)
                time.sleep(2)
                self.lobby()          

a = bot()

def main():

    from colorama import init
    from colorama import Fore, Back, Style
    init()
    print(Fore.RED + """ __      __   _                       _     __   __        ____        _   
 \ \    / /  | |                     | |    \ \ / /       |  _ \      | |  
  \ \  / /_ _| | ___  _ __ __ _ _ __ | |_    \ V / _ __   | |_) | ___ | |_ 
   \ \/ / _` | |/ _ \| '__/ _` | '_ \| __|    > < | '_ \  |  _ < / _ \| __|
    \  / (_| | | (_) | | | (_| | | | | |_    / . \| |_) | | |_) | (_) | |_ 
     \/ \__,_|_|\___/|_|  \__,_|_| |_|\__|  /_/ \_\ .__/  |____/ \___/ \__|
                                                  | |                      
                                                  |_|                      """)
    print(Style.RESET_ALL)

    print(Style.BRIGHT + Fore.BLUE + "                              Only for Deathmatch")
    print(Style.RESET_ALL)
    print(Fore.CYAN + "                                  by WolfAnto")
    print(Style.RESET_ALL)

    print("")
    print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
    print("")

    menu = int(input("""Enter 1 to start the program

Enter 2 to leave the program

Enter 3 to get info about the program

-----> """))
    print("")
    if menu == 1:
        print(Fore.RED + "Go to VALORANT.exe")
        print(Style.RESET_ALL)
        time.sleep(1)
        print("Step 1 : wait approximately 10 seconds when you are in Valorant")
        print("Step 2 : Don't move the mouse when you are in Valorant")
        print("Step 3 : If the program doesn't work, restart the program")
        print("")
        print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print("")
        time.sleep(5)
        a.lobby()

    if menu == 2:
        print("""    	    ████████████████████████████████                
  	  ██                                ██              
	██                                  ░░██            
	██    ██████    ██    ██  ████████    ██            
	██    ██    ██  ██    ██  ██          ██            
	██    ██████░░    ██████  ██████      ██            
	██    ██    ██        ██  ██          ██            
	██    ██████      ████    ████████    ██            
	██                                    ██            
  	  ██                                ██░░            
    	    ████████████████████████████████                
    	    ░░░░░░            ░░░░░░░░░░░░                  
""")
        print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(" ")
        time.sleep(2)

    if menu == 3:
    	print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
    	print("")
    	print("If you don't know how to use the program, check",Fore.GREEN + "README.md",Style.RESET_ALL + "in the folder")
    	print("Change the",Fore.GREEN +"ingame.png",Style.RESET_ALL + "in",Fore.GREEN + "1080 folder",Style.RESET_ALL + "| check",Fore.MAGENTA +"README.md",Style.RESET_ALL)
    	print("the program was created by",Fore.BLUE +"jordan123pal",Style.RESET_ALL +"and re-edited by",Fore.BLUE +"WolfAnto",Style.RESET_ALL +"for Valorant")
    	print("Low chance to get",Fore.RED +"ban",Style.RESET_ALL +"due to the Deatchmatch gamemode. Only by player reports")
    	print("The exp gain is quite slow due to the very long Deathmatch queue.",Fore.MAGENTA +"~900xp/15min",Style.RESET_ALL)
    	print("In 1 hour you can get",Fore.MAGENTA +"3600 exp",Style.RESET_ALL+"| 8 hours:",Fore.MAGENTA +"28 800exp",Style.RESET_ALL +"| 24 hours:",Fore.MAGENTA +"86 400 exp",Style.RESET_ALL)
    	print("the code is not optimised so may cause fps drops and crash after several hours")
    	print("If you encounter any difficulties during the installation or other contact me")
    	print(Fore.CYAN + "Discord: WolfAnto#5183","| ",Fore.YELLOW + "Github : https://github.com/WolfAnto",Style.RESET_ALL)
    	print("")
    	print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
    	time.sleep(999)


main()
