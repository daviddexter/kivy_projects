from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty,StringProperty
from kivy.uix.screenmanager import Screen

import webbrowser
import sys
from calculation import Calculation



class KivyTutorRoot(BoxLayout):
    screen_list = ListProperty([])
    sign = StringProperty(None)
    items_list = ListProperty([])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


    def changeScreen(self,next_screen):

        if next_screen == 'about this app':
            self.ids.kivy_screen_manager.current = "about_screen"
            self.screen_list.append('start_screen')
        else:
            self.math_screen.operation_text.text = next_screen.capitalize()
            self.ids.kivy_screen_manager.current = "math_screen"
            self.math_screen.question_text.text = ""
            self.math_screen.input_text.text = ""
            self.math_screen.answer_text.text = ""
            self.screen_list.append('start_screen')

    def previousScreen(self):
        go_to = self.screen_list.pop()
        self.ids.kivy_screen_manager.current = go_to

    def add_text(self, number):
        previousInput = self.math_screen.input_text.text
        self.math_screen.input_text.text = previousInput + number

    def proceed_operation(self):
        _operations = {
            "addition":"+",
            "subtraction":"-",
            "multiplication":"*",
            "division":"/"
        }
        operationText = self.math_screen.operation_text.text
        if operationText.lower() in _operations.keys():
            self.sign = _operations[operationText.lower()]
        Input = self.math_screen.input_text.text
        previousNum = self.math_screen.question_text.text
        if previousNum == '':
            self.math_screen.question_text.text = Input
            self.math_screen.input_text.text = " "
        else:
            self.math_screen.question_text.text = self.math_screen.question_text.text + ' ' + self.sign + ' ' + Input
            self.math_screen.input_text.text = " "

    def get_answer(self):
        _operations = {
            "addition":"+",
            "subtraction":"-",
            "multiplication":"*",
            "division":"/"
        }
        operationText = self.math_screen.operation_text.text.lower()
        if operationText in _operations.keys():
            self.sign = _operations[operationText]

        question = self.math_screen.question_text.text.split(self.sign)
        for i in question:
            self.items_list.append(int(i))
        math = Calculation(operationText,self.items_list)
        result = math.do_calculation()
        self.math_screen.answer_text.text = result
        self.math_screen.question_text.text = ''


    def clear(self):
        self.math_screen.question_text.text = ''
        self.math_screen.input_text.text = ''
        self.math_screen.answer_text.text = ''


class MathScreen(Screen):
	"""docstring for MathScreen"""
	def __init__(self, *args, **kwargs):
		super(MathScreen, self).__init__(*args, **kwargs)
		
		

class KivyTutorApp(App):
    def __int__(self, **kwargs):
        super().__init__(**kwargs)


    def build(self):
        return KivyTutorRoot()

    def getText(self):
        return ("Built using"
    		  	"[b][ref=kivy] Kivy version 1.9.1[/ref][/b]  "
    		  	"Visit Kivy Project Here :"
    		  	"[b][ref=webiste] kivy.org[/ref][/b]")

    def on_ref_press(self,instance,ref):
        _dict = {"kivy": "https://kivy.org", "webiste": "https://kivy.org"}
        webbrowser.open(_dict[ref])

    def quit_app(self):
        sys.exit()
    		  	 
if __name__=='__main__':
    KivyTutorApp().run()