#video_camera.py
import cv2, numpy, time, threading, settings

class VideoCamera(threading.Thread):
    """Classe que estende threading.Thread responsável por ler uma imagem da placa de captura colocando a mesma em uma multiprocessing.Queue"""
    def __init__(self, path = 0, queue = None):
        """Inicia a câmera

        :type path: inteiro
        :param path: Indica qual placa de captura deve ser utiliza. Número identido ao indicado na placa conectada a placa mãe da Estação Leona.

        :type queue: multiprocessing.Queue
	:param queue: array reponsável por guardar os frames para que outro processo possa ler

        """
        threading.Thread.__init__(self)

        self.stream = cv2.VideoCapture(path)
        """:variável stream: (cv2.VideoCapture) Instância de VideoCapture"""
        self.stream.release()
        """:variável stream.release: (cv2.VideoCapture) Limpa a memória disponivel para a leitura da câmera. Necessário para a iniciação correta das câmeras."""        
        self.stream.open(path)
        """:variável stream.open: (cv2.VideoCapture) re-instância de VideoCapture"""
        
        (self.grabbed, self.frame) = self.stream.read()

        self.stopped = False#:(booleano) - Controla a finalização da gravação
        """:variável stopped: (boolean) Controla finalização da aquisição de imagem"""
        self.recorded = False#:(booleano) - Controla a inicialização da gravação
        """:variável recorded: (boolean) Controla inicialização e finalização da gravação"""
        self.queue = queue#:(multiprocessing.Queue) - buffer de imagens
        """:variável queue: (multiprocessing.Queue) Instância de Queue"""
        self.out = None
        """:variável out: (cv2.VideoWriter) Instância de VideoWriter"""

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

        while True:

            if self.stopped:#Finaliza a leitura das câmeras
                break
            
            tcurrent = time.time()

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

    def stop(self):
        """Finaliza a leitura da camera"""
        self.stopped = True

