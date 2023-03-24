import os
import term
from colorama import Fore, Back
import rich

class Config():
    exists = False
    baseplate = {"fileEditing":""}

    def readCFG(self) -> dict:
        try: return eval(open("config.json", "r").read())
        except: return False
    def writeCFG(self, config:dict) -> bool:
        try: open("config.json", "+w").write(str(config))
        except Exception: pass

    def __init__(self) -> None:
        cfg = self.readCFG()
        if not cfg: return

        if os.path.exists("config.json"): self.exists = True

class File():
    name = ""
    content = ""

    def getContent(self):
        if os.path.exists(self.name): self.content = open(self.name, "r").read()
        else: return False
        return True
    def setContent(self):
        if os.path.exists(self.name): self.content = open(self.name, "w").write(self.content)
    def __init__(self) -> None:
        if os.path.exists(self.name): self.content = open(self.name, "r").read()
        else: pass

config = Config()

def load():
    filename = ""

    if not config.exists:
        term.alert("NO  CONFIG")
        createConfig = term.ask(f"{term.Fore.RED}There is no config, do you want to create one?")
        if not createConfig:
            term.alert("QUITTING")
            term.prompt("Without a config you cannot use this program.")
            quit()
        config.writeCFG(config.baseplate)

    if config.readCFG()['fileEditing'] == '':
        term.banner("NVREditor")

        files = os.listdir(os.getcwd())
        filesDictionary = {}

        for file in files:
            if os.path.isfile(file): filesDictionary.update({file:""})
        
        fileSelected = term.printOptions(filesDictionary)

        try: fileSelected = int(fileSelected)
        except: return


        tempFiles = []
        if type(fileSelected) == int:
            for i in range(len(files)):
                if os.path.isfile(files[i]): tempFiles.append(files[i])
        for i in range(len(tempFiles)):
            if i == fileSelected-1:
                filename = tempFiles[i]
        

        cfg = config.baseplate
        cfg['fileEditing'] = filename
        config.writeCFG(cfg)
def main():
    load()
    cfg = config.readCFG()
    filename = cfg['fileEditing']

    if not os.path.exists(filename): open(filename, "+w")

    file = File()
    file.name = filename
    while True:
        cfg = config.readCFG()
        filename = cfg['fileEditing']

        if not os.path.exists(filename): open(filename, "+w")

        file = File()
        file.name = filename

        term.cls()
        file.getContent()

        content = file.content.splitlines()
        lineNum = 1
        
        editingText = f"{Fore.LIGHTBLUE_EX}Editing {Fore.RED}- {Back.WHITE}{Fore.BLACK}{file.name}{Back.BLACK}{Fore.WHITE}"
        print(" "*((rich.get_console().width//2)-(len(editingText)//3)) + editingText)

        for line in content:
            print(f"{Fore.LIGHTBLUE_EX}{lineNum}{' '*(len(str(content.index(content[-1])+1))-len(str(lineNum)))}{Fore.WHITE}) {Fore.LIGHTBLUE_EX}-{Fore.WHITE} ", end="")
            rich.get_console().print(line)
            lineNum+=1

        print(f"{Fore.LIGHTBLUE_EX}{lineNum}{' '*(len(str(content.index(content[-1])+1))-len(str(lineNum)))}{Fore.WHITE}) {Fore.LIGHTBLUE_EX}-{Fore.WHITE} ", end="")
        newLine = input()
        
        if newLine.startswith(".del"):
            splitLine = newLine.split(" ")
            splitLine.remove(splitLine[0])
            try:
                if splitLine[0] != "":
                    delLine = int(splitLine[0])-1
                    content.remove(content[delLine])
                else: content.remove(content[-1])
            except: pass
        elif newLine.startswith(".repl"):
            splitLine = newLine.split(" ")
            splitLine.remove(splitLine[0])
            replLine = int(splitLine[0])-1
            replText = " ".join(splitLine[1:])
            content[replLine] = replText
        elif newLine.startswith(".insert"):
            splitLine = newLine.split(" ")
            splitLine.remove(splitLine[0])
            insLine = int(splitLine[0])-1
            insText = " ".join(splitLine[1:])
            content.insert(insLine, insText)
        elif newLine.startswith(".back"):
            config.writeCFG({'fileEditing':''})
            load()
        else:
            if newLine == "": content.append("\n")
            else: content.append(newLine)

        file.content = "\n".join(content)
        file.setContent()







main()