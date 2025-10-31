import numpy as np
from datetime import datetime, timezone
from .schemas import AnaliseInput, ResultadoAnalise
from .extensions import db


# Definindo o ORM Model. 

class ResultadoAnaliseDB(db.Model): # db.Model:Define a estrutura da tabela no banco de dados usando SQLAlchemy

    # Nome da tabela no banco de dados
    __tablename__ = 'resultados_analise'

    # primary_key=True: Marca esta coluna como a chave primária (ID único)
    id = db.Column(db.Integer, primary_key=True)

    media = db.Column(db.Float, nullable=False)
    mediana = db.Column(db.Float, nullable=False)
    desvio_padrao = db.Column(db.Float, nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    data_criacao = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    # Representação em string do objeto para facilitar a depuração
    def __repr__(self):
        return f"<ResultadoAnaliseDB {self.id}: {self.media}, {self.mediana}, {self.desvio_padrao}, {self.quantidade}, {self.data_criacao}>"
    


def calcular_estatisticas(input_data:AnaliseInput) -> ResultadoAnalise:

    dados_array = np.array(input_data.dados) # Converte a lista para array numpy multidimensional.
    
    media = float(np.mean(dados_array))
    mediana = float(np.median(dados_array))
    desvio_padrao = float(np.std(dados_array))
    quantidade = len(dados_array)

    resultado = ResultadoAnalise(
        media=media,
        mediana=mediana,
        desvio_padrao=desvio_padrao,
        quantidade=quantidade
    )
    return resultado


def salvar_resultado(resultado: ResultadoAnalise) -> None:

    # Convertendo o resultado da análise para o modelo ORM do banco de dados (Pydantic -> SQLAlchemy)
    novo_resultado_db = ResultadoAnaliseDB(
        media=resultado.media,
        mediana=resultado.mediana,
        desvio_padrao=resultado.desvio_padrao,
        quantidade=resultado.quantidade
    )

    db.session.add(novo_resultado_db)  # Adiciona o novo resultado à sessão do banco de dados

    try:
        db.session.commit() # Salva (commita) a transação no banco de dados.
        print(f"INFO: Resultado da análise salvo com sucesso: {novo_resultado_db.id}")

    except Exception as e:
        db.session.rollback() # Reverte a transação em caso de erro.
        print(f"ERROR: Falha ao salvar resultado da análise: {e}")