video\_camera\_teste
====================
	
	Classe de Teste de gravação de frames e transmissão dos dados
	
    Estende threading.Thread responsável por ler uma imagem da placa de captura colocando a mesma em uma multiprocessing.Queue
    
	Debug
    
        Osciloscopio
        
            Permite o monitoramento do loop com osciloscopio
            para o mesmo é necessário que no arquivo de configuração
            a variável TEST_OSCILOSCOPIO esteja como True e que passe
            como parametro um objeto da classe comunicacaoserial

        Arquivo txt

            Gera um arquivo txt contendo o timestamp do instante de cada loop

.. automodule:: video_camera_teste
    :members:
    :undoc-members:
    :show-inheritance:
