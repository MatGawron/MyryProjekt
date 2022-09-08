from kivy.app import App
from kivy.uix.widget import Widget
from ctypes import windll, Structure, c_long, byref
import time



class MojeWidgety(Widget):
    #def on_touch_move(self, touch):
    pass




class MyryProgram(App):
    pass


class Cursor():
    now = time.time()
    future = now + 10000
    while time.time() < future:
        class POINT(Structure):
            _fields_ = [("x", c_long), ("y", c_long)]


        def queryMousePosition():
            pt = POINT()
            windll.user32.GetCursorPos(byref(pt))
            return {"x": pt.x, "y": pt.y}


        pos = queryMousePosition()
        print(pos)

MyryProgram().run()
