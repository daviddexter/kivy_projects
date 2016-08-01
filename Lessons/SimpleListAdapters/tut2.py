from kivy.uix.boxlayout import BoxLayout
from kivy.uix.listview import ListView
from kivy.uix.label import Label
from kivy.base import runTouchApp
from kivy.adapters.simplelistadapter import SimpleListAdapter

class Container(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        simple_list = SimpleListAdapter(data=["item #{0}".format(num) for num in range(1,100)], cls=Label)
        list_view = ListView(adapter=simple_list)
        self.add_widget(list_view)



if __name__=='__main__':
    runTouchApp(Container())