#needs Pillow, pyautogui, and numpy to work
from PIL import ImageGrab, ImageOps
import pyautogui
from numpy import *

class Coords():
    reactbutton = (311, 204)

def restartGame():
    pyautogui.click(Coords.reactbutton)

def imageGrab():
    box = (Coords.reactbutton[0] + 74, Coords.reactbutton[1], Coords.reactbutton[0] + 100, Coords.reactbutton[1] + 30)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    print(a.sum())
    return(a.sum())

def click():
    pyautogui.click(Coords.reactbutton)

def check():
    while True:
        if(imageGrab() != 870 and imageGrab() != 895):
            click()

check()