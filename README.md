# Hello Stone
* Foi desenvolvido uma API com o intuito de gerenciar rotas de clientes e vendedores dado um estabelecimento comercial hipotético.
* Validação de funcionalidades básicas: criação, listagem, consulta, exclusão e autorizações.

## Aspecto geral
* Linguagem Python: versão 3.8.5
* Framework: Django versão 3.1.6
* Banco de dados relacional: sqlite3
* Docker versão 19.03.8
* Token JWT.
* Aplicação dockerizada.
* PyCharm Community Edition, Visual Studio Code ou sua IDE favorita.
* Extensão Docker pelo Visual Studio Code. (opcional)
* Controle de versão GIT instalado na máquina. >Upload na nuvem via Github.


## Iniciando projeto
* PIP (Sistema de gerenciamento de pacotes) deve estar atualizado.
* Python 3.8 deve estar instalado.
* Virtualenv (ambiente virtual) deve estar ativado. Estimulando boas práticas em Python.
* Atenção em 'settings.py', 'urls.py' e o modelo de dados pela aplicação em 'models.py'.

Instalação do Django:
```shell script
$ pip install django
```

I - Django na pasta do projeto. *Com o ambiente virtual ativado
II - Em caso de dúvidas, acesse o diretório para checar dependências.
```shell script
$ cd 'pasta'
$ pip freeze
```

Criando projeto master Django: *Com o ambiente virtual ativado
```shell script
$ cd 'pasta'
$ django-admin startproject hello_django
```

Criando um app Django que se conecta com o projeto master: *Com o ambiente virtual ativado
```shell script
$ cd 'hello_django'
$ django-admin startapp core
```

Pré-iniciação Django administration:
```shell script
$ python manage.py migrate
```

Criando usuário superadmin:
```shell script
$ python manage.py createsuperuser --username admin  
```

Formando o palco na aplicação:
```shell script
$ python manage.py makemigrations core
```

Migração específica para o banco de dados: (opcional)
```shell script
$ python manage.py sqlmigrate core 0001
```

Migração para o banco de dados:
```shell script
$ python manage.py migrate core 0001
```

Autenticação JWT:
```shell script
$ pip install djangorestframework-jwt
$ pip install django-rest-auth django-allauth
```


## Checar dependências
```shell script
$ pip freeze
```

Para executar o projeto no terminal, digite o seguinte comando:

```shell script
$ python manage.py runserver 
```

Visualização do projeto:

```
http://localhost:8000/
```


## Docker
Estimulando boas práticas de programação com Docker:

### Primeiro passo: entrar como root no terminal;

### Criar imagem que vem das instruções do Dockerfiles:
```shell script
$ docker build -t 'tag/create img' .
```

### Verificar imagens no armazenamento local:
```shell script
$ docker images
```

### Verificar containers:
```shell script
$ docker ps
```

### Rodar container:
```shell script
$ docker run -d -p 8000:8000 api/hello_stone
$ curl http://localhost:8000
```


## Material de apoio
* [Python](https://docs.python.org/3.8)
* [Django](https://docs.djangoproject.com)
* [Banco de dados relacional](https://www.oracle.com/database/what-is-a-relational-database)
* [Docker](https://docs.docker.com)
* [PostgreSQL](https://www.postgresql.org/docs)
