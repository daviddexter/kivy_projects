from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label

from datetime import datetime
import calendar
import sys

Builder.load_file('todo.kv')
class MainContainer(BoxLayout):
    screen_list = ListProperty([])
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def load_file(self):
        pass

    def quitapp(self):
        sys.exit()

    def change_screen(self):
        self.ids.app_screen_manager.current = "add_screen"
        self.screen_list.append('start_screen')

    def previous_screen(self):
        self.ids.app_screen_manager.current = self.screen_list.pop()

    def change_year_up(self):
        _cur_year = int(self.ids.add_screen.year.text)
        _new_year = _cur_year + 1
        self.ids.add_screen.year.text = str(_new_year)

    def change_year_down(self):
        _cur_year = int(self.ids.add_screen.year.text)
        _new_year = _cur_year - 1
        self.ids.add_screen.year.text = str(_new_year)

    def change_month_up(self):
        _cur_month = int(self.ids.add_screen.month.text)
        if _cur_month == 12:
            self.ids.add_screen.month.text = str(_cur_month)
        else:
            _new_month = _cur_month + 1
            self.ids.add_screen.month.text = str(_new_month)


    def change_month_down(self):
        _cur_month = int(self.ids.add_screen.month.text)
        if _cur_month == 1:
            self.ids.add_screen.month.text = str(_cur_month)
        else:
            _new_month = _cur_month - 1
            self.ids.add_screen.month.text = str(_new_month)

    def change_day_up(self):
        pass

    def change_day_down(self):
        pass

    def save_item(self):
        _item = self.ids.add_screen.activity.text
        if _item == '':
            pop = Popup(title='Error saving',
                        content=Label(text="Cannot save empty activity"),
                        size_hint=(None, None), size=(self.width/2, self.height/2), on_dismiss=self.close_dialog)
            pop.open()
        else:
            print(_item)
    def close_dialog(self, *args):
        return self.previous_screen()

class MainRoot(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def build(self):
        return MainContainer()

if __name__=='__main__':
    MainRoot().run()