# import os
# os.environ['KIVY_METRICS_DENSITY'] = '1'
# os.environ['KIVY_NO_CONSOLELOG'] = '1'
# os.environ['KIVY_WINDOW'] = 'mock'

# main.py
from kivy.app import App # type: ignore
from kivy.lang import Builder # type: ignore
from kivy.uix.screenmanager import ScreenManager, Screen # type: ignore

# Definindo a classe WindowManager como o gerenciador de telas
class WindowManager(ScreenManager):
    pass

# Importar as telas
from screens.login_screen import LoginScreen
from screens.main_screen import MainScreen
from screens.item_detail_screen import ItemDetailScreen
from widgets.item_widget import ItemWidget

# Carregar arquivos KV
Builder.load_file('app.kv')
Builder.load_file('screens/login_screen.kv')
Builder.load_file('screens/main_screen.kv')
Builder.load_file('screens/item_detail_screen.kv')
Builder.load_file('widgets/item_widget.kv') 

class MyApp(App):
    def build(self):
        wm = WindowManager()
        wm.add_widget(LoginScreen(name="login"))
        wm.add_widget(MainScreen(name="main"))
        wm.add_widget(ItemDetailScreen(name="item_detail"))
        wm.current = "login"  # Define a tela inicial
        return wm

if __name__ == "__main__":
    MyApp().run()