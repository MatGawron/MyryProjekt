from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.properties import BooleanProperty
from kivy.uix.textinput import TextInput
import random

class LED(Widget):
    SelectedLED = BooleanProperty(True)


class DefButton(Button):
    selected = BooleanProperty(False)


class Ring(Widget):
# Ustawianie wskaźnika dla Ringa. Od -90 do 90

    i = 10


class Interface(Widget):
    def ButtonClick1(LED):
        LED.ids.buttonLED1.SelectedLED = not LED.ids.buttonLED1.SelectedLED

    def ButtonClick2(LED):
        LED.ids.buttonLED2.SelectedLED = not LED.ids.buttonLED2.SelectedLED

    def ButtonClick3(LED):
        LED.ids.buttonLED3.SelectedLED = not LED.ids.buttonLED3.SelectedLED

    def ButtonClick4(LED):
        LED.ids.buttonLED4.SelectedLED = not LED.ids.buttonLED4.SelectedLED

    def ButtonClickLED(LED):
        # liczpa = random.randint(1, 5)
        # xx = "led"+str(liczpa)
        # print(type(xx))
         LED.ids.led2.SelectedLED = not LED.ids.led2.SelectedLED


class InterfaceApp(App):

    def build(self):
        return Interface()


InterfaceApp().run()
