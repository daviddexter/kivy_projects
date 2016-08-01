from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout


Builder.load_file("VideoPlayer.kv")
class MainContainer(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(*kwargs)



class  VideoPlayerApp(App):
    def __int__(self,**kwargs):
        super().__init__(**kwargs)

    def build(self):
        return  MainContainer()

if __name__== "__main__" :
    VideoPlayerApp().run()
