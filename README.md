# API de Análise de Dados

Este projeto é uma API simples construída em Python para fins de estudo, demonstrando o padrão de arquitetura clássico **MVC (Model-View-Controller)**.

A API expõe um único endpoint que recebe uma lista de números e retorna suas principais estatísticas (média, mediana, desvio padrão e quantidade).

## Tecnologias Utilizadas

* **Python 3.10+**
* **Flask:** Para a construção da API (o **Controller**).
* **Pydantic:** Para a definição e validação dos modelos de dados (o **Model**).
* **NumPy:** Para os cálculos estatísticos (a lógica de negócio dentro do **Model**).

## Arquitetura 

Para esta API, utilizei o padrão MVC, que divide a aplicação em três responsabilidades principais:

* `app/models.py`: O **Model (Modelo)**.
  * Contém a definição das estruturas de dados (com Pydantic: `AnaliseInput`, `ResultadoAnalise`).
  * Contém a lógica de negócio principal (a função `calcular_estatisticas`).
  * Contém a lógica de persistência (a função `salvar_resultado` e o _storage_ em memória).

* `app/controllers.py`: O **Controller (Controlador)**.
  * Define as rotas/endpoints da API usando um Flask Blueprint.
  * Recebe as requisições HTTP (`request`).
  * Valida os dados de entrada *chamando* o Modelo.
  * Executa a lógica de negócio *chamando* o Modelo.
  * Retorna a resposta formatada (`jsonify`), que atua como a **View (Visão)**.

* `app/__init__.py` e `run.py`: São os arquivos de "cola" e inicialização, responsáveis por criar a instância do Flask e registrar o Controlador.

## Como Executar o Projeto

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/eduardovcn/api_analise_de_dados.git](https://github.com/eduardovcn/api_analise_de_dados.git)
    cd api_analise_de_dados
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    python -m venv venv
    ```
    * No Windows: `.\venv\Scripts\activate`
    * No Linux/macOS: `source venv/bin/activate`

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute o servidor:**
    ```bash
    python run.py
    ```
    O servidor estará rodando em `http://127.0.0.1:8000`.

## Endpoints da API

Você pode testar os endpoints usando ferramentas como Postman, Insomnia ou cURL.

---

### `POST /v1/analisar`

Recebe uma lista de números e retorna suas estatísticas.

**Request Body (Exemplo):**
```json
{
  "dados": [10, 20, 30, 40, 50, 50, 60]
}
```
**Response Body 200 - Sucesso:**
```json
{
  "media": 37.142857142857146,
  "mediana": 40.0,
  "desvio_padrao": 17.13926868853112,
  "quantidade": 7
}
```
**Response Body 422 - Erro de validação:**
```json
[
  {
    "loc": [
      "dados"
    ],
    "msg": "ensure this value has at least 1 items",
    "type": "value_error.list.min_items",
    "ctx": {
      "limit_value": 1
    }
  }
]
```



