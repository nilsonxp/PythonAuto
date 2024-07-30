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

# DESAFIO 1
# Analise botões
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

sleep(2)

# DESAFIO 2
# Enviando dados a caixa de texto e clicando
input_nome = driver.find_element(By.ID,'dadosusuario')
input_nome_escondido = driver.find_element(By.ID,'escondido')
nome_submit = driver.find_element(By.ID,'desafio2')
nome_submit_escondido = driver.find_element(By.ID,'validarDesafio2')
# Rolar até o elemento antes de clicar
ActionChains(driver).move_to_element(nome_submit).perform()
input_nome.send_keys('Nilson')
sleep(1)
nome_submit.click()
ActionChains(driver).move_to_element(nome_submit_escondido).perform()
input_nome_escondido.send_keys('Nilson de novo, aff')
nome_submit_escondido.click()
sleep(3)

# DESAFIO 3
# Trabalhando com checkbox
checkbox_conversivel = driver.find_element(By.ID,'conversivelcheckbox')
checkbox_offroad = driver.find_element(By.ID,'offroadcheckbox')
# ActionChains(driver).move_to_element(checkbox_conversivel).perform()
ActionChains(driver).move_to_element(checkbox_offroad).perform()
checkbox_conversivel.click()
checkbox_offroad.click()
sleep(3)


# DESAFIO 4
# Digitando um texto grande e finalizando com um clique
texto_grande = driver.find_element(By.ID,'campoparagrafo')
validar_text = driver.find_element(By.XPATH,"//button[@onclick='ValidarDesafio4()']")
ActionChains(driver).move_to_element(validar_text).perform()
texto_original = 'Simulando uma pessoa digitando um texto, com tempo de pausa de 0.04. Texto muito grande, bla bla bla bla bla bla bla. Texto muito grande, bla bla bla bla bla bla bla.'
texto = 'teste veloz'
for letras in texto_original:
    texto_grande.send_keys(letras)
    sleep(0.04)
validar_text.click()
sleep(3)

# Tratando o alerta da validação acima
alert = driver.switch_to.alert
print(f"Alerta encontrado: {alert.text}")
sleep(3)
alert.accept()  # ou alert.dismiss() para dispensar o alerta


# DESAFIO 5
# 1
carro_2 = driver.find_element(By.XPATH,"(//div/input[@name='carros'])[2]")
carro_4 = driver.find_element(By.XPATH,"(//div/input[@name='carros'])[4]")
carro_5 = driver.find_element(By.XPATH,"(//div/input[@name='carros'])[5]")
ActionChains(driver).move_to_element(carro_5).perform()
carro_2.click()
carro_4.click()
carro_5.click()
sleep(3)

# 2
motos = driver.find_elements(By.XPATH,"//div/input[@name='motos']")
for moto in motos:
    ActionChains(driver).move_to_element(moto).perform()
    moto.click()
sleep(3)


# DESAFIO 6
# trabalhando com dropdown
paises_select = driver.find_elements(By.ID,'paisesselect')
ActionChains(driver).move_to_element(paises_select[0]).perform()
sleep(1)
pais_eua = driver.find_element(By.XPATH,"//select/option[@value='estadosunidos']").click()
sleep(1)
pais_africa = driver.find_element(By.XPATH,"//select/option[@value='africa']").click()
sleep(1)
pais_chile = driver.find_element(By.XPATH,"//select/option[@value='chille']").click()
sleep(3)

# # outro modo
# from selenium.webdriver.support.select import Select
# opcoes = Select(paises_select)
# # por indice
# opcoes.select_by_index(2)
# # por valor
# opcoes.select_by_value('estadosunidos')
# # por texto de exibição
# opcoes.select_by_visible_text('Brasil')



# DESAFIO 7
# Abre nova janela
# Guardar o identificador da janela original
janela_original = driver.current_window_handle

# Clicar para abrir uma nova janela
nova_janela = driver.find_element(By.XPATH, "//button[@onclick='abrirJanelaDesafio()']")
ActionChains(driver).move_to_element(nova_janela).perform()
sleep(4)
nova_janela.click()
sleep(3)

# Capturar todos os identificadores de janelas abertas
janelas = driver.window_handles

# Alternar para a nova janela
for janela in janelas:
    if janela != janela_original:
        driver.switch_to.window(janela)
        break

# Executar as ações na nova janela
driver.get('https://cursoautomacao.netlify.app/janeladesafio')
opiniao_curso = driver.find_element(By.ID, 'opiniao_sobre_curso')
opiniao_curso.send_keys('Melhor curso que já vi na internet!!')
pesquisar = driver.find_element(By.ID, 'fazer_pesquisa').click()

sleep(3)
driver.switch_to.window(janela_original)
fim_curso_texto = driver.find_element(By.ID,'campo_desafio7')
ActionChains(driver).move_to_element(nova_janela).perform()
fim_curso_texto.send_keys('Que curso incrível!!')
label_final = driver.find_element(By.ID,'label7')
ActionChains(driver).move_to_element(label_final).perform()

# FIM

input('aperte uma tecla para fechar')
driver.close()


