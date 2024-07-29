from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

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
driver.get('https://cursoautomacao.netlify.app/')

botao = driver.find_element(By.ID,'buttonalerta')
botoes = driver.find_elements(By.ID,'buttonalerta')
digite_seu_nome = driver.find_element(By.NAME,'seu-nome')
radio_buttons = driver.find_elements(By.NAME,'exampleRadios')
logo = driver.find_element(By.CLASS_NAME,'navbar-brand')
links_menu = driver.find_elements(By.CLASS_NAME,'navbar-brand')
home = driver.find_element(By.LINK_TEXT,'Home')
desafios_parcial = driver.find_element(By.PARTIAL_LINK_TEXT,'Des')
titulo_por_texto = driver.find_element(By.XPATH,"//*[text()='ZONA DE TESTES']")
titulo_por_tag = driver.find_element(By.TAG_NAME,'h1')
elemento_por_tag = driver.find_elements(By.TAG_NAME,'h4')

if botao is not None:
    print('botao foi encontrado')
if botoes is not None:
    print('botoes foi encontrado')
if digite_seu_nome is not None:
    print('Campo digite seu nome foi encontrado')
if radio_buttons is not None:
    print('Radio buttons foram encontrados')
if logo is not None:
    print('A logo foi encontrada')
if links_menu is not None:
    print('Os links do menu foram encontrados')
if home is not None:
    print('O link home foi encontrado')
if desafios_parcial is not None:
    print('O link desafio foi encontrado por pesquisa parcial')
if titulo_por_texto is not None:
    print('O titulo foi encontrado por pesquisa xpath')
if titulo_por_tag is not None:
    print('O titulo foi encontrado por pesquisa de tag h1')
if elemento_por_tag is not None:
    print('Os elementos h4 foram encontrados por pesquisa de tag')


# tag(section,div,h4,button)
# class(.btn)
# combinação de class(.btn.btn-success)
# Id (#dropDownMenuButton)

# Para encontrar valores exatos
# input[class='form-check-input']
# Inicia com algum valor
# input[class^='form']
# finaliza com algum valor
# input[class$='input']
# Contem algum valor
# input[class*='check']


# Encontrar o primeiro elemento <h2>
elemento_h2 = driver.find_element(By.CSS_SELECTOR, 'h1')
print(elemento_h2.text)  # Exemplo para exibir o texto do elemento

# Encontrar todos os elementos com a classe "form-check-input"
# elementos_form_chec = driver.find_element(By.CSS_SELECTOR,'input[class="form-check-input"]')
elementos_form_chec = driver.find_elements(By.CSS_SELECTOR, 'input.form-check-input')
for elemento in elementos_form_chec:
    print(elemento.get_attribute('outerHTML'))  # Exemplo para exibir o HTML do elemento

input('aperte uma tecla para fechar')
driver.close()


