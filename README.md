# pre-entrega Curso de Automation QA
# alumno: David Cotari


Propósito del proyecto: realizar pruebas automatizadas en el sitio "https://www.saucedemo.com"

Tecnologías utilizadas: python, html, css, selenium web driver, pytest y git. Editor VSCode

Instalar las dependencias: En mi Linux Debian 13 (python3.12 viene instalado con el S.O) y para la instalación de las dependencias se utilizan los comandos 

pip install selenium
pip install pytest
pip install webdriver-manager
pip install pytest-html

Ejecución de las pruebas:

para la ejecución de test especificos utilizamos los comandos:

correr cada test con pytest
.venv/bin/pytest tests/test_login.py
.venv/bin/pytest tests/test_inventory.py
.venv/bin/pytest tests/test_cart.py

para ejecutar todos los test juntos con pytest y generar un reporte html
.venv/bin/pytest tests/ -o log_cli=true --html=report.html --self-contained-html

