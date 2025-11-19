import google.generativeai as genai
import os
import json

# Configure sua API KEY aqui ou via variável de ambiente
# os.environ["GOOGLE_API_KEY"] = "SUA_CHAVE_AQUI"

def analisar_hemograma_ia(texto_extraido):
    """
    Envia os dados extraídos para o LLM (Gemini) para análise.
    """
    api_key = os.getenv("GOOGLE_API_KEY")
    
    # Mock/Fallback se não houver chave configurada
    if not api_key:
        return {
            "score": 75,
            "classificacao": "Risco Moderado (Simulação - Sem API Key)",
            "sugestao": "Realizar teste confirmatório Western Blot. (Modo Demo)"
        }

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.5-flash')

    prompt = f"""
    Você é um assistente médico especializado em hematologia.
    Analise os dados do hemograma abaixo extraídos de um PDF.
    Verifique padrões sugestivos de infecções virais agudas ou crônicas (como HIV).
    
    DADOS DO HEMOGRAMA:
    {texto_extraido}

    Responda ESTRITAMENTE em formato JSON com as chaves:
    - "score": (inteiro de 0 a 100, onde 100 é alta probabilidade de anomalia viral)
    - "classificacao": (texto curto, ex: "Baixa Probabilidade", "Padrão Sugestivo")
    - "sugestao": (conduta clínica recomendada)
    """

    try:
        response = model.generate_content(prompt)
        # Tratamento básico para extrair o JSON da resposta markdown
        texto_limpo = response.text.replace("```json", "").replace("```", "")
        return json.loads(texto_limpo)
    except Exception as e:
        return {
            "score": 0,
            "classificacao": "Erro na Análise",
            "sugestao": f"Falha ao comunicar com IA: {str(e)}"
        }