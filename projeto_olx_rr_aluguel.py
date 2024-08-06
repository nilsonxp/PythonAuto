from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1300,1000', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,

    })
    driver = webdriver.Chrome(options=chrome_options)

    return driver

driver = iniciar_driver()
driver.get('https://www.olx.com.br/imoveis/estado-rr')

# botao_categorias = driver.find_element(By.XPATH,"/html/body/div[2]/div/main/div[1]/div[1]/div/div[3]/button/span/span")
# botao_filtros = driver.find_element(By.XPATH,"/html/body/div[2]/header/nav/nav/ul/li[1]/a/span")
# botao_categorias.click()
# sleep(3)
# botao_categ_imoveis = driver.find_element(By.XPATH,"/html/body/div[2]/div/main/div[3]/div/div[2]/div/li[2]/a/div")
# botao_categorias.click()

input_valor_min = driver.find_element(By.XPATH,"/html/body/div[1]/main/section[1]/div[3]/div/div/div[3]/div/div[1]/span/input")
input_valor_max = driver.find_element(By.XPATH,"/html/body/div[1]/main/section[1]/div[3]/div/div/div[3]/div/div[2]/span/input")
botao_buscar = driver.find_element(By.XPATH,"/html/body/div[1]/main/section[1]/div[3]/div/div/a/span")

input_valor_min.send_keys('1400')
sleep(1)
input_valor_max.send_keys('1800')
sleep(1)
botao_buscar.click()
sleep(2)

# Scroll down na página
actions = ActionChains(driver)
actions.send_keys(Keys.PAGE_DOWN).perform()
sleep(2)
actions.send_keys(Keys.PAGE_DOWN).perform()

input('aperte uma tecla para fechar')
driver.close()