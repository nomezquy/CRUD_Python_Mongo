from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")
driver.get("http://python.org") ## Abrir página en especifico.
driver.close() ## Cerrar página