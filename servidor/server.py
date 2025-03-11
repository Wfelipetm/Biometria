from app import create_app
from app.database import get_db_connection  

app = create_app()

# Testar conexão ao iniciar o servidor
conn = get_db_connection()
if conn:
    print("Conectado ao banco de dados com sucesso!")
    conn.close()
else:
    print("Falha ao conectar ao banco de dados.")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)







