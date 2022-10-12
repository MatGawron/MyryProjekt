from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.properties import BooleanProperty
import random
from ctypes import windll, Structure, c_long, byref

class LED(Widget):
    ledzik = BooleanProperty(True)

class GuzikWyglad(Button):
    selected = BooleanProperty(False)

class Interface(Widget):
    def guzik_click(LED):
        LED.ids.ledguzik1.ledzik = not LED.ids.ledguzik1.ledzik

    def guzik_click2(LED):
        LED.ids.ledguzik2.ledzik = not LED.ids.ledguzik2.ledzik

    def guzik_click3(LED):
        LED.ids.ledguzik3.ledzik = not LED.ids.ledguzik3.ledzik


    def guzik_clickLED(LED):
       # liczpa = random.randint(1, 5)
       # xx = "led"+str(liczpa)
       # print(type(xx))
        ledzikk = not LED.ids.led2.ledzik
        LED.ids.led2.ledzik = ledzikk


class InterfaceApp(App):

    def build(self):
        return Interface()


InterfaceApp().run()
