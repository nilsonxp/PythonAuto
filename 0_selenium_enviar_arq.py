from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=800,1000', '--incognito']
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
driver.get('https://cursoautomacao.netlify.app')
sleep(1)
driver.execute_script('window.scrollTo(0,2100);')
# # Encontrar campo escolher arquivo
# botao_escolher_arquivo = driver.find_element(By.XPATH, "//input[@id='myFile']")
# sleep(1)
# # Enviar caminho completo para o arquivo dentro do meu computador
# botao_escolher_arquivo.send_keys(
#     '//Users//evoxnk//Desktop//PythonAuto//telacalc.jpg')
# sleep(1)
# # Clicar em enviar
# botao_enviar = driver.find_element(
#     By.XPATH, "//input[@value='Enviar Arquivo']")
# sleep(1)
# botao_enviar.click()

# Encontrar campo escolher arquivo
botao_escolher_arquivo = driver.find_element(By.XPATH, "//input[@id='myFile']")
sleep(1)
botao_escolher_arquivo.send_keys('//Users//evoxnk//Desktop//PythonAuto//telacalc.jpg')
sleep(1)

# Esperar até que o botão esteja clicável e então clicar
botao_enviar = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@value='Enviar Arquivo']"))
)

# Tentar clicar usando JavaScript
driver.execute_script("arguments[0].click();", botao_enviar)


input('')
driver.close()