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
## Histórias de Usuário (Backlog Inicial)
- **US1 (Core):** Eu, como profissional de saúde, quero fazer o upload do hemograma do meu paciente (PDF), para que o sistema possa extrair os dados e me retornar uma análise sobre a possibilidade desse paciente possuir HIV.
- **US2 (Valor Agregado):** Eu, como profissional de saúde, quero que o sistema destaque quais indicadores do hemograma levaram à suspeita, para me auxiliar na identificação técnica dos vestígios do vírus.
- **US3 (UI/UX):** Eu, como profissional de saúde, preciso de uma interface simples de upload de arquivos PDF e um retorno visual claro, indicando se há vestígios (Sim/Não) e listando as informações que levaram a essa decisão.

# Plano do Sprint
A equipe de 3 pessoas agora tem tarefas integradas para o desenvolvimento do MVP em Streamlit.

## Definição de Papéis:
- **Dev 1 (Streamlit/UI):** Foca na interface (componentes `st.file_uploader`, `st.metric`, visualização de texto).
- **Dev 2 (Data/Lógica):** Foca na extração de texto do PDF (`pdf_parser.py`) e estruturação dos dados para envio.
- **Dev 3 (IA/LLM):** Foca na engenharia de prompt para detecção de padrões e explicação médica.

## Cronograma de Tarefas:
| Tarefa | História | Responsável | Estimativa (Horas) |
|--------|----------|-------------|-------------------|
| Configurar ambiente (venv, pip install streamlit, pypdf) | U$1 | Dev 1 | 1h |
| Criar módulo pdf_parser.py (Extração de texto do PDF) | U$1 | Dev 2 (Data) | 3h |
| Criar módulo predictor.py (Configuração da API LLM) | U$1 | Dev 3 (IA) | 2h |
| app.py: Criar UI de upload e validação de arquivo | U$1, US$3 | Dev 1 (UI) | 4h |
| predictor.py: Prompt para análise de risco (Lógica da US1) | U$1 | Dev 3 (IA) | 6h |
| predictor.py: Prompt para destacar evidências/justificativas | US$2 | Dev 3 (IA) | 6h |
| app.py: Lógica do botão "Analisar" (Integra Parser + LLM) | U$1 | Dev 2 (Data) | 5h |
| app.py: UI de exibição de resultados e justificativas | US$3 | Dev 1 (UI) | 6h |
| Refinamento dos Prompts (Melhorar acurácia da análise) | US$2 | Dev 3 (IA) | 4h |
| Integração Final, Testes de Usabilidade e Bugfix | - | Todos | 6h |
| **Total** | | | **43 horas** |

## Diagrama Proposto
![Diagrama](diagram.png)

