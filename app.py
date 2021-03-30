
import pyperclip
import win32clipboard
from pynput import keyboard
import pyautogui as pya
import time

def copy_clipboard():
    pya.hotkey('ctrl', 'c')
    # ctrl-c is usually very fast but your program may execute faster
    time.sleep(.01)
    return pyperclip.paste()


EngQurty = {
    "q": 1,
    "w": 2,
    "e": 3,
    "r": 4,
    "t": 5,
    "y": 6,
    "u": 7,
    "i": 8,
    "o": 9,
    "p": 10,
    "[": 11,
    "]": 12,
    "a": 13,
    "s": 14,
    "d": 15,
    "f": 16,
    "g": 17,
    "h": 18,
    "j": 19,
    "k": 20,
    "l": 21,
    ";": 22,
    "'": 23,
    "z": 24,
    "x": 25,
    "c": 26,
    "v": 27,
    "b": 28,
    "n": 29,
    "m": 30,
    ",": 31,
    ".": 32,
    "/": 33,
}


HebQurty = {
    "/": 1,
    "'": 2,
    "ק": 3,
    "ר": 4,
    "א": 5,
    "ט": 6,
    "ו": 7,
    "ן": 8,
    "ם": 9,
    "פ": 10,
    "]": 11,
    "[": 12,
    "ש": 13,
    "ד": 14,
    "ג": 15,
    "כ": 16,
    "ע": 17,
    "י": 18,
    "ח": 19,
    "ל": 20,
    "ך": 21,
    "ף": 22,
    ",": 23,
    "ז": 24,
    "ס": 25,
    "ב": 26,
    "ה": 27,
    "נ": 28,
    "מ": 29,
    "צ": 30,
    "ת": 31,
    "ץ": 32,
    ".": 33,
}

def swapToHeb(text):
    # ---------------------------------------#
    res = ""
    for letter in text:
        if str(letter).lower() in EngQurty:
            index = EngQurty[str(letter).lower()]
            for key in HebQurty:
                if index == HebQurty[key]:
                    res += key
        else:
            res += letter

    return res

def swapToEng(text):
    # ---------------------------------------#
    res = ""
    for letter in text:
        if letter in HebQurty:
            index = HebQurty[letter]
            for otherLangLetter in EngQurty:
                if index == EngQurty[otherLangLetter]:
                    res += otherLangLetter
        else:
            res += letter

    return res

def swap(text):
    # ----------------detect lang-----------------------#
    if str(text[0]).isascii():
        text = swapToHeb(text) # is eng
    else:
        text = swapToEng(text) # is heb

    return text
        
def copy(text):
    # --------------place text in clipboard-------------------------#
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(text, win32clipboard.CF_UNICODETEXT)
    win32clipboard.CloseClipboard()

def paste():
    # -----------------get text from clipboard----------------------#
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData(win32clipboard.CF_UNICODETEXT)
    win32clipboard.CloseClipboard()
    return data

def placeInPlace():
    pya.hotkey('ctrl', 'v')

def getclipboard():
    # double clicks on a position of the cursor
    pya.doubleClick(pya.position())
    pya.click(pya.position())

    text = (swap(text=copy_clipboard()))
    try: text = text.decode('utf8')
    except AttributeError: pass
    print("%r" % text.encode('utf8'))
    copy(text)
    time.sleep(0.1)
    placeInPlace()


if __name__ == "__main__": 
    # ---------------set hotkeys------------------------#
    with keyboard.GlobalHotKeys({
        '<ctrl>+<alt>+o': getclipboard,
        '<ctrl>+<alt>+ם': getclipboard}) as h:h.join()






