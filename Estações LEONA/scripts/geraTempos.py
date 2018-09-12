#BIBLIOTECA DE TESTE
#VERIFICA SE A FREQUENCIA DE LEITURA DOS FRAMES É 33ms
#GERA UM ARQUIVO DE NOME 'tempos.txt'
#CONTEUDO:
#   - Data de inicio e fim da gravação
#   - Somatória de total de frames adquiridos 'Nº Frames'
#   - Média da frequência de leitura dos Frames ' Média em ms'
#   - Frames adquiridos por segundo 'FPS'

from datetime import datetime

class GeraTempos():

    def __init__(self):
        self.anterior = 0
        self.atual = 0
        self.soma = 0
        self.conteudo = None

    def tempo(self,lista):
        print("tempo")
        arquivo = open('tempos.txt', 'r')
        self.conteudo = arquivo.readlines()
        self.conteudo.append('\n\n\n################################################################################'+
                             '\n################################################################################'+
                             '\n\t\t\tNova Captura'+
                             '\n################################################################################'+
                             '\n################################################################################\n\n\n')
        for i in range (len(lista)):
            self.conteudo.append(str(lista[i])+'\n')
            self.atual = lista[i].microsecond
            if self.anterior != 0:
                count = self.atual - self.anterior
                if count < 0:
                    count = count+1000000
                self.soma = self.soma + count
            self.anterior = lista[i].microsecond
                
        self.soma = self.soma/1000
        
        self.conteudo.append('\n'+'Inicio de Gravação: '+str(lista[0])+'\n')
        print("\nInicio de Gravação: "+str(lista[0])+"\n")
        
        self.conteudo.append('Fim da Gravação: '+str(lista[len(lista)-1])+'\n')
        print("Fim da Gravação: "+str(lista[len(lista)-1])+"\n\n")
        
        self.conteudo.append('Soma: '+str(self.soma)+'\n')
        print("Soma: "+str(self.soma)+"\n")
        
        self.conteudo.append('Nº Frames: '+str(len(lista))+'\n')
        print("Nº Frames: "+str(len(lista))+"\n")

        self.conteudo.append('Média em ms: '+str(self.soma/len(lista))+'\n')
        print("Média em ms: "+str(self.soma/len(lista))+"\n")

        self.conteudo.append('FPS: '+str((1/(self.soma/len(lista)))*1000)+'\n')
        print("FPS: "+str((1/(self.soma/len(lista)))*1000)+"\n")
        

        arquivo = open('tempos.txt', 'w')
        arquivo.writelines(self.conteudo)
        arquivo.close()
