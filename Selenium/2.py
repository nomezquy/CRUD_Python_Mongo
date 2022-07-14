##ingresar datos del correo.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")
driver.get("https://gmail.com")
usuario = driver.find_element_by_id("identifierId")
usuario.send_keys("pruebas.dnomezquy@gmail.com")
usuario.send_keys(Keys.ENTER)
time.sleep(3)
contraseña = driver.find_element_by_name("password")
contraseña.send_keys("Pruebas")
contraseña.send_keys(Keys.ENTER)
