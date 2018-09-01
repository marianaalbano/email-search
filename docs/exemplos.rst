########
Exemplos
########

Este tópico tem como objetivo demostrar a utilização do módulo e seus métodos.


.. _admin-params:


Configuração Inicial
====================

.. highlight:: python
   :linenothreshold: 5

.. code-block:: python

   from python_mail.Search import Search

    search = Search("inbox")
    id_messages = search.search_subject('Subject Message')
    data_messages = search.result_message(id_messages)

    for message in data_messages:
        print(message)




.. note:: A configuração inicial consiste em passar a caixa na qual será feita a pesquisa das mensagens.


Métodos disponíveis
===================

Os métodos disponíveis deste módulo são:

:file:`search_body(str)` filtra as mensagens pelo campo "Body", ou seja, filtra no corpo da mensagem.

:file:`search_from(str)` filtra as mensagens pelo campo "From", ou seja, faz uma pesquisa pelo remetente da mensagem.

:file:`search_subject(str)` filtra as mensagens pelo campo "Subject", ou seja, filtra no assunto da mensagem.

.. note:: Todos os métodos de filtro de mensagens que estão listados acima devem receber como parâmetro uma string e retorna o ID das mensagens que foram encontradas.

:file:`result_message([list])` retorna o conteúdo completo das mensagens: data, from, to, subject e body.

:file:`result_date([list])` retorna a data das mensagens.

:file:`result_from([list])` retorna o remetente das mensagens.

:file:`result_to([list])` retorna o destinatário das mensagens.

.. note:: Todos os métodos para o retorno do conteúdo deve receber como parâmetro uma lista contendo um ou mais IDs das mensagens.