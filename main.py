from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.properties import BooleanProperty
from ctypes import windll, Structure, c_long, byref


class GuzikWyglad(Button):
    selected = BooleanProperty(False)
class Interface(Widget):
    def odklikujka_Guzika(self):
        self.ids.naszguzik.selected = False
        self.ids.naszguzik2.selected = False
        self.ids.naszguzik3.selected = False
    def guzik_click(self):
        nastpepny_stan = not self.ids.naszguzik.selected
        self.odklikujka_Guzika()
        self.ids.naszguzik.selected = nastpepny_stan
        print("gUZIK  W k l i k n i e n t y")
    def guzik_click(self):
        nastpepny_stan = not self.ids.naszguzik2.selected
        self.odklikujka_Guzika()
        self.ids.naszguzik2.selected = nastpepny_stan
        print("guz2  W k l i k n i e n t y")
    def guzik_click(self):
        nastpepny_stan = not self.ids.naszguzik3.selected
        self.odklikujka_Guzika()
        self.ids.naszguzik3.selected = nastpepny_stan
        print("guz3  W k l i k n i e n t y")

class InterfaceApp(App):

    def build(self):
        return Interface()

InterfaceApp().run()