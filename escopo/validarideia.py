"""
O código foi desenvolvido primordialmente para validação de ideias
e para testes de implementação de inteligência artificial utilizando
modelos e APIs.

Este **NÃO É O CÓDIGO FINAL** e foi utilizado somente para testes
"""

from google import genai
from google.genai import types
import PyPDF2
from google.colab import userdata
import json



def generate_from_file(file_path):

    try:
        if file_path.lower().endswith('.pdf'):
            with open(file_path, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                file_content = ""
                for page_num in range(len(reader.pages)):
                    file_content += reader.pages[page_num].extract_text()
        else:
            with open(file_path, 'r', encoding='latin-1') as f:
                file_content = f.read()

    except FileNotFoundError:
        return f"Erro: Arquivo não encontrado em {file_path}"
    except Exception as e:
        return f"Erro ao ler o arquivo: {e}"

    client = genai.Client(
        api_key=userdata.get('GOOGLE_API_KEY'),
    )

    model = "gemini-2.5-flash-lite"

    # Load the prompt from the JSON file
    try:
        with open("prompt.json", "r", encoding="utf-8") as f:
            prompt_data = json.load(f)
        system_instruction = f"Persona: {prompt_data['persona']}\n\nContexto: {prompt_data['context']}\n\nTarefa e Formato de Saída Obrigatório:\n{prompt_data['task_and_output_format']}"
    except FileNotFoundError:
        return "Erro: Arquivo de prompt 'prompt.json' não encontrado."
    except KeyError as e:
        return f"Erro: Chave '{e}' não encontrada no arquivo de prompt."


    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=f"""{file_content}"""),
            ],
        ),
    ]
    tools = [
        types.Tool(googleSearch=types.GoogleSearch(
        )),
    ]
    generate_content_config = types.GenerateContentConfig(
        thinking_config = types.ThinkingConfig(
            thinking_budget=0,
        ),
        tools=tools,
        system_instruction=[
            types.Part.from_text(text=system_instruction),
        ],
    )

    response_text = ""
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        response_text += chunk.text

    return response_text

if __name__ == "__main__":
    file_path = "/content/hemograma_completo.pdf"  # Replace with the actual text file path
    response = generate_from_file(file_path)
    print(response)
