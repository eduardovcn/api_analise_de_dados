from flask_sqlalchemy import SQLAlchemy


#Para evitar importações circulares, a instância do SQLAlchemy é criada aqui.

db = SQLAlchemy()
