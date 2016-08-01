from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.lang import Builder
from dbase import dbAccess
import os

Builder.load_file('todo.kv')
class Container(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        _curFolder = os.getcwd()
        index = dbAccess(_curFolder)
        items = index.accessDb()

        #self.add_widget(ItemsWidget())


class ItemsWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class ToDoRoot(App):
    def __int__(self, **kwargs):
        super().__init__(**kwargs)
    def build(self):
        return Container()

if __name__=='__main__':
    ToDoRoot().run()
