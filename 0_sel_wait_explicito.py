from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import *
from selenium.webdriver.chrome.service import Service as ChromeService
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait # <<<<<<<<<<<<< NECESSARIO
from selenium.webdriver.support import expected_conditions as condicao_esperada # <<<<<<<<<<<<< NECESSARIO

# Iniciar o webdriver


def iniciar_driver():
    chrome_options = Options()

    arguments = ['--lang=en-US', '--window-size=1300,1000', '--incognito']

    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1

    })

    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(
        driver,
        10, # SEGUNDOS
        poll_frequency=1, # QUANTAS VEZES POR SEGUNDO
        ignored_exceptions=[
            NoSuchElementException, # NÃO ENCONTROU
            ElementNotVisibleException, # NÃO VISIVEL
            ElementNotSelectableException, # NÃO SELECIONAVEL
        ]
        # DOC SELENIUM
        # https://selenium-python.readthedocs.io/api.html?_gl=1*jzswit*_ga*MTczMTA0MDMwNy4xNzE5MzQ2NjY0*_ga_37GXT4VGQK*MTcyMjk1NDIwMy42OC4xLjE3MjI5NTQ4NzUuMC4wLjA.#module-selenium.common.exceptions
    )
    return driver, wait


driver, wait = iniciar_driver()
driver.get('https://google.com/flights')

sugestoes_de_voo = wait.until(condicao_esperada.visibility_of_all_elements_located(
    (By.XPATH, "//div[@class='wIuJz']")))

# sugestoes_de_voo = wait.until(condicao_esperada.visibility_of_any_elements_located(
#     (By.XPATH, "//div[@class='wIuJz']")))

# sugestoes_de_voo = driver.find_elements(By.XPATH, "//div[@class='wIuJz']") # ANTES DO WAIT EXPLICITO

sugestoes_de_voo[0].click()


sleep(5)

driver.get('https://cursoautomacao.netlify.app/login')

campo_email = wait.until(condicao_esperada.element_to_be_clickable(
    (By.XPATH, "//input[@id='email']")))

campo_email.send_keys('jhonatan@hotmail.com')

# sugestoes_de_voo = driver.find_elements(By.XPATH, "//div[@class='wIuJz]")

input('')
driver.close()