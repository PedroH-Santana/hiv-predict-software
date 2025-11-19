import sqlite3
import datetime
from cryptography.fernet import Fernet
import os

# Configuração de Segurança: Gera ou carrega uma chave de criptografia
key_file = 'secret.key'
if not os.path.exists(key_file):
    key = Fernet.generate_key()
    with open(key_file, 'wb') as key_file_out:
        key_file_out.write(key)
else:
    with open(key_file, 'rb') as key_file_in:
        key = key_file_in.read()

cipher_suite = Fernet(key)

DB_NAME = "hemoscope.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Tabela de Pacientes (Dados Pessoais Criptografados)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pacientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_encrypted BLOB NOT NULL,
            cpf_encrypted BLOB UNIQUE NOT NULL
        )
    ''')

    # Tabela de Histórico de Análises (Minimização de dados: Apenas resultados)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS historico (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            paciente_id INTEGER,
            data_analise TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            score INTEGER,
            classificacao TEXT,
            sugestao TEXT,
            FOREIGN KEY(paciente_id) REFERENCES pacientes(id)
        )
    ''')

    # Tabela de Logs de Auditoria (Rastreabilidade)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS auditoria (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT,
            acao TEXT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

def encrypt_data(data):
    return cipher_suite.encrypt(data.encode())

def decrypt_data(token):
    return cipher_suite.decrypt(token).decode()

def log_action(usuario, acao):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO auditoria (usuario, acao) VALUES (?, ?)", (usuario, acao))
    conn.commit()
    conn.close()

def registrar_paciente(nome, cpf, usuario_admin):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Verifica se existe
    # Nota: Em produção, a busca em dados criptografados requer estratégias de hash cego (blind index).
    # Aqui faremos inserção direta para simplificação do protótipo.
    
    try:
        cursor.execute("INSERT INTO pacientes (nome_encrypted, cpf_encrypted) VALUES (?, ?)", 
                       (encrypt_data(nome), encrypt_data(cpf)))
        conn.commit()
        log_action(usuario_admin, f"Cadastro de paciente ID: {cursor.lastrowid}")
        return cursor.lastrowid
    except sqlite3.IntegrityError:
        return None # CPF já existe (simplificado)
    finally:
        conn.close()

def salvar_resultado(paciente_id, score, classificacao, sugestao, usuario_admin):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO historico (paciente_id, score, classificacao, sugestao)
        VALUES (?, ?, ?, ?)
    """, (paciente_id, score, classificacao, sugestao))
    conn.commit()
    log_action(usuario_admin, f"Análise salva para paciente ID: {paciente_id}")
    conn.close()