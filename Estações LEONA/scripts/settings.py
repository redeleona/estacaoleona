#settings.py

import json, os

class Settings():
    #Classe para iniciar as configuração dos Servidores"""
    def __init__(self, n):
        """
        :type n: inteiro
        :param n: Posição no array de câmeras no arquivo settings.json
        """
        
        jsonFile = os.path.join(os.path.dirname(__file__),'settings.json')
        """:variável jsonFile: procura o arquivo .json"""
        arq_settings = open(jsonFile,'r')
        """:variável arq_settings(): Lê Arquivo .json"""        
        json_settings = json.load(arq_settings)
        """:variável json_settings(): Lê arq_settings e transforma em object.json"""
        camera = json_settings['cameras'][n]
        """:variável camera(json.array): Recebe configuração de cada servidor"""
        
        self.config = {}
        """:contante config: Lê as configuração de Porta serial de controle de teste de câmeras e do pantilt, a taxa de aquisição de dados e se a versão de teste deve ser ativada"""
        self.config['is_pantilt'] = camera['is_pantilt']
        """:contante config['is_pantilt']: Verifica se o controla de pantilt está ativo"""
        self.config['port_con'] = camera['controle_pantilt']['comunicacao_serial']['port_com']
        """:constante self.config['port_con']: (string) Lê a porta escolhida para comunicação serial com o pantilt"""
        self.config['baudrate'] = camera['controle_pantilt']['comunicacao_serial']['baudrate']
        """:constante self.config['baudrate']: (string) Determina a taxa de leitura de dados da comunicação serial com o pantilt"""

        self.config['frames'] = camera['frames']
        """:constante self.config[]: (inteiro) Taxa de transmissão do servidor"""
        self.config['port_listen'] = camera['port_listen']
        """:constante self.config[]: (string) Porta de comunicação do servidor"""

        self.config['is_test'] = camera['is_test']
        """:constante self.config[]: (booleano) Indica se a versão de testes deve ser inicializada"""

        self.config['vc_port_con'] = camera['test']['video_camera']['port_com']
        """:constante self.config[]: (string) Determina a porta de comunicação serial para o teste das câmeras"""
        self.config['vc_baudrate'] = camera['test']['video_camera']['baudrate']
        """:constante self.config[]: (string) Determina a taxa de leitura de dados da comunicação serial nesta porta"""
        self.config['vc_name_arq'] = camera['test']['video_camera']['name_arq']
        """self.config[]: (string) Nome do arquivo gerado no teste de gravação da(s) câmera(s)"""

    def get_config(self):
        """Retorna as configurações lidas do arquvo settings.json"""
        return self.config
