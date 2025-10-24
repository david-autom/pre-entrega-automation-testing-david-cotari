# tests/test_cart.py
from utils.helpers import BaseTest
from selenium.webdriver.common.by import By
import time


class TestCartFunctionality(BaseTest):

    def test_add_to_cart_and_verify(self):
        # Comprueba que funcione el carrito y se agreguen los productos
        self._login()
        driver = self.driver

        # 00. Almacenar el nombre del producto a agregar

        products_header = driver.find_element(By.CLASS_NAME, "inventory_item_name")
        producto_a_agregar = products_header.text.strip()
        #print ("Producto para agregar: ", producto_a_agregar, type(producto_a_agregar))
        
        # 01. Validar el botón agregar al carrito
        
        driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']").click()
        time.sleep(2)
        # 02. Validar el contador del carrito
        
        products_header = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        self.assertEqual("1", products_header.text)

        # 03. Validar que el carrito de compras esté presente
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # 04. Validar que el producto agregado esté en el carrito
        products_header = driver.find_element(By.CLASS_NAME, "inventory_item_name")
        producto_en_carrito = products_header.text.strip()
        #print ("Producto para agregado: ", producto_en_carrito, type(producto_en_carrito))
        self.assertEqual(producto_en_carrito, producto_a_agregar)

        time.sleep(2)