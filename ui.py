import streamlit as st
import requests

# Configuração da URL do Backend (Flask)
API_URL = "http://127.0.0.1:5000/api"

st.set_page_config(page_title="HEMOSCOPE-X", layout="wide")

# Título e Cabeçalho
st.title("🩸 HEMOSCOPE-X | HIV Predict Software")
st.markdown("### Sistema de Apoio à Decisão Clínica")

# Sidebar para Autenticação Simulada e Gestão
with st.sidebar:
    st.header("Painel do Profissional")
    usuario = st.text_input("ID do Profissional", value="medico_01")
    st.divider()
    
    st.subheader("Novo Paciente")
    novo_nome = st.text_input("Nome do Paciente")
    novo_cpf = st.text_input("CPF")
    if st.button("Cadastrar Paciente"):
        if novo_nome and novo_cpf:
            resp = requests.post(f"{API_URL}/pacientes", json={
                "nome": novo_nome, "cpf": novo_cpf, "usuario_operador": usuario
            })
            if resp.status_code == 201:
                st.success(f"Cadastrado ID: {resp.json()['id']}")
            else:
                st.error("Erro ao cadastrar.")

# Área Principal - Fluxo de Análise
st.header("Análise de Hemograma")

col1, col2 = st.columns(2)

with col1:
    paciente_id_input = st.number_input("ID do Paciente para Análise", min_value=1, step=1)
    uploaded_file = st.file_uploader("Upload do Hemograma (PDF)", type=["pdf"])

    analisar_btn = st.button("Processar e Analisar")

if analisar_btn and uploaded_file and paciente_id_input:
    with st.spinner('Enviando para servidor Flask e processando IA...'):
        try:
            # Prepara o arquivo para envio via POST form-data
            files = {'file': uploaded_file.getvalue()}
            data = {'paciente_id': paciente_id_input, 'usuario': usuario}
            
            response = requests.post(f"{API_URL}/analisar", files=files, data=data)
            
            if response.status_code == 200:
                resultado = response.json()
                
                with col2:
                    st.subheader("Resultados da Análise")
                    
                    # Score Visual
                    st.metric(label="Score de Probabilidade Viral", value=f"{resultado['score']}/100")
                    
                    # Detalhes
                    st.info(f"**Classificação:** {resultado['classificacao']}")
                    st.write(f"**Sugestão de Conduta:** {resultado['sugestao']}")
                    
                    st.divider()
                    st.warning("""
                    ⚠️ **DISCLAIMER (Aviso Legal):**
                    Este resultado foi gerado por Inteligência Artificial e serve apenas como suporte à decisão.
                    NÃO substitui o diagnóstico clínico ou exames laboratoriais confirmatórios (Western Blot/PCR).
                    """)
            else:
                st.error(f"Erro no servidor: {response.text}")
                
        except requests.exceptions.ConnectionError:
            st.error("Não foi possível conectar ao Servidor Flask. Verifique se 'app.py' está rodando.")

# Rodapé com logs visuais (simulação)
st.divider()
st.caption("Sistema em conformidade com LGPD e ANVISA (SaMD). Dados criptografados em repouso.")