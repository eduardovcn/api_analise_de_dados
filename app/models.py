from pydantic import BaseModel, Field
from typing import List
import numpy as np
import schemas



def calcular_estatisticas(input_data:schemas.AnaliseInput) -> schemas.ResultadoAnalise:
    dados_array = np.array(input_data.dados) # Converte a lista para array numpy multidimensional.
    media = float(np.mean(dados_array))
    mediana = float(np.median(dados_array))
    desvio_padrao = float(np.std(dados_array))
    quantidade = len(dados_array)

    return schemas.ResultadoAnalise(
        media=media,
        mediana=mediana,
        desvio_padrao=desvio_padrao,
        quantidade=quantidade
    )

# Armazenamento em memória, inicialmente. Vou implementar um banco de dados real mais tarde.
_storage: List[schemas.ResultadoAnalise] = []

def salvar_resultado(resultado: schemas.ResultadoAnalise) -> None:
    _storage.append(resultado)
    print(f"Resultado salvo com sucesso. Total: {len(_storage)}")
    