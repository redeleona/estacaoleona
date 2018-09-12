settings
========

Classe para iniciar as configuração dos Servidores.

.. automodule:: settings
    :members:
    :undoc-members:
    :show-inheritance:
	
Arquivo de configuração settings.json
-------------------------------------

Esta seção descreve o arquivo de configuração do software da Estação LEONA.

.. glossary::

	dependencies
		Define as dependências necessárias para que o software possa ser executado.	

.. code-block:: json
	
    {"dependencies":{
		"opencv-python":"3.2.0.7",
		"tornado":"4.4.2",
		"pyserial":"3.3",
		"numpy":"1.12.1"
	}}

**Código descrito acima:**
								
.. glossary::

	files 
		Define uma lista de arquivos que devem existir na pasta do software para que possa ser executado.	

	paths
		Define uma lista de pastas que devem existir na pasta do software para que possa ser executado.

**Código descrito acima:**
							
.. code-block:: json
	
   {"files":[
		"settings.json",
		"settings.py",
		"comunicacao_serial.py",
		"controle_pantilt.py",
		"servidor_tornado_camera_1.py",
		"servidor_tornado_camera_2.py",
		"video_camera.py",
		"video_camera_teste.py"
	],
	"paths":[
		"videos"
	]}

.. glossary::
	
	cameras
		Define um array de configuração para cada câmera que existe na estação.
		
	.. glossary::

		is_pantilt
			Define um booleano para indicar a presença de um pan-tilt na estação.
			
		controle_pantilt
			Objeto json que contém as configurações do pan-tilt.
			
			.. glossary::
			
				comunicacao_serial
					Objeto json com as configurações de Comunicação Serial do pan-tilt.
					
					.. glossary::
					
						port_com
							Define a porta de comunicação.
						
						baudrate
							Define a taxa de leitura da comunicação.
							
		video_camera
			Define um objeto de configuração da classe videoCamera.
		
		frames
			Define a taxa de aquisição das câmeras.
		
		port_listen
			Define a porta do websocket do servidor tornado.
			
		is_test
			Define um booleano para indicar se deverá iniciar em modo de teste.
			
		teste
			Define um objeto contendo os dados para teste do software.
			
			.. glossary::
			
				video_camera
					Define um objeto de configuração da classe videoCamera.
					
					.. glossary::
					
						port_com
							Define a porta de comunicação com o arduino.
						
						baudrate
							Define a taxa de leitura da comunicação com o arduino.
							
						name_arq
							Define o nome do arquivo onde será escrito os tempos de cada aquisição da classe videoCamera.

**Código descrito acima:**
							
.. code-block:: json
		
	{"cameras":[
		{
		"is_pantilt":"False",
		"controle_pantilt":{
			"comunicacao_serial":{"port_com":"COM4","baudrate":"9600"}
		},
		"video_camera":{},
		"frames":30,
		"port_listen":"8888",
		"is_test":"False",
		"test":{
			"video_camera":{
				"port_com":"COM5",
				"baudrate":"9600",
				"name_arq":"Camera1.txt"
			}}}]
	}
	