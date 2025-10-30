from flask import Flask, jsonify
from . import controllers
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()  # Carrega variáveis de ambiente do arquivo .env


db = SQLAlchemy() # Instância do SQLAlchemy para gerenciamento do banco de dados


def create_app():
    # Instância principal da aplicação Flask
    app = Flask(__name__)

    # Configuração do banco de dados usando variáveis de ambiente
    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    
    # Desabilita o rastreamento de modificações para economizar recursos.
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)  # Inicializa o SQLAlchemy com a aplicação Flask

    # Registro do Blueprint das rotas da API
    app.register_blueprint(controllers.bp, url_prefix='/api')

    @app.route('/')
    def read_root():
        return jsonify({"mensagem": "Bem-vindo à API de Análise de Dados!"}), 200
    
    return app