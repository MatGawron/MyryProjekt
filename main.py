from kivy.app import App
from kivy.uix.widget import Widget
from ctypes import windll, Structure, c_long, byref
import time

class Interface(Widget):
    def guzik_dul(self):
        print("gUZIK  W dole ")

class InterfaceApp(App):

    def build(self):
        return Interface()


class MojeWidgety(Widget):
    def on_touch_down(self, touch):
        touch.grab(self)
        posX = queryMousePositionX()
        posY = queryMousePositionY()
        print(posY, posX)




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




InterfaceApp().run()
MyryProgram().run()
#from kivy.app import App
#from kivy.uix.widget import Widget

