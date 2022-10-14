from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.properties import BooleanProperty
import random
from ctypes import windll, Structure, c_long, byref


class LED(Widget):
    SelectedLED = BooleanProperty(True)


class DefButton(Button):
    selected = BooleanProperty(False)


class Ring(Widget):
    pass


class Interface(Widget):
    def ButtonClick1(LED):
        LED.ids.buttonLED1.SelectedLED = not LED.ids.buttonLED1.SelectedLED

    def ButtonClick2(LED):
        LED.ids.buttonLED2.SelectedLED = not LED.ids.buttonLED2.SelectedLED

    def ButtonClick3(LED):
        LED.ids.buttonLED3.SelectedLED = not LED.ids.buttonLED3.SelectedLED

    def ButtonClickLED(LED):
        # liczpa = random.randint(1, 5)
        # xx = "led"+str(liczpa)
        # print(type(xx))
         LED.ids.led2.SelectedLED = not LED.ids.led2.SelectedLED


class InterfaceApp(App):

    def build(self):
        return Interface()


InterfaceApp().run()
