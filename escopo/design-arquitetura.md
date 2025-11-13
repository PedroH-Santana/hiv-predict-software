# Arquitetura do Sistema

## Arquitetura em Nuvem SaaS:
O sistema será uma aplicação web hospedada em nuvem, facilitando acesso remoto e escalabilidade, conforme descrito no escopo do produto, entretanto seus testes serão hospedados localmente.

## Camadas da Arquitetura:

### Camada de Apresentação (Front-end):
Interface web para interação dos profissionais de saúde e administradores, permitindo upload de hemogramas em PDF, visualização de resultados e administração de contas.

### Camada de Aplicação (Back-end):
Lógica de negócio, incluindo validação, processamento dos dados extraídos, comunicação com o motor de IA e gerenciamento do histórico de análises.

### Camada de Dados:
Banco de dados seguro para armazenamento criptografado das informações essenciais do paciente, resultados preditivos e logs de auditoria.

### Serviço de IA:
Motor de Machine Learning previamente treinado responsável pela análise dos dados do hemograma e geração do score, classificação e sugestão.

## Segurança e Conformidade:

* Criptografia AES-256 para dados sensíveis em repouso.

* Controle rigoroso de acesso e auditoria de operações para conformidade com LGPD e boas práticas ANVISA.

* Minimização de dados: não armazenar o PDF original após extração.

## Design do Sistema

### Módulos Funcionais:

* Gestão de Pacientes: Cadastro, pesquisa e seleção dos pacientes com dados minimizados e controlados.

### Upload e Processamento de Hemogramas:

* Upload de arquivos PDF.

* Extração e parsing dos dados (marcadores-chave do hemograma).

* Validação desses marcadores.

### Análise de IA:

* Envio dos dados validados para o motor de IA.

* Recebimento do score numérico, classificação textual e sugestão de conduta.

### Apresentação de Resultados:

* Exibição do score, classificação, sugestão e aviso legal (disclaimer).

* Armazenamento dos resultados no histórico.

### Auditoria e Logs:

* Registro detalhado de acessos e operações para segurança e rastreamento.

### Fluxo Principal:

1. Usuário (profissional de saúde) loga e seleciona/cadastra um paciente.

2. Realiza upload do PDF do hemograma.

3. Sistema processa o PDF, extrai dados e valida.

4. Dados são enviados ao motor de IA para análise.

5. Apresentação dos resultados ao usuário com disclaimer.

6. Resultados e logs são armazenados com criptografia.

### Considerações de Usabilidade e Desempenho:

* Interface simples e direta, com máximo de 3 cliques para upload e visualização.

* Tempo de processamento máximo esperado: 180 segundos em 95% das operações.