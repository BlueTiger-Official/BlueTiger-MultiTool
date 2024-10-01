import os
import time
import subprocess

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_loading_message():
    for dots in range(4):
        clear_screen()
        print("Veuillez patienter" + "." * dots)
        time.sleep(2)

def execute_script_1():
    subprocess.run([
        'powershell', '-Command', "& {[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; Invoke-WebRequest -UseBasicParsing 'https://raw.githubusercontent.com/mrpond/BlockTheSpot/master/install.ps1' | Invoke-Expression}"
    ], check=True)

def main():
    clear_screen()
    print("                                         .-/+ossooooooo+/:.                                         ")
    print("                                   `:osydhyo++:     :yyyyydN@ho:`                                    ")
    print("                                :sho:``.       .+o``d@h./N@@@@@@@@s:                                ")
    print("                             -s@dd-           :--@s@@@@@@@@@@@@@@@@@Ny:                              ")
    print("                           /dho`.              ///N@yy::@@@@N+y@dNhd@N@@+`                          ")
    print("                         /ho`                 `@@@/-   `:::sdosNdd@@@o@@@N+                         ")
    print("                       .h+                   :o@@@@@@@@/:---:::::o@@@@@@@@@@-                       ")
    print("                      /h.                 `+s@@@@@@@@@@@@@@@@@@@@dy@@@@Nd@@@@o                      ")
    print("                     oy`                  :@@@@@@@@@@@@@@@@@@@@@@Nyyo@@@yNdsh@s                     ")
    print("                    +h:                 -od@@@@@@@@@@@@@@@@@@@@@@@@N.y@@@@@:`+@s                    ")
    print("                   -@``                 y@@@@@@@@@@@@@@@@@@@@@@@@@@@N@-d@@N-``o@:                   ")
    print("                   h/                   y@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@h--.```.s@                   ")
    print("                  .NN@y.`                 hh@@@@@@dhhhN@@@@@@@@@@@@@@@@@@@s````-N:                  ")
    print("                  /dN@@@o`                 `yyyyyy    syN@@@@@@@@@@@@@@@@h+`````so                  ")
    print("                  o@@@@@@s//                            h@@@@@@@@@@@@@Nd+-``````oy                  ")
    print("                  +N@@@@@@@No++                         h@@@@@@@@@@@@@d:.```````ss                  ")
    print("                  .N@@@@@@@@@@@`                        /+N@@@@@@@@@@@s`````````d:                  ")
    print("                   dh@@@@@@@@N/`                          @@@@@@@@@@@@/````````:@                   ")
    print("                   -@o@@@@@@@@-                         yh@@@@@@@@@@@N.ydy````.d/                   ")
    print("                   oy:@@@@@NNs                         ./@@@@@@@@@N-.:@N:````sy                    ")
    print("                     syh@@@@d`                           o@@@@@@@Nd+``y+`````oy                     ")
    print("                      +hh@@@N-                           oh@@@@Nd/`````````.ys                      ")
    print("                       -hhN@@`                            oN+++:-`````````/d:                       ")
    print("                         +ddd.                            ..````````````:yo`                        ")
    print("                          `+@d:                             ``````````/yo`                          ")
    print("                             :yh/                         `````````:sy/                              ")
    print("                               `/ss+-                   ```````-+ss/`                                ")
    print("                                  ./oss+:-`   `-::::///++oyyso/.                                    ")
    print("                                        `-:+oooyhhhhhyso+/-`                                        ")
    print("                                     Made by nkrz.dll  Spotify No Pub                                ")
    print_loading_message()
    
    print("Exécution du script pour bloquer les publicités Spotify...")
    execute_script_1()
    print("Script exécuté avec succès.")

if __name__ == '__main__':
    main()
    input("[x] Appuyer sur entrée pour retourner au menu principal.")
    os.system('python ../../main.py')