from app import create_app

# Cria a aplicação chamando a fábrica
app = create_app()

if __name__ == '__main__':
    # Roda o servidor de desenvolvimento do Flask
    # Em produção, você usaria um servidor como Gunicorn ou uWSGI
    app.run(debug=True, port=8000)