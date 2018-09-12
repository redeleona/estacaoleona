#comunicacao_serial.py
__author__ = 'Igor Henrique Camargo, Ana Laura Gonçalves da Silva'
__date__ = "$22/08/2017 13:30:00$"
__version__ = '1.0'

import serial

class ComunicacaoSerial(object):

    def __init__(self, port='COM3', baudrate=9600):
        """Inicia a Comunicação Serial

        :type port: string
        :param port: Recebe a porta COM em que o Arduino foi conectado, por padrão, porta COM3

        :type baudrate: inteiro
        :param baudrate: Taxa de aquisição de dados feita pelo Arduino, por padrão 9600 
        """
        
        self.ser = serial.Serial()
        """:função ser:  Abre comunicação a Comunicação Serial e é responsável por ler port e baudrate definidos"""
        self.baudrate = baudrate
        """:variável baudarate: Recebe a taxa de aquisição de dados feita pelo Arduino"""
        self.ser.port = port
        """:variável ser.port: (string) Recebe porta em que o Arduino foi conectado, por padrão, porta COM3"""
        self.ser.open()
        """:função open: Inicia a comunicação"""
       
    def __del__(self):
       """ Finaliza a conexão com a porta serial escolhida""" 
       self.ser.close()
  
    def enviar(self, arg):
        """Recebe o dado a ser enviado para o Arduino e depois limpa a memória para permitir novo envio de dados

        :type arg: inteiro
        :param arg: Dado para teste da taxa de leitura das cameras. Teste feito com Osiloscópio e Arduino: taxa deve ser 30ms.
        """
        
        self.ser.write(bytes(arg,'UTF-8'))
        """:função self.ser.write(): Envia dado para Arduino"""
        self.ser.flush()
        """:função ser.flush(): Limpa a memória"""
