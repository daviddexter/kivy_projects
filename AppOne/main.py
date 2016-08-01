from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import get_color_from_hex


class Container(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        return Builder.load_file('appone.kv')
    def update_label(self, *args):
        capital_label = self.ids['capital_label']
        capital_label.text = self.ids['textbox'].text.upper()

        lower_label = self.ids['lower_label']
        lower_label.text = self.ids['textbox'].text.lower()

        red_label = self.ids['red_label']
        red_label.color = get_color_from_hex('#f4433')

        green_label = self.ids['green_label']
        green_label.color = get_color_from_hex('#1de9b6')

        blue_label = self.ids['blue_label']
        blue_label.color = get_color_from_hex('#03a9f4')




class AppOne(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def build(self):
        return Container()

if __name__=='__main__':
    AppOne().run()
