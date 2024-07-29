from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

# Fonte de opções de switches https://chromium.googlesource.com/chromium/src/+/master/chrome/common/chrome_switches.cc e  https://peter.sh/experiments/chromium-command-line-switches/
def iniciar_driver():

    chrome_options = Options()
    '''
    --start-maximized # Inicia maximizado
    --lang=pt-BR # Define o idioma de inicialização, # en-US , pt-BR
    --incognito # Usar o modo anônimo
    --window-size=800,800 # Define a resolução da janela em largura e altura
    --headless # Roda em segundo plano(com a janela fechada)
    --disable-notifications # Desabilita notificações
    --disable-gpu # Desabilita renderização com GPU
    '''
    arguments = ['--lang=pt-BR', '--window-size=800,600', '--incognito',]
    for argument in arguments:
        chrome_options.add_argument(argument)
    # Lista de opções experimentais(nem todas estão documentadas) https://chromium.googlesource.com/chromium/src/+/master/chrome/common/pref_names.cc
    # Uso de configurações experimentais
    chrome_options.add_experimental_option('prefs', {
        # Alterar o local padrão de download de arquivos
        'download.default_directory': 'C:/PythonCurso',
        # notificar o google chrome sobre essa alteração
        'download.directory_upgrade': True,
        # Desabilitar a confirmação de download
        'download.prompt_for_download': False,
        # Desabilitar notificações
        'profile.default_content_setting_values.notifications': 2,
        # Permitir multiplos downloads
        'profile.default_content_setting_values.automatic_downloads': 1,

    })
    # inicializando o webdriver
    driver = webdriver.Chrome(options=chrome_options)
    # Navegar até um site
    
    return driver

driver = iniciar_driver()
driver.get('https://cursoautomacao.netlify.app/desafios.html')

botao1 = driver.find_element(By.ID,'btn1')
botao2 = driver.find_element(By.XPATH,'/html/body/section[1]/button[2]')
botao3 = driver.find_element(By.XPATH,'/html/body/section[1]/button[3]')

if botao1.is_enabled():
    print('Botão 1 habilitado')
else:
    print('Botão 1 desabilitado')
    
if botao2.is_enabled():
    print('Botão 2 habilitado')
else:
    print('Botão 2 desabilitado')
    
if botao3.is_enabled():
    print('Botão 3 habilitado')
else:
    print('Botão 3 desabilitado')



input_nome = driver.find_element(By.ID,'dadosusuario')
input_nome_escondido = driver.find_element(By.ID,'escondido')
nome_submit = driver.find_element(By.ID,'desafio2')
nome_submit_escondido = driver.find_element(By.ID,'validarDesafio2')
# Rolar até o elemento antes de clicar
ActionChains(driver).move_to_element(nome_submit).perform()
input_nome.send_keys('Nilson')
nome_submit.click()
ActionChains(driver).move_to_element(nome_submit_escondido).perform()
input_nome_escondido.send_keys('Nilson de novo, aff')
nome_submit_escondido.click()


checkbox_conversivel = driver.find_element(By.ID,'conversivelcheckbox')
checkbox_offroad = driver.find_element(By.ID,'offroadcheckbox')
# ActionChains(driver).move_to_element(checkbox_conversivel).perform()
ActionChains(driver).move_to_element(checkbox_offroad).perform()
checkbox_conversivel.click()
checkbox_offroad.click()


texto_grande = driver.find_element(By.ID,'campoparagrafo')
texto = 'Texto muito grande, bla bla bla bla bla bla bla. Texto muito grande, bla bla bla bla bla bla bla. Texto muito grande, bla bla bla bla bla bla bla.'
for letras in texto:
    texto_grande.send_keys(letras)
    sleep(0.1)



input('aperte uma tecla para fechar')
driver.close()


