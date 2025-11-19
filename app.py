from flask import Flask, request, jsonify
from pypdf import PdfReader
import io
import database
import predictor

app = Flask(__name__)

# Inicializa o banco ao arrancar
database.init_db()

@app.route('/api/status', methods=['GET'])
def status():
    return jsonify({"status": "online", "service": "HEMOSCOPE-X"})

@app.route('/api/pacientes', methods=['POST'])
def criar_paciente():
    data = request.json
    usuario = data.get('usuario_operador', 'sistema')
    pid = database.registrar_paciente(data['nome'], data['cpf'], usuario)
    if pid:
        return jsonify({"msg": "Paciente cadastrado", "id": pid}), 201
    return jsonify({"error": "Erro ao cadastrar"}), 400

@app.route('/api/analisar', methods=['POST'])
def analisar_pdf():
    """
    Recebe o PDF, extrai texto, valida e chama a IA.
    """
    if 'file' not in request.files:
        return jsonify({"error": "Nenhum arquivo enviado"}), 400
    
    file = request.files['file']
    paciente_id = request.form.get('paciente_id')
    usuario = request.form.get('usuario', 'desconhecido')

    # 1. Extração (Parsing)
    try:
        reader = PdfReader(file)
        texto_completo = ""
        for page in reader.pages:
            texto_completo += page.extract_text()
        
        if len(texto_completo) < 50:
            return jsonify({"error": "PDF ilegível ou imagem. Necessário OCR."}), 422

    except Exception as e:
        return jsonify({"error": f"Erro ao ler PDF: {str(e)}"}), 500

    # 2. Análise (IA)
    resultado = predictor.analisar_hemograma_ia(texto_completo)

    # 3. Persistência (Apenas resultados, não o PDF - Minimização de Dados)
    if paciente_id:
        database.salvar_resultado(
            paciente_id, 
            resultado['score'], 
            resultado['classificacao'], 
            resultado['sugestao'], 
            usuario
        )

    return jsonify(resultado)

if __name__ == '__main__':
    # Roda na porta 5000
    app.run(debug=True, port=5000)