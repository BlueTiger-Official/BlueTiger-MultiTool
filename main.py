from Settings.config.config import *
from Settings.config.option import *

try:
    import requests
    import webbrowser
    import re
    import sys
    import fade
except ImportError:
    raise ImportError("Module not installed.")


try:
    new_version = re.search(r'version_tool\s*=\s*"([^"]+)"', requests.get(url_config).text).group(1)
    if new_version != version_tool:
        print(f"\033[92mINFO:\033[0m Please install the new version of the tool: \033[97m{version_tool}\033[91m -> \033[97m{new_version}")
        webbrowser.open(github_tool)
        input(f"\033[92mINFO:\033[0m Press Enter to still use this version -> ")
        popup_version = f"\033[91mNew Version: \033[97m{version_tool}\033[91m -> \033[97m{new_version}"
    else:
        popup_version = ""
except:
    popup_version = ""

def center_text(text):
    width = os.get_terminal_size().columns
    return '\n'.join(line.center(width) for line in text.split('\n'))

menu1 = fade.water(center_text("""\
╭───────────────────────────────────────────────────────────────────────╮
│                       BlueTiger - Tool Categories                     │
├───────────────────────────────────────────────────────────────────────┤
│                      Dev in Python 3.12 By Nkrz.dll                   │
│                                                                       │
│  [P] Paid                        -> Paid Menu.                        │
│  [L] Lookup/Search               -> Lookup menu.                      │
│                                                                       │
│  [N] Next Page                   -> Go to the next category.          │
│  [B] Previous Page               -> Go back to the previous category. │
│                                                                       │
╰───────────────────────────────────────────────────────────────────────╯
"""))

menu2 = fade.water(center_text(f"""
╭───────────────────────────────────────────────────────────────────────╮
│                     Discord Tools (Dsc)                               │
├───────────────────────────────────────────────────────────────────────┤
│  01: {format_option('01')}                                        │
│  03: {format_option('03')}                                            │
│  04: {format_option('04')}                                            │
│  06: {format_option('06')}                                            │
│  07: {format_option('07')}                                            │
│  08: {format_option('08')}                                            │
│  52: {format_option('52')}                                            │
│  53: {format_option('53')}                                            │
│  54: {format_option('54')}                                            │
│  55: {format_option('55')}                                            │
├───────────────────────────────────────────────────────────────────────┤
│  [N] Next Menu     [B] Previous Menu           [P] Paid Tools         │
╰───────────────────────────────────────────────────────────────────────╯
"""))

menu3 = fade.water(center_text(f"""
╭──────────────────────────────────────────────────────────────────────────────────╮
│                      Lookup/Search Tools                                         │
├──────────────────────────────────────────────────────────────────────────────────┤
│  09: {format_option('09')}                                                       │
│  10: {format_option('10')}                                                       │
│  11: {format_option('11')}                                                       │
│  12: {format_option('12')}                                                       │
│  13: {format_option('13')}                                                       │
│  14: {format_option('14')}                                                       │
│  17: {format_option('17')}                                                       │
│  18: {format_option('18')}                                                       │
│  19: {format_option('19')}                                                       │
│  20: {format_option('20')}                                                       │
│  21: {format_option('21')}                                                       │
│  23: {format_option('23')}                                                       │
│  24: {format_option('24')}                                                       │
│  32: {format_option('32')}                                                       │
│  34: {format_option('34')}                                                       │
├──────────────────────────────────────────────────────────────────────────────────┤
│  [N] Next Menu            [B] Previous Menu                  [P] Paid Tools      │
╰──────────────────────────────────────────────────────────────────────────────────╯
"""))

