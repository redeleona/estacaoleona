Software
========

Detalhamento das etapas para configuração do Software da Estação LEONA
-----------------------------------------------------------------------------------

Acesse o servidor de versionamento GIThub, para isso será necessario instalar o TortoiseSVN na Estação LEONA.

Crie uma pasta na área de trabalho com o nome "Estação LEONA v3.0", clique com o botão direito na pasta e selecione 'SVN Checkout...'

**Utilize o endereço:** 

.. code:: bash

	https://leona.sytes.net/svn/LEONA
	
A Estação possui um login único de acesso que tem permissão somente de leitura.

**Login e senha de acesso:**

.. code:: bash

	Nome de Usuários: estLEONA
	senha: estLEONA
		
Após o checkout três pastas ficaram disponiveis:

.. code:: bash
	
	Instalação
	Código Arduino
	LEONA v3 Tornado

Instalação dos softwares:
^^^^^^^^^^^^^^^^^^^^^^^^^

A pasta 'Instalação' contém alguns softwares que podem ser necessários na Estação LEONA.

Os softwares que obrigatóriamente devem ser instalados estão listados abaixo [#f1]_

**Controle do arduino:**

.. code:: bash

	arduino-1.8.2-windows(x86)

**Drive da placa de aquisição de vídeo:**

.. code:: bash
	
	IVCE-C6XX_Series_Driver_64Bit_V1.2.5

**Desenvolvimento e uso do software da Estação LEONA:**

.. code:: bash
	
	python-3.6.1
	
Código Arduino
^^^^^^^^^^^^^^

**Requisito:**

* IDE Arduino instalado

Esta pasta possui duas outras pastas:

.. code:: bash

	Código osciloscopio

A pasta 'Código osciloscopio' contém o script 'Arduino_python.ino' que é responsável pela comunicação serial feita no software de teste de taxa de transmissão e gravação de imagens.

.. code:: bash

	Pantilt_001_28_08_15
	
A pasta 'Pantilt_001_28_08_15' contém o script 'Pantilt_001_28_08_15.ino' que é responsável pela comunicação serial feita para o controle de movimento do pantilt.

Carregue estes códigos nos Arduinos. Se necessário, utilize o `Tutorial de uso do Arduino <https://youtu.be/rCILKZPG0Kg?t=1134>`_

LEONA v3 TORNADO
^^^^^^^^^^^^^^^^

Dentro da pasta 'LEONA v3 TORNADO' existe a pasta LEONA TORNADO v3.0 com duas pastas:

.. code:: bash
	
	documentacao

Contém a documentação detalhada referente ao software .v3.0 da Estação LEONA.

.. code:: bash
	
	scripts
	
Contém todos os scripts Python para o funcionamento da Estação LEONA. 

**Se todos os passos foram corretamente seguidos, a Estação LEONA está pronta para iniciar a transmissão das imagens.**

Documentação de Software Estação LEONA .v3.0
--------------------------------------------

Para ler a documentação e modo de utilização do software de controle e transmissão da Estação LEONA .v3.0 acesse: `Documentação de Software Estação LEONA v3.0 <Documentação%20de%20Software.html>`_

.. [#f1] **¹Para executar a instalação automática execute o arquivo 'AutoInstalacao.bat' localizado na pasta 'Instalação'. Ao termino das instalações a máquina será automáticamente REINICIADA e o serviço de transmissão e coleta de dados da Estação LEONA será inicializado automaticamente.**
