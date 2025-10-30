from app import create_app, db

# Cria a aplicação chamando a fábrica
app = create_app()

with app.app_context():
    # Cria todas as tabelas no banco de dados (se não existirem)
    db.create_all()
    print("Banco de dados inicializado e tabelas verificadas/criadas.")

if __name__ == '__main__':
    # Roda o servidor de desenvolvimento do Flask
    # Em produção, você usaria um servidor como Gunicorn ou uWSGI
    app.run(debug=True, port=8000)