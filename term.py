import os
import fade, art
from colorama import Fore, init

__mainAccent = f"{Fore.LIGHTBLUE_EX}"
__accent1 = f"{Fore.CYAN}"
__accent2 = f"{Fore.BLUE}"
__seperatorAccent = f"{Fore.WHITE}"

def printOptions(options:dict={"Test Option Without Info":"", "With Info":"Info"}, prompt:str=f"\n{__accent2}-->{__mainAccent} Choose{__seperatorAccent}:{__accent1} "):
    optionNum = 1
    for key in options:
        hasExtra = False
        option = options[key]
        if option != "": hasExtra = True

        if hasExtra: print(f"{__accent2}{optionNum}{__seperatorAccent}) {__mainAccent}{key}{__seperatorAccent}: {__accent1}{option}")
        else: print(f"{__accent2}{optionNum}{__seperatorAccent}) {__mainAccent}{key}{__seperatorAccent}")


        optionNum+=1


    if prompt != "":
        print(prompt, end="")
        return input()
def prompt(text:str=""):
    if text == "": print(f"\n{__accent2}-->{__mainAccent} Choose{__seperatorAccent}:{__accent1} ", end="")
    else: print(f"\n{__accent2}-->{__mainAccent} {text}{__seperatorAccent}:{__accent1} ", end="")
    return input()
def ask(text):
    print(text)
    print(f"\n{__accent2}-->{__mainAccent} y\\n{__seperatorAccent}:{__accent1} ", end="")
    out = input()

    if "y" in out.lower(): return True
    else: False

def cls(): os.system("cls" if os.name != 'posix' else quit())
def banner(text:str="NWRHook"):
    cls()
    print(fade.water(art.text2art(text)))
def alert(text:str="NWRHook"):
    cls()
    print(fade.fire(art.text2art(text)))

init()

.help
.h
!del