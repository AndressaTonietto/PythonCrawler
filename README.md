# PythonCrawler

## Configuração
Obs: Os passos 1 e 2 só devem ser feitos caso você não tenha instalado o Python anteriormente.
1. Python. Disponível em: https://www.python.org/downloads/
 - Ao instalar o Python, não esqueça de adicionar o mesmo ao PATH caso esteja usando Windows.
2. Virtualenv, disponível pelo pip
`pip install virtualenv`
 - Criar o ambiente no diretório a sua escolha
`virtualenv DIRETORIO`
 - Ativar o virtualenv no diretório selecionado anteriormente
`Scripts/activate`

Criado o ambiente, prosseguir com as dependências.

Obs: Caso use Linux, vá direto ao passo 5.

3. PyWin32: `pip install pywin32`
4. Twisted, com download em https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted
Obs: Baixar a versão compatível com o Python instalado. usar o `pip install` na versão baixada, dentro do diretório criado pelo virtualenv.
5. Scrapy: `pip install scrapy`

## Primeiro Projeto
* Após configurar o ambiente, você pode criar um projeto scrapy com o comando:

`scrapy startproject NOMEDOPROJETO`

* Criado o projeto, acesse a pasta spiders criada pelo scrapy. Para criar um spider:

`scrapy genspider NOMESPIDER SITE`

* Para rodar um spider já criado:

`scrapy runspider NOMESPIDER`

## Este Projeto
* Clone este projeto e realiza o processo de configuração como explicado anteriormente.

* Execute os arquivos `redis-server` e `redis-cli` disponíveis no projeto.

* Acesse a pasta spiders e inicie o mesmo com o comando:

`scrapy runspider prefsctba.py`
