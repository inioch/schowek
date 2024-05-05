import keyboard
import pyperclip

lastClipboard = []
isEnabled = True
textInput = ""

def handleEvent():
    global textInput
    textInput = pyperclip.paste()
    lastClipboard.append(textInput)

def resetArray():
    lastClipboard.clear()

keyboard.add_hotkey('ctrl+q', handleEvent)

keyboard.wait('esc')