  #video_camera.py
__author__ = 'Igor Henrique Camargo, Ana Laura Gonçalves da Silva'
__date__ = "$22/08/2017 13:30:00$"
__version__ = '1.0'

import cv2, numpy, time, threading
from datetime import datetime
#LEONA LIBS
from geraTempos import GeraTempos

class VideoCamera(threading.Thread):
##    """ Classe de Teste de gravação de frames e transmissão dos dados
##
##    Estende threading.Thread responsável por ler uma imagem da placa de captura colocando a mesma em uma multiprocessing.Queue
##    
##    Debug
##    
##        Osciloscopio
##        
##            Permite o monitoramento do loop com osciloscopio
##            para o mesmo é necessário que no arquivo de configuração
##            a variável TEST_OSCILOSCOPIO esteja como True e que passe
##            como parametro um objeto da classe comunicacaoserial
##
##        Arquivo txt
##
##            Gera um arquivo txt contendo o timestamp do instante de cada loop
##    
##    """
    
    def __init__(self, path = 0, queue = None, com = None, arquivo = None):
        """Inicia a câmera

        :type path: String
	:param path: recebe caminho de leitura da câmera

	:type queue: multiprocessing.Queue
	:param queue: array reponsável por guardar os frames para que outro processo possa ler

	:type com: comunicacaoserial.ComunicacaoSerial
	:param com: recebe a com reponsável pelo arduino que recebera o comando para DEBUG

	:type arquivo: String
	:param arquivo: Nome do arquivo gerado para DEBUG dos tempos de aquisição

        """
        
        threading.Thread.__init__(self) # Inicia thread passando como parâmetro essa instâcia

        self.stream = cv2.VideoCapture(path) # Cria uma nova instancia cv2.VideoCapture
        """:variável stream (cv2.VideoCapture): Instância de VideoCapture"""
        self.stream.release()
        """:variável stream.release: (cv2.VideoCapture) Limpa a memória disponivel para a leitura da câmera. Necessário para a iniciação correta das câmeras."""        
        self.stream.open(path)
        """:variável stream.open: (cv2.VideoCapture) re-instância de VideoCapture"""
        
        (self.grabbed, self.frame) = self.stream.read()
        """:variável frame: Lê imagens da câmera"""
        
        self.stopped = False #(booleano) - Controla a finalização da gravação
        """:variável stopped: (boolean) Controla finalização da aquisição de imagem"""
        self.recorded = False #(booleano) - Controla a inicialização da gravação
        """:variável recorded: (boolean) Controla inicialização e finalização da gravação"""
        self.queue = queue #(intância) - buffer de imagens
        """:variável queue: (multiprocessing.Queue) Instância de Queue"""
        self.com = com #(instância) - comunicação serial
        """:variável com: (ComunicacaoSerial) Instância de ComunicacaoSerial"""
        self.arquivo = arquivo #(String) - caminho + nome do arquivo
        """:variável arquivo: (String) Caminho e/ou nome do arquivo"""
        self.out =  None
        """:variável out: (cv2.VideoWriter) Instância de VideoWriter"""

        self.lista = lista = []
        self.gr = GeraTempos()
        

    def __del__(self):
        """Finaliza Câmera"""

        self.stream.release()
        """:método stream.release(): Destroi instância de VideoCapture"""

    def run(self):
        """Métodod executado pela Thread"""

        tcurrent = time.time()
        """:variável tcurrent: (time.time) Tempo atual da aquisição"""
        texec = tcurrent + 0.030
        """:variável texec: (time.time) Tempo total de execução do loop"""
        if self.queue is None:
            return

        if self.com is None:
            return

        if self.arquivo is None:
            return

        osc = True
        arquivo = True

        while True:

            if self.stopped:
                break
            
            tcurrent = time.time()
            
            if osc:
                self.com.enviar('1')
            if arquivo:
              self.lista.append(datetime.now())  

            (self.grabbed, self.frame) = self.stream.read()

            if self.recorded:
                self.out.write(self.frame)

            if not self.queue.full():
                    self.queue.put_nowait(self.frame)

            if time.time() < texec:
                time.sleep(texec - time.time())


    def start_record(self):
        """Inicia a gravação em disco das imagens capturadas pela câmera"""
        fourcc = cv2.VideoWriter_fourcc(*'XVID')#(objeto) - Responsável pelo codec de vídeo utilizado na gravação
        """:variável fourcc: (cv2.VideoWriter_fourcc) Responsável pelo codec de vídeo utilizado na gravação"""
        video_name = time.strftime("%d-%m-%Y %H %M %S")#(string) - Variável responsável por receber a data de inicio da gravação.
        """:variável video_name: (time.strftime) Variável responsável por receber a data de inicio da gravação"""
        self.out = cv2.VideoWriter('videos/'+ video_name + '.avi',fourcc, 30.0, (640,480))#(objeto) - Determina respectivamente: nome, formato, codec, taxa de frames e tamanho, e codec do arquivo de vídeo.
        """:variável out: Inicia o arquivo de gravação das câmeras"""
        self.recorded = True

    def stop_record(self):
        """Finaliza a gravação em disco das imagens capturadas pela câmera"""
        
        self.out.release()#(método) -  Finaliza o arquivo de video e o libera pra uso.
        """:método out.release(): Finaliza o arquivo de video e o libera pra uso"""
        self.recorded = False
        
        self.gr.tempo(self.lista)

    def stop(self):
        """Finaliza a leitura da camera"""
        self.stopped = True

