from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.config import Config

Config.set('graphics', 'width', '640')
Config.set('graphics', 'height', '480')



class MakeScreen(GridLayout):
    
    def __init__(self, **kwargs):
        super(MakeScreen, self).__init__(**kwargs)
        self.cols = 1
        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)


class MyApp(App):
    def build(self):
        return MakeScreen()
if __name__ == '__main__':
    MyApp().run()
    
