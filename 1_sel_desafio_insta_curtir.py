from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as CondicaoExperada
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep


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

    wait = WebDriverWait(
        driver,
        10,
        poll_frequency=1,
        ignored_exceptions=[
            NoSuchElementException,
            ElementNotVisibleException,
            ElementNotSelectableException,
        ]
    )
    return driver, wait


driver, wait = iniciar_driver()
# Entrar no site do instagram
driver.get('https://www.instagram.com/')
# Clicar e digitar meu usuário
campo_usuario = wait.until(CondicaoExperada.element_to_be_clickable(
    (By.XPATH, "//input[@name='username']")))
campo_usuario.send_keys('seuusuario')
sleep(3)
# Clicar e digitar minha senha
campo_senha = wait.until(CondicaoExperada.element_to_be_clickable(
    (By.XPATH, "//input[@name='password']")))
campo_senha.send_keys('suasenha')
sleep(3)
# Clicar no campo entrar
botao_entrar = wait.until(CondicaoExperada.element_to_be_clickable(
    (By.XPATH, "//div[text()='Entrar']")))
sleep(3)
botao_entrar.click()
sleep(15)
while True:
    # Navegar até a página alvo
    driver.get('https://instagram.com/devaprender')
    sleep(5)
    # Clicar na última  postagem
    postagens = wait.until(CondicaoExperada.visibility_of_any_elements_located(
        (By.XPATH, "//div[@class='_aagu']")))
    sleep(5)
    postagens[0].click()
    # Verificar se postagem foi curtida, caso não tenha sido, clicar curtir, caso já tenha sido, aguardar 24hrs
    elementos_postagem = wait.until(CondicaoExperada.visibility_of_any_elements_located(
        (By.XPATH, "//div[@class='_abm0 _abl_']")))
    if len(elementos_postagem) == 6:
        elementos_postagem[0].click()
        sleep(86400)
    else:
        print('postagem já foi curtida')
        sleep(86400)