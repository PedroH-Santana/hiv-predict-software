# HIV-Predict-Software

Este documento descreve os passos necessários para configurar, instalar as dependências e executar o sistema **HIV-Predict-Software**. O sistema é composto por uma API Backend (Flask) e uma Interface de Usuário (Streamlit) que utilizam Inteligência Artificial (Google Gemini) para auxiliar na análise de hemogramas.

## Pré-requisitos

  * **Python 3.9** ou superior instalado no sistema.
  * Conexão com a internet para instalação de pacotes e comunicação com a API da IA.

-----

## Passo 1: Obter a Chave da API (Google AI Studio)

O sistema utiliza o modelo Gemini da Google para processar os textos extraídos dos PDFs. Para que o sistema funcione, é necessário obter uma chave de acesso gratuita.

1.  Acesse o site do **Google AI Studio** (anteriormente MakerSuite).
2.  Faça login com sua conta Google.
3.  No menu lateral ou no painel principal, localize a opção **Get API key**.
4.  Clique no botão **Create API key**.
5.  Selecione o projeto apropriado ou crie um novo projeto.
6.  Copie a sequência de caracteres gerada (a chave começa geralmente com `AIza...`). **Guarde esta chave, ela será usada no Passo 3.**

-----

## Passo 2: Configuração do Ambiente Virtual (Venv)

É altamente recomendado utilizar um ambiente virtual para isolar as dependências do projeto e evitar conflitos com outras instalações do Python.

### 2.1. Criação do Ambiente

Abra o seu terminal (Prompt de Comando, PowerShell ou Terminal do Linux/Mac) na pasta raiz do projeto e execute o seguinte comando:

```bash
python -m venv venv
```

### 2.2. Ativação do Ambiente

Antes de instalar as bibliotecas, você deve ativar o ambiente virtual. O comando varia conforme o sistema operacional:

**Windows (PowerShell):**

```powershell
.\venv\Scripts\Activate
```

**Windows (Command Prompt - cmd):**

```cmd
.\venv\Scripts\activate.bat
```

**Linux ou macOS:**

```bash
source venv/bin/activate
```

Se a ativação for bem-sucedida, você verá `(venv)` aparecendo no início da linha de comando do seu terminal.

### 2.3. Instalação das Dependências

Com o ambiente ativado, instale todas as bibliotecas necessárias listadas no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

As principais dependências instaladas serão:

  * **flask:** Servidor web para o backend.
  * **streamlit:** Interface visual para o usuário.
  * **pypdf:** Para leitura de arquivos PDF.
  * **google-generativeai:** SDK para comunicação com o Gemini.
  * **cryptography:** Para criptografia dos dados no banco SQLite.
  * **python-dotenv:** Para gerenciamento de variáveis de ambiente.

-----

## Passo 3: Configuração das Variáveis de Ambiente (.env)

Para manter a segurança da sua chave de API, não a insira diretamente no código. Utilizaremos um arquivo `.env`.

1.  Na pasta raiz do projeto (a mesma onde estão `app.py` e `ui.py`), crie um novo arquivo chamado `.env`.
2.  Abra este arquivo com qualquer editor de texto (Bloco de Notas, VS Code, etc.).
3.  Adicione a seguinte linha, substituindo `SUA_CHAVE_COPIADA_AQUI` pela chave que você obteve no **Passo 1**:

<!-- end list -->

```env
GOOGLE_API_KEY=SUA_CHAVE_COPIADA_AQUI
```

4.  Salve e feche o arquivo.

**Nota:** O sistema buscará automaticamente este arquivo para autenticar as requisições junto ao Google.

-----

## Passo 4: Executando o Sistema

Como a arquitetura do sistema é dividida em **Backend** e **Frontend**, é necessário rodar dois processos simultaneamente. Você precisará de **dois terminais** abertos.

### Terminal 1: Iniciando o Servidor Backend (Flask)

1.  Certifique-se de que o ambiente virtual (`venv`) está ativado neste terminal.
2.  Execute o comando:

<!-- end list -->

```bash
python app.py
```

**Resultado esperado:**
O terminal exibirá mensagens indicando que o servidor Flask está rodando, geralmente na porta **5000**.
Exemplo:
`Running on http://127.0.0.1:5000`

Deixe este terminal aberto. Ele processará as requisições de análise e banco de dados.

### Terminal 2: Iniciando a Interface do Usuário (Streamlit)

1.  Abra um **novo** terminal.
2.  Navegue até a pasta do projeto.
3.  Ative o ambiente virtual novamente neste segundo terminal (siga as instruções do Passo 2.2).
4.  Execute o comando:

<!-- end list -->

```bash
streamlit run ui.py
```

**Resultado esperado:**
O Streamlit inicializará e abrirá automaticamente uma nova aba no seu navegador padrão (geralmente no endereço `http://localhost:8501`).

-----

## Utilizando o Sistema

1.  **Cadastro de Paciente:** Na barra lateral da interface web, insira um nome e CPF fictícios e clique em **Cadastrar Paciente**. O sistema retornará um ID.
2.  **Upload e Análise:**
      * Na área principal, insira o **ID do Paciente** que acabou de ser gerado.
      * Faça o upload de um arquivo PDF contendo um hemograma (certifique-se de que o PDF contém texto selecionável, não apenas imagem). Vale ressaltar que o arquivo na branch _main_ [gerar_hemogramaPDF.py](https://github.com/PedroH-Santana/hiv-predict-software/blob/main/gerar_hemogramaPDF.py) permite que você crie um hemograma teste para usar na aplicação.
      * Clique em **Processar e Analisar**.
3.  **Resultados:** Aguarde alguns segundos. O sistema exibirá o Score, Classificação, Sugestão de Conduta e o Aviso Legal.

## Resolução de Problemas Comuns

**Erro: 404 models/gemini-pro is not found**
Isso ocorre se o modelo configurado no código for antigo.

  * **Solução:** Abra o arquivo `predictor.py` e certifique-se de que a linha de definição do modelo está usando `gemini-1.5-flash` ou `gemini-1.5-pro`.

**Erro: Module not found**
Isso ocorre se você tentar rodar o código sem ativar o ambiente virtual ou sem instalar os requisitos.

  * **Solução:** Repita o Passo 2.

**Erro: ConnectionRefusedError na interface**
Isso ocorre se você tentar usar a interface (Streamlit) sem que o backend (Flask) esteja rodando.

  * **Solução:** Verifique se o **Terminal 1** está aberto e sem erros.
