import os
from flask import Flask, jsonify
from . import controllers
from .extensions import db
from dotenv import load_dotenv
from urllib.parse import quote_plus
from pathlib import Path 

# Definindo o caminho raiz do projeto
# Path(__file__) é o caminho para o __init__.py
# .parent aponta para 'app'
# .parent.parent aponta para a raiz do projeto
ROOT_DIR = Path(__file__).parent.parent

# O caminho completo para seu .env (ex: C:\Users\eduardo\...\api_analise_de_dados\.env)
ENV_PATH = ROOT_DIR / ".env"


load_dotenv(dotenv_path=ENV_PATH) 

def create_app():

    # Instância principal da aplicação Flask
    app = Flask(__name__)

    # Carregando variáveis de ambiente para configuração do banco de dados    
    DB_USER = os.environ.get("DB_USER")
    DB_PASS = os.environ.get("DB_PASSWORD")
    DB_HOST = os.environ.get("DB_HOST", "localhost")
    DB_PORT = os.environ.get("DB_PORT", "5432")
    DB_NAME = os.environ.get("DB_NAME")

    # Verifica se as variáveis essenciais foram carregadas
    if not all([DB_USER, DB_PASS, DB_NAME]):
        raise ValueError("Erro: Variáveis de banco de dados (DB_USER, DB_PASSWORD, DB_NAME) não definidas no .env ou não lidas.")

    # Construindo a URI de forma mais organizada e segura.
    uri_conexao = (
        f"postgresql+psycopg://{quote_plus(DB_USER)}:{quote_plus(DB_PASS)}@"
        f"{quote_plus(DB_HOST)}:{quote_plus(DB_PORT)}/{quote_plus(DB_NAME)}"
    )

    # Configurações do SQLAlchemy para a aplicação Flask
    app.config['SQLALCHEMY_DATABASE_URI'] = uri_conexao
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

    # Inicializa o SQLAlchemy com a aplicação Flask
    db.init_app(app) 

    # Registro do Blueprint das rotas da API
    app.register_blueprint(controllers.bp, url_prefix='/api')

    
    return app