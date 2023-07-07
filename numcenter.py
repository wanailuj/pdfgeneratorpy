from fpdf import FPDF
from jinja2 import Environment, FileSystemLoader

# Defina o caminho para o arquivo HTML
arquivo_html = 'arqhtml.html'

# Configurações do PDF
opcoes_pdf = {
    'page-size': 'Letter',
    'margin-top': '0mm',
    'margin-right': '0mm',
    'margin-bottom': '0mm',
    'margin-left': '0mm',
}

# Carregar o conteúdo do arquivo HTML usando o Jinja2
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template(arquivo_html)
html_content = template.render()

# Criar a classe do PDF personalizada com a função de cabeçalho e rodapé
class MyPDF(FPDF):
    def header(self):
        pass

    def footer(self):
        self.set_y(-10)
        self.set_font('Helvetica', 'I', 8)
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")

# Inicializar o objeto PDF personalizado
pdf = MyPDF()
pdf.set_auto_page_break(auto=True, margin=0)
pdf.add_page()

# Adicionar o conteúdo HTML ao PDF
pdf.write_html(html_content)

# Salvar o PDF com o conteúdo e as páginas numeradas
pdf.output('output_com_paginas.pdf')

print("PDF gerado com sucesso.")