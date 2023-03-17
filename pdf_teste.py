from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter,A4
from reportlab.platypus import Frame,Table, Paragraph
import pandas as pd
import matplotlib as matlb
import io
import mysql.connector  as con
import math as m




config = {
    'user':'root', 
    'password':'Lempe8596@R3cife',
    'host': 'localhost',
    'database':'lempe'
}
con = con.connect(**config)

cursor = con.cursor()

def rep(number):
    return "{number:06}".format(number=int(number))

def montar_obj_cliente():
    query_cliente = 'SELECT nome, razao_social, telefone, endereco FROM clientes WHERE id_clientes = 180;'
    cursor.execute(query_cliente)
    cliente_data = cursor.fetchall()
    chaves = ['nome', 'razaosocial', 'telefone', 'endereco']
    obj_cliente = {chaves[x]:cliente_data[0][x]  for x in range(0,len(cliente_data[0]))}
    return obj_cliente


def montar_lista_instrumento():
    query_instrumento = 'SELECT nome_instrumento, cod_tag_instrumento,num_serie, tag, modl.nome_modelo, fab.nome_fabricante, insTipo.nome_tipo FROM instrumento JOIN fabricante as fab ON instrumento.fabrincante = fab.id_fabricante JOIN tipo_instrumento as insTipo ON instrumento.tipo_instrumento = insTipo.id_tipo JOIN modelo_instrumentos as modl ON instrumento.modelo = modl.id_modelo WHERE id_instrumento = 10;'
    cursor.execute(query_instrumento)
    instrumento_data = cursor.fetchall()
    chaves = ['nome', 'tag', 'numserie', 'tag', 'modelo', 'fabricante', 'tipo', '']
    obj_instrumento = {chaves[x]: instrumento_data[0][x] for x in range(0, len(instrumento_data[0]))}
    obj_instrumento['local_calibracao'] = 'laboratorio'
    obj_instrumento['faixa'] = 'faixa_teste'
    obj_instrumento['resolucao'] = '0 a 2000mm'
    return obj_instrumento

    
num_inicial = 1


"""
    1 - informações do cliente;
    2 - informações do instrumento;
    3 - informações da calibracao;
    4 - informações do padrão;
    5 - informações do procedimento 
    6 - tabela de resultados
    7 - Observações
    8 - assinatura
"""
    
