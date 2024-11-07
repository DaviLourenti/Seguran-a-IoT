from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty

class LoginScreen(Screen):
    username = ObjectProperty(None)
    password = ObjectProperty(None)

    def validate_credentials(self):
        # Simulação de validação de credenciais
        if self.username.text == "usuario" and self.password.text == "senha":
            self.manager.current = "main"
        else:
            # Aqui você pode adicionar uma mensagem de erro
            pass
