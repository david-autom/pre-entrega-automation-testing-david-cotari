# tests/helpers.py
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class BaseTest(unittest.TestCase):
    """Clase padre que contiene setUp/tearDown y el helper de login."""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        # `close()` solo cierra la ventana activa; `quit()` termina el proceso.
        self.driver.quit()

    def _login(self):
        """Entra a la aplicación con las credenciales estándar."""
        driver = self.driver
        # usuario
        driver.find_element(By.ID, "user-name").send_keys("standard_user", Keys.TAB)
        # contraseña
        driver.find_element(By.ID, "password").send_keys("secret_sauce", Keys.TAB)
         # botón login
        driver.find_element(By.ID, "login-button").click()
