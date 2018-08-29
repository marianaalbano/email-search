# Python-Mail

## Sumário

> * [Introdução](#introdução)
> * [Instalando o módulo](#instalando-o-módulo)
> * [Configurando a conexão](#configurando-a-conexão)
>   * [Linux](#variáveis-de-ambiente-no-linux)
>   * [Windows](#variáveis-de-ambiente-no-windows)

## Introdução

Esse módulo foi criado com o objetivo de realizar a busca de mensagens na caixa de e-mail de forma simplificada e intuitiva utilizando o módulo imaplib para conexão. 


## Instalando o módulo

  - Para a instalação utilize:

  ```bash
  $ pip install email-search 
  ```
  
  
### Configurando a conexão
   A conexão com a caixa de e-mail é feita através de variáveis de ambiente.


  #### Variáveis de ambiente no Linux
   - Configurando o servidor:

      ```bash
      $ export CONNECT='imap.servidor.com' 
      ```
  
   - Configurando o email:

      ```bash
      $ export EMAIL='email@dominio.com' 
      ```
  
   - Configurando a senha:

      ```bash
      $ export PASSWD='password' 
      ```
  
  #### Variáveis de ambiente no Windows
   - Configurando o servidor:

      ```batch
      > set CONNECT='imap.servidor.com' 
      ```
  
   - Configurando o email:

      ```batch
      > set EMAIL='email@dominio.com' 
      ```
  
   - Configurando a senha:

      ```batch
      > set PASSWD='password' 
      ```
