from kivy.storage.jsonstore import JsonStore
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Root(BoxLayout):
    def __int__(self, **kwargs):
        super().__init__(**kwargs)
        store = JsonStore('hello.json')
        #put some values
        store.put('tito', name='Mathieu', org='kivy')
        store.put('tshirtman', name='Gabriel', age=27)
        store.put('tito', name='Mathieu', age=30)

        print('tito is', store.get('tito')['age'])


class MyMain(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        return Root()

if __name__=='__main__':
    MyMain().run()