def generate_pdf():
    from reportlab.pdfbase.pdfmetrics import stringWidth
    buffer = io.BytesIO()
    nomedoPDF = 000000
    nextpdf = 1
    vlr_atual = 11
    year = 2023
    if num_inicial == 1 and vlr_atual == 1:
        numcertificado = rep(num_inicial)
    else :
        vlr_atual = vlr_atual + 1
        numcertificado = rep(vlr_atual)
    nome_relatorio = f'certificado_{numcertificado}_{year}.pdf'
    canvas_interface = canvas.Canvas(nome_relatorio, pagesize=A4, bottomup=0)
    text = canvas_interface.beginText()
   
    cliente = montar_obj_cliente()
    instrumento = montar_lista_instrumento()
    certificado_titulo = f'CERTIFICADO DE CALIBRAÇÃO N° {numcertificado}/{year}'
    # Desenhando o titulo do certificado
    
    text.setTextOrigin(((A4[0] - stringWidth(certificado_titulo, 'Helvetica', 14)) / 2.0), 85)    
    text.setFont('Helvetica', 12)
    text.textLine(certificado_titulo)
    canvas_interface.drawText(text)
    
    #----------------------------------------------
    
    text.setTextOrigin(38, 98.8)
    text.setFont('Helvetica', 9)
    
    #--Montando a área do cliente--------------------------------------
    
    cliente_data = [
              f'',
              f'1 - Dados do Solicitante',
              f'__________________________________________________________________________________________',
              f'Cliente: {cliente["nome"]}',
              f'Endereço: {cliente["endereco"]}',
              f'Solicitabte: ',
              f'Endereço: ',
    ]
    
    for line in cliente_data:
        text.textLine(line)
    
   
    
    #--Dados instrumento------------------------------------------------
    instrumento_data = [
              f'2 - Dados do Instrumento Calibrado',
              f'___________________________________________________________________________________________',
              f'Instrumento:    {instrumento["nome"]}       Local da Calibração: {instrumento["local_calibracao"]}',
              f'Identificação: {instrumento["numserie"]}    Faixa de Indicação: {instrumento["faixa"]}',
              f'Número de Série: {instrumento["numserie"]}  Resolução:   {instrumento["resolucao"]}',
              f'Modelo: {instrumento["modelo"]}             Faixa de Calibração:  {instrumento["faixa"]}',
              f'Fabricante:   {instrumento["fabricante"]}   Ordem de serviço:  ',
              f'Localização:                                Data da Calibração: ',
              f'Classe:                                     Data de Emissão: ',
              f''
    ]
    
    for line in instrumento_data:
        text.textLine(line)
        
   
    
    #---Dados do Ambiente---------------------------------------------
    ambiente = [
              f'3 - Dados do Ambiente',
              f'___________________________________________________________________________________________',
              f'Temperatura:                               Umidade Relativa:  ',
              f''
    ]
    
    
    #-----------------------------------------------------------------
    
    #--Padrões Utilizados---------------------------------------------
    padroes_strings = [
            f'4 - Padrões Utilizados',
            f'___________________________________________________________________________________________',
            f'',
            f'Código      Descrição    Certificado      Rastreabilidade    Validade            ',
            f'',
            f'',
            f'',
            f'',
            f'',
            f'',
            f''
        ]
    
    for instLine in padroes_strings:
        text.textLine(instLine)
    
    
    # Montando o procedimento para o certificado ---------------------
    
    query_procedimento = f'SELECT procedimento, procedimento_desc FROM procedimento WHERE procedimento_id'
        
    
    #-----------------------------------------------------------------
    procedimento_string = [
              f'5 - Procedimento',
              f'___________________________________________________________________________________________',
              f'',
              f'',
              f'',
              f'',
              f'',
    ]
    
    for line in procedimento_string:
        text.textLine(line)
        
    
    #-----------------------------------------------------------------
    
    #-----Montagem da tabela------------------------------------------
    
    table = [
        ['Pressão Indicada UNIDADES', 'Pressão Referência mmhg'],
        ['SI', 'INSTR. mmhg'],
        ['Primeiro Ciclo', 'Segundo Ciclo'],
        ['0','0', '0,000', '0,000', '0,000','0,000'],
        ['20', '20', '20,000', '20,000', '20,000', '20,000']
    ]
    
    t = Table(table)
    
    tabela_calibração = [
              f'6 - Resultados da Calibração',
              f'____________________________________________________________________________________________',
              f'',
              f'',
              f'',
              f'',
              f'',
              f'',
              f'',
              f'',
              f'',
              f'',
              f'',
              f''
              ]
    
    
    
    for line in tabela_calibração:
        text.textLine(line)
    
        
    consideracoes_abaixo_da_tabela = [
              f'CARACTERÍSTICA METROLÓGICAS APRESENTADAS EM RELAÇÃO A AMPLITUDE DA FAIXA DE CALIBRAÇÃO:(%)',           
              f' INCERTEZA DE MEDIÇÃO:                  REPETITIVIDADE:            ',
              f' ERRO FIDUCIAL(ÍNDICE DA CLASSE):            HISTERESE:            ',
              f'',
              f''
        ]
    for line in consideracoes_abaixo_da_tabela:
        text.textLine(line)
        
        
    #-----------------------------------------------------------------
    string = [
              f'7 - Observações',
              f'___________________________________________________________________________________________',
              f'A incerteza expandida de medição relatada é declarada como a incerteza padrão da medição ',
              f'  multiplicação pelo '
              ]
    
    for line in string:
        text.textLine(line)
    
    canvas_interface.drawText(text)
    canvas_interface.showPage()
    canvas_interface.save()
    buffer.seek(0)
    
    return 0


def generate_certificado():
    buffer = io.BytesIO()
    cnv = canvas.Canvas
    ...

#generate_pdf()

def table_generator():
    from tabulate import tabulate
        
    table = [
        ['0','0', '0,000', '0,000', '0,000','0,000'],
        ['20', '20', '20,000', '20,000', '20,000', '20,000']
    ]
    theadpt1 = ['Pressão Indicada UNIDADES', 'Pressão Referência mmhg']
    theadpt2 = ['SI', 'INSTR. mmhg']
    theadpt3 = ['Primeiro Ciclo', 'Segundo Ciclo']
    print(tabulate(table, headers=['PRESSÃO INDICADA UNIDADES', 'PRESSÃO DE REFERÊNCIA']))
    return 0

table_generator()
    
    
    
    
        
    