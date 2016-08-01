from kivy.app import App
from kivy.adapters.simplelistadapter import SimpleListAdapter
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty
from kivy.uix.listview import ListView

class MyWidget(Widget):
    mylist = ListProperty(['dexter', 'lis', 'jeff'])
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        SimpleListAdapter(data=self.mylist, cls=ListView.ListItemButton)

'''
class MyLayout(ListView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        btn = ListView.ListItemButton()
        return btn
'''

class App(App):
    def build(self):
        return Widget()

if __name__ == '__main__':
    App().run()