menu4 = fade.water(center_text(f"""
╭───────────────────────────────────────────────────────────────────────╮
│                     Scrapping/Tools Divers                            │
├───────────────────────────────────────────────────────────────────────┤
│  16: {format_option('16')}                                            │
│  25: {format_option('25')}                                        │
│  26: {format_option('26')}                                        │
│  31: {format_option('31')}                                            │
│  36: {format_option('36')}                                            │
│  37: {format_option('37')}                                            │
│  38: {format_option('38')}                                            │
│  39: {format_option('39')}                                            │
│  40: {format_option('40')}                                            │
│  41: {format_option('41')}                                            │
│  42: {format_option('42')}                                            │
│  43: {format_option('43')}                                            │
│  44: {format_option('44')}                                            │
│  45: {format_option('45')}                                            │
│  46: {format_option('46')}                                            │
│  47: {format_option('47')}                                            │
│  48: {format_option('48')}                                            │
│  49: {format_option('49')}                                            │
│  50: {format_option('50')}                                            │
│  51: {format_option('51')}                                            │
│  59: {format_option('59')}                                            │
├───────────────────────────────────────────────────────────────────────┤
│  [N] Next Menu       [B] Previous Menu            [P] Paid Tools      │
╰───────────────────────────────────────────────────────────────────────╯
"""))

menu5 = fade.water(center_text(f"""
╭───────────────────────────────────────────────────────────────────────╮
│                          Brute Force (Soviet)                         │
├───────────────────────────────────────────────────────────────────────┤
│  56: {format_option('56')}                                            │
│  57: {format_option('57')}                                            │
│  58: {format_option('58')}                                            │
├───────────────────────────────────────────────────────────────────────┤
│  [N] Next Menu       [B] Previous Menu            [P] Paid Tools      │
╰───────────────────────────────────────────────────────────────────────╯
"""))

menu6 = fade.water(center_text(f"""
╭─────────────────────────────────────────────────────────╮
│                     Paid Tools                          │
├─────────────────────────────────────────────────────────┤
│  27: {format_option('27')}                              │
│  28: {format_option('28')}                              │
│  29: {format_option('29')}                              │
│  30: {format_option('30')}                              │
├─────────────────────────────────────────────────────────┤
│  [N] Next Menu     [B] Previous Menu                    │
╰─────────────────────────────────────────────────────────╯
"""))


def Menu():
    try:
        menu_number = read_menu_state()  

        if menu_number == "1":
            menu = menu1
        elif menu_number == "2":
            menu = menu2
        elif menu_number == "3":
            menu = menu3
        elif menu_number == "4":
            menu = menu4
        elif menu_number == "5":
            menu = menu5
        elif menu_number == "6":
            menu = menu6
        else:
            menu = menu1
            menu_number = "1"

        banner = get_banner(menu)
        return banner, menu_number

    except Exception as e:
        Error(e)
        return menu1, "1"   

def display_prompt():
    Clear()
    banner, menu_number = Menu()
    faded_banner = fade.water(banner) 
    print(faded_banner)

    dark_blue = '\033[34m'  
    reset_color = '\033[0m'  

    prompt = f"┌───[{get_username()}@BlueTiger: Menu-{menu_number}]───[~]\n└──$ "
    colored_prompt = f"{dark_blue}{prompt}{reset_color}"  

    sys.stdout.write(colored_prompt)  
    sys.stdout.flush()  

while True:
    try:
        display_prompt()  
        choice = input().strip()  

        menu_number = read_menu_state()  

        if choice in ['N', 'n', 'NEXT', 'Next', 'next']:
            if menu_number == "1":
                write_menu_state("2")
            elif menu_number == "2":
                write_menu_state("3")
            elif menu_number == "3":
                write_menu_state("4")
            elif menu_number == "4":
                write_menu_state("5")
            elif menu_number == "5":
                write_menu_state("6")
            continue

        elif choice in ['B', 'b', 'BACK', 'Back', 'back']:
            if menu_number == "2":
                write_menu_state("1")
            elif menu_number == "3":
                write_menu_state("2")
            elif menu_number == "4":
                write_menu_state("3")
            elif menu_number == "5":
                write_menu_state("4")
            elif menu_number == "4":
                write_menu_state("5")             
            continue
        
        elif choice in ['P', 'p', 'Paid', 'paid']:
            write_menu_state("5")
            continue
            
        elif choice in ['L', 'l', 'Lookup', 'lookup']:
            write_menu_state("3")
            continue

        if choice in options:
            StartProgram(f"{options[choice]['script']}")
        elif '0' + choice in options:
            StartProgram(f"{options['0' + choice]['script']}")
        else:
            ErrorChoiceStart()

    except Exception as e:
        Error(e)
