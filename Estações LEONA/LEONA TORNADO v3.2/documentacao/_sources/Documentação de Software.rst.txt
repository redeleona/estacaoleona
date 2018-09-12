:orphan:

Documentação de Software
========================

Esta seção compôe a descrição da arquitetura de software das Estações LEONA.
O software das Estações LEONA foi escrito na linguagem Python.

Para iniciar o controle e transmissão da Estação LEONA inicie o script 'main.py' localizado na pasta 'scripts'.
**Antes de inicializar o serviço, verifique qual porta COM esta conectada ao controle e ao teste.**

Detalhamento da versão 3.0 do software da Estação LEONA v3.0 - Scripts Python:
------------------------------------------------------------------------------

Cada link desta seção representa um script python.

.. toctree::
   :maxdepth: 2
    
   settings
   main
   servidor_tornado_camera_1
   servidor_tornado_camera_2
   servidor_tornado_camera_3
   video_camera
   video_camera_teste
   comunicacao_serial
   controle_pantilt

Gerar automaticamente a documentação de sofware
-----------------------------------------------

A documentação da Estação LEONA v3.0 foi gerada automaticamente com o uso de biblioteca Sphinx, para utilizar o mesmo método com esta ou outras versões do software em python basta seguir os passos abaixo.

Requisitos
----------

Para utilizar a biblioteca Sphinx é necessário que a versão 3.6.1 ou superior do python esteja instalada. Para instalar você pode checar a seção `Software - Detalhamento das etapas para configuração do Software da Estação LEONA <Software.html#detalhamento-das-etapas-para-configuracao-do-software-da-estacao-leona.html>`_

Preparando o esquema básico de documentação
-------------------------------------------

Instalar:

.. code:: bash

	pip install sphinx
	pip install sphinx_rtd_theme

Na pasta dos scripts execute o comando:

.. code :: bash

	md documentacao scripts rst
	
Para iniciar a biblioteca Sphinx execute o comando:

.. code:: bash
	
	sphinx-quickstart
	
Na tela do quickstart altere os comandos:

.. code:: bash

	Project Name: [coloque o nome]
	Author name: [coloque o nome]
	Project Version: [coloque a versão]
	Project release: [coloque a versão de produção]
	Project language: pt_BR
	autodoc[y]: y
	viewcode[y]: y
	Create Makefile[y]: y
	Create Windows command file[y]: y

No arquivo conf.py modifique as linhas:

* Substitua as linhas:

.. code:: python	

	# import os
 	# import sys
	# sys.path.insert(0, os.path.abspath('.'))
	
* Pelas linhas:

.. code:: python	

	import os
	import sys
	sys.path.insert(0, os.path.abspath('../scripts'))
	import sphinx_rtd_theme

* Para garantir que a a def __init__ será automaticamente documentada adicione a linha:

.. code:: python
	
	autoclass_content = 'both'

* Na seção # -- General configuration ---

Na linha:

.. code:: python

	# The master toctree document
	master_doc = 'index'
	
Altere 'index' para:

.. code:: python

	master_doc = 'RedeLeonaDoc'

* Na linha # -- Options for HTML output -----#

Comente:
	
.. code:: python
	
	html_theme = 'alabaster'

E insira:

.. code:: python

	html_theme = "sphinx_rtd_theme"
	html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

Execute o comando:

.. code:: bash

	make html
	
Aviso:Todos os scripts python devem estar na pasta "scripts"!
Executar o comando:	

.. code:: bash

	sphinx-apidoc -o ./rst ./scripts
	cd rst
	md _static
	
Recorte o script "conf.py" e "index.rst" para a pasta criada "rst".
		
Execute o comando:

.. code:: bash
	
	cd ..

Execute o comando:

.. code:: bash

	sphinx-build -b html ./rst ./documentacao	
	
Pronto! A estrutura básica de documentação foi gerada!

Você pode conferir na pasta "documentacao" na arquivo 'RedeLeonaDoc.html'

Exemplo de código python para gerar auto documentação
-----------------------------------------------------

Código de Exemplo do padrão de documentação em Python:

.. code-block:: python

	import cv2, time

	class testeCamera:
	"""Classe para testar funcionamento da câmera"""
	
	def __init__(self, captura):
		"""Recebe camera
		
		:type captura: object
		:param captura: recebe caminho de leitura da câmera
		"""
		
			self.captura0 = cv2.VideoCapture(0)
			#time.sleep(3)
			#captura1 = cv2.VideoCapture(0)

		def start(self):
		""" Inicia leitura da camera"""
		
			while(1):
				ret0, frame0 = self.captura0.read()
				""":variável frame0: (matrix de string) Imagens capturada da câmera"""
				cv2.imshow("Video - 0", frame0)
				
			k = cv2.waitKey(30) & 0xff
			if k == 27:
				break

		def __del__(self):
		"""Finaliza transmissão da camera"""
			
			captura0.release()
			#captura1.release()
			cv2.destroyAllWindows()

**AVISO: O arquivo settings.json não é automaticamente documentado, qualquer alteração deve ser feita diretamente no arquivo 'settings.rst', seção: 'Arquivo de configuração settings.json'.**
			
Referências
-----------

* Tutorial em vídeo:

	`Video Youtube em inglês <https://www.youtube.com/watch?v=qrcj7sVuvUA>`_.

* Exemplo de documentação:

	`Pythonhosted <https://pythonhosted.org/an_example_pypi_project/sphinx.html>`_.

	`Sphinx <http://www.sphinx-doc.org/en/stable/ext/example_google.html>`_.
	