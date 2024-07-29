from selenium import webdriver
from selenium.common.exceptions import WebDriverException

try:
    driver = webdriver.Chrome()
    driver.get('https://www.devaprender.com')
    input('Pressione Enter para fechar...')
except WebDriverException as e:
    print(f"Ocorreu um erro ao abrir o navegador: {e}")
finally:
    driver.quit()  # Certifique-se de fechar o navegador corretamente