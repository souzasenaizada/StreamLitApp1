import sqlite3

# Função para conectar ao banco
def get_connection():
    conn = sqlite3.connect("funcionarios.db", check_same_thread=False)
    return conn
# Criar tabela se não existir
def criar_tabela():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS funcionarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cargo TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
        )
    """)          
    conn.commit()
    conn.close()

def inserir_funcionario(nome, cargo, email):
   conn = get_connection()
   cursor = conn.cursor()
   cursor.execute("INSERT INTO FUNCIONARIOS (nome, cargo, email) VALUES (?,?,?)", (nome, cargo, email))
   conn.commit()
   conn.close()
   
def listar_funcionarios():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM funcionarios")
    data = cursor.fetchall()
    conn.close()
    return data