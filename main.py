from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options


if __name__ == '__main__':
    options = Options()
    options.add_argument('--headless') #se asegura que no se muestre el navegador
    driver = webdriver.Firefox(options=options)
  
    try:
        # Navegar a una página web
        driver.get('https://selenium-python.readthedocs.io/getting-started.html')
        # Obtener algunos datos de la página
        # Por ejemplo, extraer el título de la página
        title = driver.title
        print(f'Título de la página: {title}')

        # Extraer un elemento por su XPath
        #example_element = driver.
        #print(f'Texto del elemento: {example_element.text}')

    finally:
        # Cerrar el navegador
        driver.quit()
   
    # driver = webdriver.Firefox()
    # driver.get("http://www.python.org")
    # assert "Python" in driver.title
    # elem = driver.find_element(By.NAME, "q")
    # elem.clear()
    # elem.send_keys("pycon")
    # elem.send_keys(Keys.RETURN)
    # assert "No results found." not in driver.page_source
    # driver.close()
