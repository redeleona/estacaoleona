#controle_pantilt.py
__author__ = 'Igor Henrique Camargo, Ana Laura Gonçalves da Silva'
__date__ = "$22/08/2017 13:30:00$"
__version__ = '1.0'

class ControlePantilt(object):

    def __init__(self, con = None):
        """Iniciar a posição do Pan-Tilt

        :type con: object
        :param con: Instância de comunicao serial      
  
        Padrão de comando de comunicação entre Arduino e Pan-Tilt:

        .. code:: bash
        
            !000U* - Mover para cima
            !000D* - Mover para baixo
            !000R* - Mover para direita
            !000L* - Mover para esquerda
            !111O* - Ligar camera (um,um,um,letra 'O')
            !111F* - Desligar camera
            
        Valores máximos e mínimos:
            Azimute: 0º -> 350º
            Elevação: -35º -> +35º      
        """

        self.azGraus = 0
        """:variável azGraus:  (inteiro) Armazena a ultima posicao do pan-tilt em azimute"""
        self.elGraus = 0
        """:variável elGraus: (inteiro) Armazena a ultima posicao do pan-tilt em elevacao"""
        self.con = con
        """:variável con: (instância) Recebe a comunicação serial iniciado pela classe principal"""
        
        if con is None: # Verifica se a comunicação serial foi iniciada
            print('Sem Comunicação Serial')
            return
        
    def formatargraus(self,graus):
        """Verifica valor informado e formata no padrão de bits

        :type graus: inteiro
        :param graus: valor de azimute ou elevação selecionado pelo observador da Rede Leona
        """
        if graus < 10:
            return '!00' + str(graus)
        elif graus >= 10 and graus < 100:
            return '!0' + str(graus)
        return '!' + str(graus)
    
    def converterelevacao(self,graus):
        """Converte o valor recebido para o valor esperado pelo controlador de Pan-Tilt, onde
        -35º == 0, 0º == 35, 35º == 70, ou seja todos os valores recebidos devem ser acrescidos de 35

        :type graus: inteiro
        :param graus: valor entre -35 e 35 elevação
        """
        return graus+35
        
    def azimute(self,graus):
        """Verifica se os graus recebidos estão entre 0 e 350, compara com o valor anterior e assim determina se o comando enviado deve ser para a direita ou esquerda

        :type graus: inteiro
        :param graus: valor entre 0 e 350 azimute        
        """
        if graus >= 0 and graus <= 350:
            if graus < self.azGraus:
                self.esquerda(self.azGraus - graus)
            elif graus > self.azGraus:
                self.direita(graus - self.azGraus)
        self.azGraus = graus
        
    def elevacao(self,graus):
        """Verifica se os graus recebidos estão entre 0 e 70, compara com o valor anterior e assim determina se o comando enviado deve ser para cima ou baixo

        :type graus: inteiro
        :param graus: valor entre -35 e 35 elevação
        """
        graus = self.converterelevacao(graus)#converterelevacao(graus)- Converte o valor recebido para o esperado pelo controlador
        if graus >= 0 and graus <= 70:
            if graus < self.elGraus:
                self.descer(self.elGraus - graus)
            elif graus > self.elGraus:
                self.subir(graus - self.elGraus)
            self.elGraus = graus
            
    def subir(self,graus):
        """Concatena os graus com !###U* onde #### representa os graus, e envia para a controladora

        :type graus: inteiro
        :param graus: valor a ser enviado para controlador
        """
        self.con.enviar(self.formatargraus(graus)+'U*')
        
    def descer(self,graus):
        """Concatena os graus com !###D* onde #### representa os graus, e envia para a controladora

        :type graus: inteiro
        :param graus: valor a ser enviado para controlador
        """
        self.con.enviar(self.formatargraus(graus)+'D*')
        
    def direita(self,graus):
        """Concatena os graus com !###R* onde #### representa os graus, e envia para a controladora

        :type graus: inteiro
        :param graus: valor a ser enviado para controlador
        """
        self.con.enviar(self.formatargraus(graus)+'R*')
        
    def esquerda(self,graus):
        """Concatena os graus com !###L* onde #### representa os graus, e envia para a controladora

        :type graus: inteiro
        :param graus: valor a ser enviado para controlador
        """
        self.con.enviar(self.formatargraus(graus)+'L*')
        
    def resetarazimute(self):
        """Envia para a controladora !350L, assim resetando azimute em 0º"""
        
        self.con.enviar(self.formatargraus(350)+'L*')
        
    def resetarelevacao(self):
        """Envia para a controladora !070D, assim resetando a elevação em 0º ou -35º """

        self.con.enviar(self.formatargraus(70)+'D*')

    def ligarcamera(self):
        """Liga as câmeras: """
        
        self.con.enviar('!111O*')

    def desligarcamera(self):
        """Desliga as câmeras: Comando deve ser sempre executado após as observações agendadas, ou hórarios determinado na Estação LEONA, para diminuir a degrdação das câmeras CCDs."""

        self.con.enviar('!111F*')

    def __del__(self):
        """Garante que caso exista algum erro ou falha no sistema as câmeras serão desligadas """

        self.desligarcamera()
