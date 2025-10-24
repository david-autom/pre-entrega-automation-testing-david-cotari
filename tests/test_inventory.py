# tests/test_inventory.py
from utils.helpers import BaseTest
from selenium.webdriver.common.by import By
import time


class TestInventoryView(BaseTest):

    def test_view_inventary(self):
        #Comprueba que la vista de inventario muestra todos los productos
        self._login()
        driver = self.driver

        # 01. Validar que el encabezado “Products” esté presente
        products_header = driver.find_element(By.CLASS_NAME, "title")
        self.assertEqual("Products", products_header.text)

        # 02. Validar que el menú hamburguesa esté presente
        products_header = driver.find_element(By.CLASS_NAME, "bm-burger-button")
        self.assertIs(products_header.is_displayed(), True)

        # 03. Validar que el carrito de compras esté presente
        products_header = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        self.assertIs(products_header.is_displayed(), True)

        # 04. Validar que el menú de ordenamiento esté presente
        products_header = driver.find_element(By.CLASS_NAME, "product_sort_container")
        self.assertIs(products_header.is_displayed(), True)

        # 05. Validar las imágenes de los productos #

        buscar_por_xpath = driver.find_element(By.XPATH, "//img[@alt='Sauce Labs Bike Light']")
        self.assertTrue(buscar_por_xpath.is_displayed())

        buscar_por_xpath = driver.find_element(By.XPATH, "//img[@alt='Sauce Labs Bolt T-Shirt']")
        self.assertTrue(buscar_por_xpath.is_displayed())

        buscar_por_xpath = driver.find_element(By.XPATH, "//img[@alt='Sauce Labs Onesie']")
        self.assertTrue(buscar_por_xpath.is_displayed())

        buscar_por_xpath = driver.find_element(By.XPATH, "//img[@alt='Sauce Labs Fleece Jacket']")
        self.assertTrue(buscar_por_xpath.is_displayed())

        buscar_por_xpath = driver.find_element(By.XPATH, "//img[@alt='Sauce Labs Bike Light']")
        self.assertTrue(buscar_por_xpath.is_displayed())

        # 06. Validar el nombre del 1er producto
        products_header = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/a/div")
        self.assertEqual("Sauce Labs Backpack", products_header.text)
        print (products_header.text)

        # 06. Validar el precio del 1er producto
        products_header = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div")
        self.assertEqual("$29.99", products_header.text)
        print (products_header.text)

        time.sleep(2)