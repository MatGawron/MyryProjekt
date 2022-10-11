from kivy.app import App
from kivy.uix.widget import Widget
from ctypes import windll, Structure, c_long, byref

import GuzikWyglad

class Interface(Widget):
    def guzik_dul(self):
        print("gUZIK  W dole ")

class InterfaceApp(App):

    def build(self):
        return Interface()

InterfaceApp().run()