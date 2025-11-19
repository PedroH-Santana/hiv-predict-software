"""
Este script foi desenvolvido apenas para testar
o produto HEMOSCOPE-X com dados reais presentes em
um hemograma que indicam possível contaminação por HIV
"""

from fpdf import FPDF
import random
from datetime import datetime

class PDF(FPDF):
    def header(self):
        # Logo / Nome do Laboratório
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'LABORATÓRIO DE ANÁLISES CLÍNICAS FICTÍCIO', 0, 1, 'C')
        self.set_font('Arial', '', 10)
        self.cell(0, 5, 'Rua Exemplo, 123 - Cidade/UF - Tel: (00) 1234-5678', 0, 1, 'C')
        self.ln(10)

    def footer(self):
        self.set_y(-30)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Este documento é uma simulação gerada por IA para fins de teste/design.', 0, 1, 'C')
        self.cell(0, 5, f'Página {self.page_no()}', 0, 0, 'C')

def gerar_hemograma():
    pdf = PDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    # --- Dados do Paciente ---
    pdf.set_font('Arial', 'B', 11)
    pdf.cell(0, 8, f'Paciente: João da Silva (ID: {random.randint(1000,9999)})', 0, 1)
    pdf.set_font('Arial', '', 11)
    pdf.cell(50, 8, f'Idade: 34 anos', 0, 0)
    pdf.cell(50, 8, f'Sexo: Masculino', 0, 0)
    pdf.cell(0, 8, f'Data: {datetime.now().strftime("%d/%m/%Y")}', 0, 1)
    
    pdf.line(10, 45, 200, 45) # Linha separadora
    pdf.ln(5)

    # --- Configuração da Tabela ---
    col_w = [60, 40, 30, 60] # Larguras das colunas
    
    def criar_cabecalho_tabela():
        pdf.set_font('Arial', 'B', 10)
        pdf.set_fill_color(230, 230, 230)
        pdf.cell(col_w[0], 8, 'Exame', 1, 0, 'L', 1)
        pdf.cell(col_w[1], 8, 'Resultado', 1, 0, 'C', 1)
        pdf.cell(col_w[2], 8, 'Unidade', 1, 0, 'C', 1)
        pdf.cell(col_w[3], 8, 'Referência', 1, 1, 'C', 1)
        pdf.set_font('Arial', '', 10)

    # --- Eritrograma ---
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'ERITROGRAMA', 0, 1, 'L')
    criar_cabecalho_tabela()
    
    dados_eritro = [
        ['Hemácias', '4,85', 'milhões/mm³', '4,50 a 5,90'],
        ['Hemoglobina', '14,8', 'g/dL', '13,0 a 17,5'],
        ['Hematócrito', '44,2', '%', '40,0 a 52,0'],
        ['VCM', '91,1', 'fL', '80,0 a 100,0'],
        ['HCM', '30,5', 'pg', '27,0 a 32,0'],
        ['CHCM', '33,5', 'g/dL', '32,0 a 36,0'],
        ['RDW', '13,2', '%', '11,5 a 14,5'],
    ]

    for row in dados_eritro:
        pdf.cell(col_w[0], 7, row[0], 1)
        pdf.cell(col_w[1], 7, row[1], 1, 0, 'C')
        pdf.cell(col_w[2], 7, row[2], 1, 0, 'C')
        pdf.cell(col_w[3], 7, row[3], 1, 0, 'C')
        pdf.ln()

    pdf.ln(5)

    # --- Leucograma ---
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'LEUCOGRAMA', 0, 1, 'L')
    criar_cabecalho_tabela()
    
    # Dados baseados no visualizador acima
    dados_leuco = [
        ['Leucócitos Totais', '6.800', '/mm³', '4.000 a 11.000'],
        ['Neutrófilos (58%)', '3.944', '/mm³', '1.600 a 8.000'],
        ['Linfócitos (30%)', '2.040', '/mm³', '900 a 4.000'],
        ['Monócitos (7%)', '476', '/mm³', '200 a 1.000'],
        ['Eosinófilos (4%)', '272', '/mm³', '0 a 500'],
        ['Basófilos (1%)', '68', '/mm³', '0 a 200'],
    ]

    for row in dados_leuco:
        pdf.cell(col_w[0], 7, row[0], 1)
        pdf.cell(col_w[1], 7, row[1], 1, 0, 'C')
        pdf.cell(col_w[2], 7, row[2], 1, 0, 'C')
        pdf.cell(col_w[3], 7, row[3], 1, 0, 'C')
        pdf.ln()
        
    pdf.ln(5)

    # --- Plaquetas ---
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'PLAQUETAS', 0, 1, 'L')
    criar_cabecalho_tabela()
    
    dados_plaq = [
        ['Contagem de Plaquetas', '245.000', '/mm³', '150.000 a 450.000'],
        ['VPM', '10,5', 'fL', '6,5 a 12,0'],
    ]

    for row in dados_plaq:
        pdf.cell(col_w[0], 7, row[0], 1)
        pdf.cell(col_w[1], 7, row[1], 1, 0, 'C')
        pdf.cell(col_w[2], 7, row[2], 1, 0, 'C')
        pdf.cell(col_w[3], 7, row[3], 1, 0, 'C')
        pdf.ln()

    # --- Assinatura ---
    pdf.ln(20)
    pdf.line(70, pdf.get_y(), 140, pdf.get_y())
    pdf.set_font('Arial', '', 10)
    pdf.cell(0, 5, 'Dr. Exemplo Genérico', 0, 1, 'C')
    pdf.cell(0, 5, 'CRF/CRM: 123456', 0, 1, 'C')
    pdf.cell(0, 5, 'Bioquímico Responsável', 0, 1, 'C')

    # Salvar
    pdf.output("Hemograma_Simulado.pdf")
    print("PDF gerado com sucesso: 'Hemograma_Simulado.pdf'")

if __name__ == "__main__":
    gerar_hemograma()
