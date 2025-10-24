# tests/test_login.py
from utils.helpers import BaseTest
import time


class TestLoginValid(BaseTest):

    def test_valid_login(self):
        # Comprueba que el título sea correcto y que la autenticación funcione
        driver = self.driver

        # 01. Título correcto
        self.assertEqual("Swag Labs", driver.title)

        # 02. Iniciar sesión (usamos el helper)
        self._login()

        # 03. Verificar que cambió a la página de inventario
        self.assertIn("inventory.html", driver.current_url)

        time.sleep(3)
