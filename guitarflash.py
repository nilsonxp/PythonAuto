import pyautogui as p
import threading
import keyboard

# Definição das cores e posições
posicao_das_cores = {
    'green': {'posicao': (1064, 1265), 'cor': (0, 152, 0), 'tecla': 'a'},
    'red': {'posicao': (1176, 1265), 'cor': (255, 0, 0), 'tecla': 's'},
    'yellow': {'posicao': (1289, 1265), 'cor': (244, 244, 2), 'tecla': 'j'},
    'blue': {'posicao': (1401, 1265), 'cor': (0, 152, 255), 'tecla': 'k'},
    'orange': {'posicao': (1462, 1268), 'cor': (255, 101, 0), 'tecla': 'l'},
}

# Cores
def checar_cor(info_cor):
    while True:
        if p.pixelMatchesColor(info_cor['posicao'][0], info_cor['posicao'][1], info_cor['cor']):
            p.press(info_cor['tecla'])

# Saída
def listen_for_exit():
    keyboard.wait('1')
    print('Automação interrompida.')
    exit()

print('Iniciando...')

# Criando e iniciando threads para cada cor
threads = []
for cor, info in posicao_das_cores.items():
    t = threading.Thread(target=checar_cor, args=(info,))
    t.daemon = True  # Define a thread como daemon
    t.start()
    threads.append(t)

# Iniciando thread para ouvir pela tecla de saída
exit_thread = threading.Thread(target=listen_for_exit)
exit_thread.daemon = True  # Define a thread como daemon
exit_thread.start()

# Aguardando a finalização do programa (não necessário quando usando daemon threads)
exit_thread.join()

print('Fim')

# Antes de usar as threads eu pensei em fazer combinações dos botões, mas alémn de trabalhoso, não iria resolver a situação
#     # if p.pixelMatchesColor(verde_pos[0],verde_pos[1],verde_cor) and p.pixelMatchesColor(vermelho_pos[0],vermelho_pos[1],vermelho_cor):
#     #     p.hotkey('a','s')
#     # if p.pixelMatchesColor(vermelho_pos[0],vermelho_pos[1],vermelho_cor) and p.pixelMatchesColor(amarelo_pos[0],amarelo_pos[1],amarelo_cor):
#     #     p.hotkey('s','j')
#     # if p.pixelMatchesColor(amarelo_pos[0],amarelo_pos[1],amarelo_cor) and p.pixelMatchesColor(azul_pos[0],azul_pos[1],azul_cor):
#     #     p.hotkey('j','k')
