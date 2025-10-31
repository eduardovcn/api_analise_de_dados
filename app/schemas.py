from pydantic import BaseModel, Field
from typing import List


#DTOs (Data Transfer Objects). Definem a "forma" dos dados que entram e saem da API.

class AnaliseInput(BaseModel):
    # Lista de dados numéricos para análise estatística.
    dados: List[float] = Field(..., min_items=1)

class ResultadoAnalise(BaseModel):
    
    media: float
    mediana: float
    desvio_padrao: float
    quantidade: int

