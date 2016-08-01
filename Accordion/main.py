from kivy.uix.anchorlayout import AnchorLayout
from kivy.app import App
from kivy.lang import Builder

class Container(AnchorLayout):
    def __int__(self, **kwargs):
        super().__init__(**kwargs)
        presentation = Builder.load_file('accordion.kv')
        return presentation

class Accordion(App):
    def __int__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        return Container()

if __name__=='__main__':
    Accordion().run()


