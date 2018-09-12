#main.py
__author__ = 'Igor Henrique Camargo, Ana Laura Gonçalves da Silva'
__date__ = "$22/08/2017 13:30:00$"
__version__ = '1.0'

import pip, json, subprocess, os, threading, time

def verificar_arquivos(files):
    """ Verifica se todos os arquivos necessários para execução do software existem

    :type files: json.array
    :param files: Lista json contendo os arquivos que deverão existir na pasta do software
    """
    print('Verificando Arquivos ...')
    for f in files:
        r = os.path.isfile(f)
        if not r:
            print('Arquivo '+f+' não encontrado')

    print('Todos os arquivos verificados!')

def verificar_pastas(paths):
    """ Verifica se todos as pastas necessárias para execução do software existem

    :type paths: json.array
    :param paths: Lista json contendo as pastas que deverão existir na pasta do software
    """    
    print('Verificando Pastas ...')
    for p in paths:
        r = os.path.exists(p)
        if not r:
            print('Criando pasta '+ p)
            os.mkdir('videos')
    print('Todos as pastas verificados!')
    
def verificar_dependencias(dependencies):
    """ Verifica se todos as dependências necessárias para execução do software existem

    :type dependencies: json.array
    :param dependencies: Lista json contendo as dependências que deverão existir para execução do software
    """
    
    print('\n\nVerificando pendências ...')
    for d in dependencies:
        m = False
        for i in pip.get_installed_distributions():
            if d == i.key and dependencies[d] == i.version:
                print('dependecie match: '+d+', '+dependencies[d])
                m = True
                break
        if not m:
            try:
                r = subprocess.call('pip install '+d+'=='+dependencies[d])
            except Exception:
                print('Erro ao instalar')

    print('Todas dependências instaladas')     

def camera(arg):
    """Recebe comando para iniciar servidores

    :type arg: string
    :param arg: Comando de inicialização da câmera 1 ou 2
    """
    
    """:função subprocess.call(): Cria um subprocesso para iniciar o servidor tornado para transmissão e controle da Câmera"""
    subprocess.call(arg)

def main():
    """Verifica se todos os arquivos e dependências estão presentes na Estação LEONA e se estiver inicia o serviço de transmissão."""
  
    jsonFile = os.path.join(os.path.dirname(__file__),'settings.json')
    """:variável jsonFile: Procura o arquivo de configuração na pasta local"""
    arq_settings = open(jsonFile,'r')
    """:variável arq_settings: Armaze os dados contidos no arquivo .json"""
    json_settings = json.load(arq_settings)
    """:váriável json_settings: Transforma "arq_settings" em um objeto do tipo json"""
    dependencies = json_settings['dependencies']
    """:variável dependencies: Lê todos as linhas com a marcação "dependecies" em "json_settings", ou seja as bilbiotecas que devem ser adicionadas para que o software da Estação LEONA funcione corretamente"""
    files = json_settings['files']
    """:variável files: Lê todos as linhas com a marcação "files" em "json_settings", ou seja os scripts Python que devem existir para que o software da Estação LEONA funcione"""
    paths = json_settings['paths']
    """:variável paths: Lê todos as linhas com a marcação "files" em "json_settings", ou seja as pastas que devem existir para que o software da Estação LEONA funcione"""
    verificar_arquivos(files)
    """:função verificar_arquivos: Verifica se todos arquivos necessários estão na pasta local"""
    verificar_pastas(paths)
    """:função verificar_pastas: Verifica se todas as pastas necessárias estão na pasta local"""
    verificar_dependencias(dependencies)
    """:função verificar_dependencias: Verifica as bibliotecas estão instaladas na Estação LEONA"""

    t = threading.Thread(target = camera,args=('python servidor_tornado_camera_1.py',))
    """:thread t: inicia o Servidor responsável pela leitura e trasmissão da Camera 1"""
    t.daemon = True
    t.start()

    time.sleep(3)

    t1 = threading.Thread(target = camera,args=('python servidor_tornado_camera_2.py',))
    """:thread t2: inicia o Servidor responsável pela leitura e trasmissão da Camera 2"""
    t1.daemon = True
    t1.start()

    time.sleep(3)

    t2 = threading.Thread(target = camera,args=('python servidor_tornado_camera_3.py',))
    """:thread t2: inicia o Servidor responsável pela leitura e trasmissão da Camera 3"""
    t2.daemon = True
    t2.start()    

if __name__ == '__main__':
    """Chama o método main para iniciar o serviço da Estação LEONA"""
    
    main()
