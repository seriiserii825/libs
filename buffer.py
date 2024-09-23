import os

def addToClipBoard(text):
    command = 'echo ' + text.strip() + '| xclip -selection clipboard'
    print(f"command: {command}")
    os.system(command)

def addToClipBoardFile(file):
    command = f"cat {file} | xclip -selection clipboard"
    print(command)
    os.system(command)

def getFromClipBoard():
    command = 'xclip -o -selection clipboard'
    print(f"command: {command}")
    return os.popen(command).read().strip()
