from termcolor import colored
from prettytable import PrettyTable
from webbrowser import open


def banner():
    banner = """  ________         __  __           __                  ____             _     
 /_  __/ /_  ___  / / / /___ ______/ /_____  __________/ __ )_________ _(_)___ 
  / / / __ \/ _ \/ /_/ / __ `/ ___/ //_/ _ \/ ___/ ___/ __  / ___/ __ `/ / __ \\
 / / / / / /  __/ __  / /_/ / /__/ ,< /  __/ /  (__  ) /_/ / /  / /_/ / / / / /
/_/ /_/ /_/\___/_/ /_/\__,_/\___/_/|_|\___/_/  /____/_____/_/   \__,_/_/_/ /_/ 
                        \n"""
    tagline = "Ethical Hacker, Programmer & FreeLancer"
    print(f"{colored(banner, 'green')}                   {tagline}\n")


def about():
    table = PrettyTable()
    abt = "Hey There, My Name is Gaurav Raj. \nAn Ethical Hacker, Programmer & FreeLancer. Mostly in System Hacker. \nDo Software Development, Android/IOS Apps Development and as well as Web Apps Development."
    table.field_names = ['About Me']
    table.add_row([abt])
    print(f"{table}\n")


def menu():
    print(f"[{colored('01', 'green')}] GitHub")
    print(f"[{colored('02', 'green')}] Blog | WebSite")
    print(f"[{colored('03', 'green')}] Projects")
    print(f"[{colored('04', 'green')}] Social")
    print(f"[{colored('05', 'green')}] More About\n")
    opt = input(f"{colored('thehackersbrain$', 'green')} ")

    if opt == "1" or opt == "01":
        print("Opening GitHub Profile in Firefox")
        open('https://github.com/thehackersbrain')
    elif opt == "2" or opt == "02":
        print("Opening https://thehackersbrain.pythonanywhere.com/")
        open('https://thehackersbrain.pythonanywhere.com/')
    elif opt == "3" or opt == "03":
        print("Open All GitHub Projects")
        open('https://github.com/thehackersbrain?tab=repositories')
    elif opt == "4" or opt == "04":
        print("Opening Social Profiles")
        open('https://thehackersbrain.github.io')
    elif opt == "5" or opt == "05":
        print("Showing More About Me")
        open('https://thehackersbrain.pythonanywhere.com/about')
    elif opt == "exit" or opt == "exit":
        exit()
    else:
        print("Invalid Command, Try Again...")
        exit()


if __name__ == "__main__":
    try:
        banner()
        about()
        menu()
    except Exception as err:
        print()
    except KeyboardInterrupt as keyerr:
        print(" Keyboard Interrupt Detected. Terminating Program.")
