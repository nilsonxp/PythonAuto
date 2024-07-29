import random
from datetime import datetime


nome = input('Informe seu nome: ')
dataNascimento = datetime.strptime(input('Informe a sua data de nascimento (dd/mm/aaaa): '),'%d/%m/%Y')
dataCadastro = datetime.now()
cartoes = ['50,00','250,00','120,00']
cartaoCliente = random.choice(cartoes)

# Formatando a data de cadastro para um formato mais legível
dataCadastroFormatada = dataCadastro.strftime('%d/%m/%Y')

print(f'Olá {nome}, seu registro foi concluído com sucesso no dia {dataCadastroFormatada}.')
print(f'Parabéns, houve um sorteio e você ganhou um cartão de compras no valor de R${cartaoCliente}.')

