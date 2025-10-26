from pydantic import BaseModel, Field
from typing import List
import numpy as np

class AnaliseInput(BaseModel):
    # Lista de dados numéricos para análise estatística.
    dados: List[float] = Field(..., min_items=1)

class ResultadoAnalise(BaseModel):
    # Média dos dados fornecidos.
    media: float
    # Mediana dos dados fornecidos.
    mediana: float
    # Desvio padrão dos dados fornecidos.
    desvio_padrao: float
    # Quantidade de dados fornecidos.
    quantidade: int


def calcular_estatisticas(input_data:AnaliseInput) -> ResultadoAnalise:
    dados_array = np.array(input_data.dados)
    media = float(np.mean(dados_array))
    mediana = float(np.median(dados_array))
    desvio_padrao = float(np.std(dados_array))
    quantidade = len(dados_array)

    return ResultadoAnalise(
        media=media,
        mediana=mediana,
        desvio_padrao=desvio_padrao,
        quantidade=quantidade
    )