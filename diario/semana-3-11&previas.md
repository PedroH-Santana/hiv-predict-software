# HEMOSCOPE-X: Sistema de Apoio à Vigilância Epidemiológica de HIV Baseado em Análise de Hemogramas.

- **Disciplina:** Tópicos em Engenharia de Software
- **Professor: Fabio Nogueira**
- **Grupo:** Cibelle Pires Botelho, Henrique Galvão, Pedro Henrique Santana
- **Data de Início:** 30/09/2025

> **Objetivo deste Registro:** Este documento funciona como um registro cronológico do nosso processo de desenvolvimento. Ele narra a jornada da nossa equipe, começando pela definição de um desafio em saúde pública e avançando até a criação de uma solução de software original. O foco é demonstrar como nossa abordagem metódica de pesquisa, análise e planejamento moldou a forma e a função do projeto final.

****
> 

---

## **Fase 1: Definição do Problema e Escopo**

- **Problema Central:** Identificamos que dados de hemogramas, apesar de baratos e abundantes, são subutilizados para a vigilância em saúde pública. A oportunidade está em analisar esses dados de forma agregada para monitoramento epidemiológico.
- **Objetivo Inicial:** Projetar um software para analisar fluxos de dados de hemogramas e identificar tendências de saúde em nível populacional.
- **Decisões Estratégicas:**
    - **Foco da Solução:** A ferramenta terá um propósito de saúde coletiva (profilaxia e alerta precoce), não de diagnóstico individual.
    - **Requisito de Dados:** O sistema será alimentado por dados de hemogramas padronizados em formato JSON para garantir consistência e interoperabilidade.

### Tarefas para a Próxima Fase

- [x]  Pesquisar e listar os principais parâmetros de um hemograma completo.
- [ ]  Analisar quais desses parâmetros possuem maior relevância para indicar problemas de saúde em escala populacional (epidemias, deficiências nutricionais, etc.).
- [ ]  Avaliar a viabilidade de analisar cada parâmetro de forma automatizada.

---

## Fase 2: Pesquisa de Parâmetros e Refinamento do Escopo ()

### 2.1 Análise Comparativa dos Parâmetros do Hemograma

O diagnóstico do HIV é feito exclusivamente por meio de testes específicos que detectam a presença de anticorpos contra o vírus, dos próprios antígenos (partículas do vírus) ou do material genético viral (RNA) no sangue.

No entanto, um hemograma completo de uma pessoa vivendo com HIV, especialmente em fases mais avançadas da infecção e sem tratamento, pode apresentar algumas **alterações inespecíficas**. É crucial entender que essas alterações não são exclusivas do HIV e podem ser causadas por diversas outras condições, como infecções, doenças autoimunes, deficiências nutricionais, entre outras.

Os critérios ou achados que um médico pode observar em um hemograma e que, **dentro de um contexto clínico suspeito**, podem levantar a necessidade de investigar o HIV, incluem:

1. **Linfopenia (Contagem Baixa de Linfócitos):** Este é o achado mais sugestivo, embora ainda inespecífico. O HIV ataca primariamente as células de defesa chamadas linfócitos T CD4+. Uma queda geral no número total de linfócitos (visível no hemograma) pode ser um sinal indireto de que o sistema imunológico está sendo comprometido.
2. **Anemia:** É comum encontrar uma diminuição no número de glóbulos vermelhos (hemácias) e na hemoglobina. A anemia em pessoas com HIV pode ser causada pela própria infecção crônica, por infecções oportunistas, por deficiências de vitaminas ou como efeito colateral de alguns medicamentos.
3. **Trombocitopenia (Plaquetopenia):** Refere-se à diminuição do número de plaquetas, que são as células responsáveis pela coagulação. Essa condição pode ocorrer em qualquer estágio da infecção pelo HIV.
4. **Neutropenia:** Queda no número de neutrófilos, outro tipo de glóbulo branco importante para combater infecções bacterianas.
5. **Pancitopenia:** Em casos mais graves ou avançados, pode ocorrer uma diminuição de todas as três principais linhagens de células sanguíneas: glóbulos vermelhos (anemia), glóbulos brancos (leucopenia) e plaquetas (trombocitopenia).

---

## Fase 3: Validação da Hipótese e Especificação do Protótipo ()

### 3.1 Levantamento de Fontes Científicas

- *Weiss, G., & Goodnough, L. T. (2005). Anemia of Chronic Disease. NEJM.*
- BRASIL. Ministério da Saúde. Secretaria de Vigilância em Saúde e Ambiente. Departamento de HIV/Aids, Tuberculose, Hepatites Virais e Infecções Sexualmente Transmissíveis.
- *Loprinzi, P. D. (2015). RDW and nutritional-related biomarkers...*
- BRASIL. Ministério da Saúde. Secretaria de Vigilância em Saúde. **Manual Técnico para o Diagnóstico da Infecção pelo HIV em Adultos e Crianças**. Brasília, DF: Ministério da Saúde, 2018
- EVANS, R. H.; SCADDEN, D. T. Hematological aspects of HIV infection. **Baillière's Best Practice & Research Clinical Haematology**, v. 13, n. 2, p. 215-230, 2000.

### Consolidação da Visão do Projeto

> 
> 
> 
> Este projeto de pesquisa visa desenvolver um **software de triagem inteligente** que utiliza modelos de ia generativa ****para analisar anonimamente grandes volumes de resultados de hemogramas do sistema público de saúde (SUS).
> 
> O objetivo não é diagnosticar, mas sim **identificar padrões de alterações hematológicas** (como linfopenia, anemia e trombocitopenia combinadas) que são estatisticamente associadas a uma maior probabilidade de infecção por HIV. O sistema funcionaria como uma **ferramenta de apoio à decisão**, gerando alertas para que profissionais de saúde possam direcionar e otimizar a oferta de testes diagnósticos específicos para pacientes de alto risco, fortalecendo a **detecção precoce e a vigilância ativa**.
> 

---

## Conclusão da Fase de Planejamento e Próximos Passos

A progressão documentada mostra a evolução lógica de um problema amplo até uma solução **clara, viável e inovadora**.

### Próximas Ações

- [x]  Implementar o protótipo em Python.
- [ ]  Criar uma base de testes (massa de arquivos JSON).
- [ ]  Rodar o protótipo e validar os relatórios gerados.
- [ ]  Documentar resultados técnicos.
- [ ]  Preparar a apresentação final do projeto.

[É realmente possível identificar HIV com hemogramas?](https://labvital.com.br/atraves-do-hemograma-e-possivel-diagnosticar-o-paciente-com-hiv/)
