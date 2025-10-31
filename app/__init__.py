import os
from flask import Flask, jsonify
from . import controllers
from .extensions import db
from dotenv import load_dotenv
from urllib.parse import quote_plus
from pathlib import Path  # <-- 1. Importe a biblioteca 'Path'

# -----------------------------------------------------------------
# PASSO 1: DEFINIR CAMINHOS DE FORMA ROBUSTA
# -----------------------------------------------------------------
# Path(__file__) é o caminho para este arquivo (__init__.py)
# .parent é a pasta 'app'
# .parent.parent é a pasta raiz do projeto (api_analise_de_dados)
ROOT_DIR = Path(__file__).parent.parent
# O caminho completo para seu .env (ex: C:\Users\eduardo\...\api_analise_de_dados\.env)
ENV_PATH = ROOT_DIR / ".env"

# -----------------------------------------------------------------
# PASSO 2: CARREGUE O ARQUIVO .ENV USANDO O CAMINHO EXPLÍCITO
# -----------------------------------------------------------------
print(f"--- DEBUG: Procurando .env em: {ENV_PATH} ---")
load_dotenv(dotenv_path=ENV_PATH) 

def create_app():
    # Instância principal da aplicação Flask
    app = Flask(__name__)

    # -----------------------------------------------------------------
    # PASSO 3: LEIA AS VARIÁVEIS E DEPURAR
    # -----------------------------------------------------------------
    DB_USER = os.environ.get("DB_USER")
    DB_PASS = os.environ.get("DB_PASSWORD")
    DB_HOST = os.environ.get("DB_HOST", "localhost")
    DB_PORT = os.environ.get("DB_PORT", "5432")
    DB_NAME = os.environ.get("DB_NAME")

    # --- DEBUGGING CRÍTICO ---
    print(f"--- DEBUG: DB_USER lido do .env: {DB_USER}")
    # (Nunca printe a senha inteira, mas vamos ver se ela foi lida)
    if DB_PASS:
        print(f"--- DEBUG: DB_PASS lido do .env: {DB_PASS[:2]}... (lido com sucesso)")
    else:
        print("--- DEBUG: DB_PASS lido do .env: !!!!! FALHOU (None) !!!!!")
    # --- FIM DO DEBUGGING ---

    # Verifica se as variáveis essenciais foram carregadas
    if not all([DB_USER, DB_PASS, DB_NAME]):
        raise ValueError("Erro: Variáveis de banco de dados (DB_USER, DB_PASSWORD, DB_NAME) não definidas no .env ou não lidas.")

    # -----------------------------------------------------------------
    # PASSO 4: CONSTRUÇÃO SEGURA DA URI (COM quote_plus)
    # -----------------------------------------------------------------
    uri_conexao = (
        f"postgresql+psycopg://{quote_plus(DB_USER)}:{quote_plus(DB_PASS)}@"
        f"{quote_plus(DB_HOST)}:{quote_plus(DB_PORT)}/{quote_plus(DB_NAME)}"
    )

    # -----------------------------------------------------------------
    # PASSO 5: CONFIGURAÇÃO DO FLASK
    # -----------------------------------------------------------------
    app.config['SQLALCHEMY_DATABASE_URI'] = uri_conexao
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

    # Inicializa o SQLAlchemy com a aplicação Flask
    db.init_app(app) 

    # Registro do Blueprint das rotas da API
    app.register_blueprint(controllers.bp, url_prefix='/api')

    @app.route('/')
    def read_root():
        return jsonify({"mensagem": "Bem-vindo à API de Análise de Dados!"}), 200
    
    return app