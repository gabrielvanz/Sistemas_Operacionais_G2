# https://www.psycopg.org/docs/usage.html
import psycopg2

# Conectar ao banco de dados existente
conn = psycopg2.connect(
    database="exampledb",
    user="docker",
    password="docker",
    host="0.0.0.0"
)

# Abra o cursor para executar a operação do banco de dados
cur = conn.cursor()

# Consultar o banco de dados
cur.execute("SELECT * FROM student")
rows = cur.fetchall()
for row in rows:
    print(row)

# Feche as comunicações com o banco de dados
cur.close()
conn.close()