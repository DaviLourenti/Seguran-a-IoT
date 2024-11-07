from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty
from kivy.app import App

class ItemWidget(BoxLayout):
    text = StringProperty("")
    category = StringProperty("")
    text_color = ListProperty([0, 0, 0, 1])  # Cor padrão: preto

    def view_details(self):
        # Navega para a tela de detalhes do item
        app = App.get_running_app()
        detail_screen = app.root.get_screen('item_detail')
        detail_screen.item_name = self.text
        detail_screen.item_category = self.category
        app.root.current = 'item_detail'
