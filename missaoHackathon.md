# Planejamento Ágil Simplificado
> [chat do gemini](https://gemini.google.com/share/e8b5b9f13cb7)

## Prompt
O prompt utilizado para gerar os seguintes dados está exposto abaixo. Depois do resultado gerado, ainda pedi para que a saída fosse ainda mais simplificada e reduzida a uma só linguagem, Python.
```
Sua Missão: o desafio é claro: projetar e codificar uma funcionalidade central.
Planejamento Ágil: transforme suas Histórias de Usuário em um backlog inicial e um plano de sprints. Dentro disso, crie uma lista de histórias de usuário a partir da descrição da ideia: Por meio de uma análise de dados estruturados, o Hemoscope-X deve prever a progressão da doença HIV, a eficácia de tratamentos e o risco de resistência a medicamentos, servindo como uma ferramenta de apoio à decisão para profissionais de saúde.
Verifique se a lista de histórias de usuário está coerente.
Crie um plano de sprints para a implementação das histórias de usuário. Este plano deve considerar uma equipe de 3 colaboradores, trabalhando 4 horas por semana perfazendo um total de 48 horas. Se for o caso, identifique quais histórias de usuário não podem ser implementadas tendo em vista o esforço disponível.
Arquitetura Inteligente: gere diagramas de arquitetura (usando formatos como PlantUML ou Mermaid) e o esquema do banco de dados. A arquitetura, naturalmente, deve ser uma proposta de software que satisfaz os requisitos. Crie um diagrama de arquitetura que identifique os principais componentes necessários para implementação das histórias de usuário
Gere a documentação correspondente para cada um dos componentes identificados.
Revise o planejamento. Provavelmente o planejamento deve ser atualizado para refletir o conhecimento acumulado com a definição da arquitetura e dos componentes.
```

## História de Usuários (Backlog Inicial)
- US1 (Core): Eu, como profissional de saúde, quero fazer o upload de dados estruturados de um paciente (ex: CSV, JSON contendo histórico de CD4, carga viral, genotipagem) para que o sistema possa analisá-los.
- US2 (Core): Eu, como profissional de saúde, quero selecionar um paciente e visualizar a previsão de progressão da doença (ex: mudança estimada na Carga Viral/CD4) nos próximos 6 meses, para ajustar o monitoramento.
- US3 (Core): Eu, como profissional de saúde, quero selecionar um paciente e visualizar o risco de resistência aos medicamentos antirretrovirais (TARV) atuais, para tomar decisões informadas sobre a terapia.
- US4 (Valor Agregado): Eu, como profissional de saúde, quero simular a eficácia de diferentes esquemas de tratamento (ex: mudar Medicamento A para B) e ver a previsão de progressão resultante.
- US5 (UI/UX): Eu, como profissional de saúde, quero ter um dashboard simples que liste meus pacientes cadastrados e seus níveis de risco atuais (Progressão/Resistência) em um piscar de olhos.
> Verificação de Coerência: O conjunto de histórias está coerente. Elas cobrem o fluxo central: Entrada de Dados (US1), Processamento/Predição (US2, US3) e Apoio à Decisão (US3, US4). A US5 fornece a interface de visualização.

## Plano do Sprint
A equipe de 3 pessoas agora tem tarefas muito mais integradas:

Dev 1 (Flask/UI): Foca na interface (componentes st.file_uploader, st.button, st.line_chart).
Dev 2 (Data/Lógica): Foca no parser dos dados e na lógica de banco de dados (SQLite/Pandas).
Dev 3 (IA/LLM): Foca no módulo de predição (chamadas ao LLM).

| Tarefa | História (US) | Responsável (Dev) | Estimativa (Horas) |
| --------------------- | --------------------- | --------------------- | --------------------- |
| Configurar ambiente (venv, pip install streamlit) | Todos | Dev 1 | 1h |
| Criar módulo database.py | US1 | Dev 2 | 2h |
| Criar módulo predictor.py (função de chamada LLM) | US2, US3 | Dev 3 | 2h |
| app.py: Criar UI de upload (US1) | US1 | Dev 1 (UI) | 4h |
| database.py: Salvar dados do upload no SQLite | US1 | Dev 2 (Data) | 6h |
| predictor.py: Criar prompt e lógica para US2 (Progressão) | US2 | Dev 3 (IA) | 8h |
| predictor.py: Criar prompt e lógica para US3 (Resistência) | US3 | Dev 3 (IA) | 6h |
| app.py: Lógica do botão "Analisar" (Chamar DB e Predictor) | US2, US3 | Dev 2 (Data) | 6h |
| app.py: UI de visualização dos resultados (US2, US3) | US2, US3 | Dev 1 (UI) | 8h |
| Integração Final e Testes	|   | Todos | 5h |
| Total | | | 48 horas |

## Diagrama Proposto
![mermaidlive-diagram](diagram.png)

### Database.py Proposto
Em vez de SQL puro, a IA gera o módulo database.py que cria o banco de dados.
```
# Módulo: database.py
import sqlite3

# O arquivo do banco de dados
DB_FILE = "hemoscope.db"

# SQL para criar as tabelas (o mesmo schema, mas em sintaxe SQLite)
SQL_CREATE_TABLES = """
CREATE TABLE IF NOT EXISTS Patients (
    patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    age INT,
    gender VARCHAR(10)
);

CREATE TABLE IF NOT EXISTS ClinicalData (
    data_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER REFERENCES Patients(patient_id),
    reading_date DATE NOT NULL,
    cd4_count INT,
    viral_load INT,
    current_treatment_regimen TEXT,
    UNIQUE(patient_id, reading_date)
);

CREATE TABLE IF NOT EXISTS Predictions (
    prediction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER REFERENCES Patients(patient_id),
    prediction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    predicted_cd4_6mo INT,
    predicted_viral_load_6mo INT,
    resistance_risk_score REAL
);
"""

def initialize_database():
    """Cria o arquivo .db e as tabelas se não existirem."""
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.executescript(SQL_CREATE_TABLES) # Executa múltiplos statements
        conn.commit()
        print("Banco de dados SQLite inicializado com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao inicializar o banco de dados: {e}")
    finally:
        if conn:
            conn.close()

# (Aqui também entrariam funções como: 
#  def add_patient_data(patient_data): ...)
#  def get_patient_history(patient_id): ...)
# )
```
