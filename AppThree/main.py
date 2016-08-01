from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.label import Label

class Container(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        return Builder.load_file('appthree.kv')

    def popbox(self):
        popup = Popup(title='Confirm Action', content=Label(text='Hello world'), size_hint=(None, None), size=(400, 400))
        popup.open()

class AppThree(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def build(self):
        return Container()

if __name__=='__main__':
    AppThree().run()