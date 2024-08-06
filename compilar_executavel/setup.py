import sys
import os
from cx_Freeze import setup, Executable

# Definir o que deve ser incluído na pasta final
arquivos = ['compilar_executavel/dados.txt', 'compilar_executavel/musicas/']
# Saida de arquivos
configuracao = Executable(
    script='compilar_executavel/app.py',
    icon='compilar_executavel/rede.png'
)
# Configurar o executável
setup(
    name='Automatizador de login',
    version='1.0',
    description='Este programa automatizar o login deste site',
    author='Nilson Almeida',
    options={'build_exe':{
        'include_files': arquivos,
        'include_msvcr': True # RODAR EM WINDOWS ETC
    }},
    executables=[configuracao]
)

# python arquivo build