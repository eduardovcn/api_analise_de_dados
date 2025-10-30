from pydantic import BaseModel, Field
from typing import List


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

