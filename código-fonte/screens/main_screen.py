from kivy.uix.screenmanager import Screen
from kivy.properties import ListProperty
from kivy.clock import Clock

class MainScreen(Screen):
    # Listas para armazenar os itens de cada categoria
    janelas_items = ListProperty(["IoT_Janela 1", "IoT_Janela 2"])
    portas_items = ListProperty(["IoT_Porta 1", "IoT_Porta 2"])
    cameras_items = ListProperty(["IoT_Camera 1", "IoT_Camera 2"])

    def on_pre_enter(self):
        # Popula todos os itens ao entrar na tela
        Clock.schedule_once(self.populate_all_items)

    def populate_all_items(self, dt):
        for category in ['janelas', 'portas', 'cameras']:
            self.update_items(category)

    def add_item(self, category):
        if category == 'janelas':
            new_item = f"IoT_Janela {len(self.janelas_items) + 1}"
            self.janelas_items.append(new_item)
        elif category == 'portas':
            new_item = f"IoT_Porta {len(self.portas_items) + 1}"
            self.portas_items.append(new_item)
        elif category == 'cameras':
            new_item = f"IoT_Camera {len(self.cameras_items) + 1}"
            self.cameras_items.append(new_item)
        self.update_items(category)

    def update_items(self, category):
        container = self.ids.get(f"{category}_container")
        if container:
            container.clear_widgets()
            self.populate_items(category)
            container.height = container.minimum_height
            # Atualiza a altura do BoxLayout da divisória
            boxlayout = container.parent
            boxlayout.height = boxlayout.minimum_height

    def populate_items(self, category):
        if category == 'janelas':
            items = self.janelas_items
        elif category == 'portas':
            items = self.portas_items
        elif category == 'cameras':
            items = self.cameras_items

        container = self.ids.get(f"{category}_container")
        for item in items:
            item_widget = self.manager.get_screen('item_detail').create_item_widget(item, category)
            container.add_widget(item_widget)
