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
    def odklikujka_Guzika(self):
        if(self.ids.naszguzik.selected == True):
            print("Guzik 1 nieaktywny")
        if (self.ids.naszguzik2.selected == True):
            print("Guzik 2 nieaktywny")
        if (self.ids.naszguzik3.selected == True):
            print("Guzik 3 nieaktywny")
        self.ids.naszguzik.selected = False
        self.ids.naszguzik2.selected = False
        self.ids.naszguzik3.selected = False

    def guzik_click(self):
        nastpepny_stan = not self.ids.naszguzik.selected
        self.odklikujka_Guzika()
        self.ids.naszguzik.selected = nastpepny_stan
        if(nastpepny_stan == True):
            print("Guzik 1 Aktywny")
        else:
            print("Guzik 1 nieaktywny")

    def guzik_click2(self):
        nastpepny_stan = not self.ids.naszguzik2.selected
        self.odklikujka_Guzika()
        self.ids.naszguzik2.selected = nastpepny_stan
        if (nastpepny_stan == True):
            print("Guzik 2 Aktywny")
        else:
            print("Guzik 2 nieaktywny")

    def guzik_click3(self):
        nastpepny_stan = not self.ids.naszguzik3.selected
        self.odklikujka_Guzika()
        self.ids.naszguzik3.selected = nastpepny_stan
        if(nastpepny_stan == True):
            print("Guzik 3 Aktywny")
        else:
            print("Guzik 3 nieaktywny")

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
