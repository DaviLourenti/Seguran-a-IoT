from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty

class ItemDetailScreen(Screen):
    item_name = StringProperty("")
    item_category = StringProperty("")

    def on_pre_enter(self):
        # Configura as especificações do item
        self.ids.item_label.text = f"Especificações do {self.item_name}\nCategoria: {self.item_category}"
        # Aqui você pode adicionar mais detalhes específicos do item

    def create_item_widget(self, item_name, category):
        from widgets.item_widget import ItemWidget
        return ItemWidget(text=item_name, category=category)

    