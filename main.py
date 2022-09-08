from kivy.app import App
from kivy.uix.widget import Widget
from ctypes import windll, Structure, c_long, byref
import time

class MojeWidgety(Widget):
    pass

class MyryProgram(App):
    pass



class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]


def queryMousePositionX():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return {pt.x}

def queryMousePositionY():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return {pt.y}

posX = queryMousePositionX()
posY = queryMousePositionY()
print(posX,posY)

MyryProgram().run()
