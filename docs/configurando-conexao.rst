####################
Configurando conexão
####################

A conexão com a caixa de email é feita através de variáveis de ambiente.


.. _admin-params:

Linux
=====
As variáveis de ambiente podem ser definidas no Linux como abaixo.

Configurando o servidor:

.. highlight:: bash
   :linenothreshold: 5

.. code-block:: bash

   $ export CONNECT_IMAP='imap.servidor.com'


Configurando o email:

.. highlight:: bash
   :linenothreshold: 5

.. code-block:: bash

   $ export EMAIL='email@dominio.com'


Configurando a senha:

.. highlight:: bash
   :linenothreshold: 5

.. code-block:: bash

   $ export PASSWD='password'


Windows
=======

As variáveis de ambiente podem ser definidas no Windows como abaixo.

Configurando o servidor:

.. highlight:: bash
   :linenothreshold: 5

.. code-block:: bash

   > set CONNECT_IMAP='imap.servidor.com'


Configurando o email:

.. highlight:: bash
   :linenothreshold: 5

.. code-block:: bash

   > set EMAIL='email@dominio.com'


Configurando a senha:

.. highlight:: bash
   :linenothreshold: 5

.. code-block:: bash

   > set PASSWD='password'