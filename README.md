# CNAB-archive

## Tabela de Conteúdos

- [Visão Geral](#1-visão-geral)
- [Tecnologias Utilizadas](#2-tecnologias-utilizadas)
- [Rodar Localmente](#3-rodar-localmente)

---

## 1. Visão Geral

Aplicação com o objetivo de criar uma interface web que aceite upload de arquivos CNAB, onde os dados serão normalizados e armazenados em um banco de dados relacional.

## 2. Tecnologias Utilizadas

Logo abaixo temos a lista de tecnologias usadas:

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)

## 3. Rodar Localmente

- Crie o ambiente virtual em seu terminal

```shell
python -m venv venv
```

- Inicie o venv

Linux
```shell
source venv/bin/activate
```

Windows
```shell
.\venv\Scripts\activate
```

- Instalando as dependências

```shell
pip install -r requirements.txt
```

- Executando as migrações

```shell
python manage.py migrate
```

- Iniciando o servidor

```shell
python manage.py runserver
```
