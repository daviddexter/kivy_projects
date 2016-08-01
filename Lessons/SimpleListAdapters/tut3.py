from kivy.uix.boxlayout import BoxLayout
from kivy.base import runTouchApp
from kivy.lang import Builder

Builder.load_string(
'''
#:import Label kivy.uix.label.Label
#:import SimpleListAdapter kivy.adapters.simplelistadapter.SimpleListAdapter

<MyListView>:
    ListView:
        adapter:
            SimpleListAdapter(data=["item #{0}".format(num) for num in range(100)],cls=Label)

'''
)

class Container(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


if __name__=='__main__':
    runTouchApp(Container())