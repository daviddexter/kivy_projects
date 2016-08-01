from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.lang import Builder
from kivy.properties import ListProperty
import sys

class Container(AnchorLayout):

    pactiveScreen = ListProperty([])

    def __int__(self, **kwargs):
        super().__init__(**kwargs)
        return Builder.load_file('apptwo.kv')

    def go_to_app(self):
        self.pactiveScreen.append('startscreen')
        self.ids.screen_manager.current = 'appscreen'

    def go_back(self):
        previousScreen = self.pactiveScreen.pop()
        self.ids.screen_manager.current = previousScreen

    def close_app(self):
        sys.exit()


class AppTwo(App):
    def __int__(self, **kwargs):
        super().__init__(**kwargs)
    def build(self):
        return Container()

if __name__=='__main__':
    AppTwo().run()

