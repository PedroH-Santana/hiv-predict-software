============================================================
       Documento de Especificação de Requisitos de Software (ERS)
       Projeto: HIV-Predict-Software
============================================================

### 1. Introdução

1.1. Propósito do Documento
    (Este documento define os requisitos funcionais e não funcionais 
    do software de análise de hemogramas para auxílio ao 
    diagnóstico de HIV.)

1.2. Escopo do Produto
    (O produto será um sistema baseado em Inteligência Artificial 
    capaz de receber dados de exames de hemograma e fornecer 
    uma análise preditiva ou de suporte à decisão sobre a 
    infecção por HIV.
    
    O sistema *NÃO* se destina a fornecer um diagnóstico 
    definitivo, mas sim a atuar como uma ferramenta de 
    suporte para profissionais de saúde.)


### 2. Descrição Geral

2.1. Perspectiva do Produto
    (O sistema será uma aplicação web (SaaS) independente, 
    hospedada em nuvem.)

2.2. Funções do Produto
    (Resumo: Upload de exames de hemograma em PDF, análise por 
    um motor de IA e apresentação de um score ou parecer 
    de suporte à decisão referente ao HIV.)

2.3. Características dos Usuários (Stakeholders)
    * 2.3.1. Profissional de Saúde (Usuário Operador/Consumidor):
        (Médicos, biomédicos, analistas clínicos e outros profissionais 
        habilitados que utilizam hemogramas. São responsáveis 
        por submeter os exames ao sistema e interpretar os 
        resultados da IA no contexto clínico do paciente.)
    * 2.3.2. Administrador (Clínica):
        (A entidade (clínica ou hospital) que contrata o serviço. 
        Responsável pela gestão de contas de seus profissionais 
        e pela supervisão do uso (auditoria).)

2.4. Restrições Gerais
    * 2.4.1. Conformidade Regulatória (LGPD): 
        (O sistema deve ser estritamente aderente à LGPD. 
        Dados sensíveis de pacientes devem ser tratados com 
        criptografia, controle de acesso rigoroso e, se possível, 
        pseudo-anonimizados durante a análise.)
    * 2.4.2. Conformidade Regulatória (ANVISA):
        (O software deve ser desenvolvido seguindo boas práticas 
        que facilitem o futuro registro ou validação junto à 
        ANVISA como um Software como Dispositivo Médico (SaMD).)
    * 2.4.3. Infraestrutura:
        (O sistema será hospedado em ambiente de nuvem (Cloud), 
        que deve garantir a segurança e a soberania dos dados 
        de saúde.)
    * 2.4.4. Formato de Entrada:
        (O sistema deve aceitar como entrada primária arquivos 
        no formato PDF.)

2.5. Premissas e Dependências
    * 2.5.1. Premissa (Qualidade da Entrada): 
        (Assume-se que os PDFs dos hemogramas são legíveis (texto 
        digital ou OCR de alta qualidade), contendo os marcadores 
        padrão de um hemograma completo.)
    * 2.5.2. Dependência (Modelo de IA):
        (O núcleo do sistema depende de um modelo de IA 
        (Machine Learning) previamente treinado e validado para 
        identificar padrões de HIV em resultados de hemogramas.)


### 3. Requisitos Específicos

#### 3.1. Requisitos Funcionais

(O que o sistema DEVE FAZER)

##### 3.1.1. Módulo: Gestão de Pacientes
* **RF-001:** O sistema deve permitir que o Profissional de Saúde (usuário) cadastre um novo paciente.
    * *Nota:* Os campos de cadastro (ex: nome, ID, data de nascimento) devem ser definidos em conformidade com o princípio de minimização de dados da LGPD.
* **RF-002:** O sistema deve permitir ao usuário pesquisar e selecionar um paciente existente em sua base de dados (da clínica).
* **RF-003:** O sistema deve exibir um histórico de exames e análises já realizadas para um paciente selecionado.

##### 3.1.2. Módulo: Análise de Hemograma (Fluxo Principal)
* **RF-004:** O sistema deve permitir ao usuário realizar o upload de um arquivo de hemograma no formato PDF para um paciente selecionado.
* **RF-005:** O sistema deve ser capaz de extrair (parsear) os dados textuais do PDF do hemograma.
* **RF-006:** O sistema deve identificar e validar os marcadores-chave do hemograma (ex: Leucócitos, Linfócitos, Plaquetas, etc.) a partir do texto extraído.
* **RF-007:** O sistema deve submeter os marcadores validados ao motor de Inteligência Artificial para processamento.

##### 3.1.3. Módulo: Apresentação de Resultados
* **RF-008:** Após a análise da IA, o sistema deve apresentar ao usuário:
    * (a) Um **Score** numérico (ex: 0-100) indicando a probabilidade.
    * (b) Uma **Classificação** textual (ex: "Baixa Probabilidade", "Padrão Sugestivo de Infecção Aguda").
    * (c) Uma **Sugestão** de conduta (ex: "Recomenda-se teste confirmatório", "Monitorar paciente").
* **RF-009:** O sistema deve exibir um *aviso legal* (disclaimer) claro, informando que o resultado é um suporte à decisão e NUNCA substitui o diagnóstico clínico ou exames confirmatórios.
* **RF-010:** O sistema deve salvar o resultado (score, classificação, sugestão) no histórico do paciente (associado ao RF-003).

#### 3.2. Requisitos Não Funcionais (Atributos de Qualidade)

(Como o sistema DEVE SER)

##### 3.2.1. Desempenho
* **RNF-DES-001:** O tempo total de processamento, desde o upload do PDF (RF-004) até a exibição do resultado (RF-008), não deve exceder 180 segundos (3 minutos) em 95% das solicitações.

##### 3.2.2. Segurança e Conformidade (LGPD)
* **RNF-SEG-001:** Todos os dados de identificação pessoal (PII) e dados sensíveis de saúde do paciente devem ser armazenados com **criptografia em repouso** (ex: AES-256) no banco de dados.
* **RNF-SEG-002:** O sistema deve manter **logs de auditoria** detalhados. Qualquer acesso ou ação (criação, leitura, análise) sobre dados de um paciente deve ser registrado, identificando o usuário (quem) e o carimbo de data/hora (quando).
* **RNF-SEG-003 (Minimização de Dados):** O arquivo PDF original (hemograma) **não deve** ser armazenado no sistema após a extração dos dados (RF-005). O sistema deve armazenar apenas os marcadores extraídos e o resultado da análise (score, classificação).
* **RNF-SEG-004:** O sistema deve forçar o *disclaimer* (RF-009) a ser visível e, se possível, exigir que o usuário reconheça (ex: um clique) que o resultado é apenas para suporte.

##### 3.2.3. Confiabilidade (Acurácia da IA)
* **RNF-CONF-001:** O modelo de IA subjacente (motor de análise) deve ser validado e documentado quanto às suas métricas de desempenho antes da implantação.
    * *Nota (Para a equipe de IA/Desenvolvimento):* O requisito "acurácia máxima" do stakeholder será traduzido em métricas mensuráveis (Ex: O modelo deve atingir uma **Sensibilidade** > 9X% e **Especificidade** > 9X% no conjunto de dados de validação clínica).

##### 3.2.4. Usabilidade
* **RNF-USA-001:** O sistema deve ser operável por profissionais de saúde com proficiência básica em informática, sem a necessidade de treinamento extensivo. O fluxo de upload (RF-004) e visualização (RF-008) deve ser concluído em, no máximo, 3 cliques.


