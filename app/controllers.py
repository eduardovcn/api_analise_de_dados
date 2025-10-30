from flask import Blueprint, request, jsonify, Response
from pydantic import ValidationError
from . import models
from .schemas import AnaliseInput



#Organização das rotas da API usando Blueprints do Flask
bp = Blueprint('api_v1', __name__)

@bp.route('/analisar', methods=['POST'])
def analisar_dados():
# Método do controlador para lidar com as requisições HTTP

    raw_data = request.get_json()
    if not raw_data:
        return jsonify({"erro": "Dados de entrada ausentes."}), 400
    
    try:
        # Validação dos dados de entrada usando o Pydantic.
        input_data = AnaliseInput.model_validate(raw_data)

    except ValidationError as e:
        #Se falhar, retorna Unprocessable Entity (status 422)
        return Response(e.json(), status=422, mimetype='application/json')  

    # Chamando a lógica das análises.
    resultado = models.calcular_estatisticas(input_data)

    # Salvando o resultado da análise.  
    models.salvar_resultado(resultado)

    return jsonify(resultado.model_dump()), 200  # Retorna o resultado como JSON

# Verificação simples para checar se a API está rodando
@bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "API de Análise de Dados está funcionando."}), 200