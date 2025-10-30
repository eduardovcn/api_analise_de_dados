from flask import Flask, jsonify
from . import controllers

# Este arquivo torna a pasta um pacote Python.

# Função de fábrica para criar a aplicação Flask
def create_app():
    # Instância principal da aplicação Flask
    app = Flask(__name__)

    # Registro do Blueprint das rotas da API
    app.register_blueprint(controllers.bp, url_prefix='/api')

    @app.route('/')
    def read_root():
        return jsonify({"mensagem": "Bem-vindo à API de Análise de Dados!"}), 200
    
    #retorna a aplicação Flask configurada
    return app