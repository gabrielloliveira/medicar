# Medicar API

API feita com intuito de um cumprir este desafio backend 👉🏽 https://github.com/Intmed-Software/desafio

## Como rodar o projeto

- Certifique-se que tenha o python >= 3.7
- Clone o projeto
- Crie um virtualenv ```python -m venv env```
- Ative o virtualenv ```source env/bin/active```
- Instale os requerimentos do projeto ```pip install -r requirements.txt```
- Faça o setup das variáveis de ambiente ```python contrib/generate_env.py```
- Gere o BD Sqlite de teste ```python manage.py migrate```
- Crie um superusuario ```python manage.py createsuperuser```

Criei um arquivo do Insomnia de exemplo o botei na raiz do projeto, para caso haja a necesisdade de uso.