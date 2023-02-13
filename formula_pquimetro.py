import math as M
import statistics as S
import numpy as np
from scipy.stats import t



"""
def media(lst_leituras):
    result = 0
    for x in lst_leituras:
        result += x
    retorno = result / len(lst_leituras)
    return retorno
    
def desvio_padrao(lst_leituras,media):
    resultado = 0
    for x in lst_leituras:
       resultado += pow((x - media), 2)
    
    desvio = resultado / len(lst_leituras)
    return desvio

 u = Maior incerteza do padrão
"""


student = {
    '1':  12.710,
    '2':  4.303,
    '3':  3.182,
    '4':  2.776,
    '5':  2.571,
    '6':  2.447,
    '7':  2.365,
    '8':  2.306,
    '9':  2.262,
    '10': 2.228,
    '11': 2.201,
    '12': 2.179,
    '13': 2.160,
    '14': 2.145,
    '15': 2.131,
    '16': 2.120,
    '17': 2.110,
    '18': 2.101,
    '19': 2.093,
    '20': 2.086,
    '21': 2.080,
    '22': 2.074,
    '23': 2.069,
    '24': 2.064,
    '25': 2.060,
    '26': 2.056,
    '27': 2.052,
    '28': 2.048,
    '29': 2.045,
    '30': 2.042,
    '40': 2.021,
    '50': 2.009,
    '60': 2.000,
    '80': 1.990,
    '100': 1.984,
    '120': 1.980,
    'inf': 1.960
    }


def media(lst_leituras):
    result = 0
    for x in lst_leituras:
        result += x
    retorno = result / len(lst_leituras)
    return retorno


def desvio_padrao(lst_leituras,media):
    resultado = 0
    for x in lst_leituras:
       resultado += pow((x - media), 2)
    
    desvio = resultado / (len(lst_leituras) - 1)
    return desvio

    
def fator_k(veff):
    valor_veff = round(veff)
    new_veff = student[f'{valor_veff}']
    resultadok = round(new_veff)
    return resultadok    



def incerteza_padrao(u):
    resultado_incerteza_padrao = (u/2)
    return resultado_incerteza_padrao

def incerteza_teste(desv_padrao):
    resultado_incerteza_teste = desv_padrao / M.sqrt(4)
    return resultado_incerteza_teste

def incerteza_res(res_smc):
    resultado_incerteza_res = ((res_smc /2) / M.sqrt(3))
    return resultado_incerteza_res

def incerteza_combinada(incerteza_padrao, incerteza_teste, incerteza_res, incerteza_deriva, incerteza_curva):
    resultado_incerteza_combinada = 0
    
    if incerteza_curva != 0:
        resultado_incerteza_combinada = M.sqrt((pow(incerteza_padrao, 2) + pow(incerteza_teste, 2) + pow(incerteza_res, 2) + pow(incerteza_deriva, 2) + pow(incerteza_curva, 2)))
        return resultado_incerteza_combinada
    else:
        resultado_incerteza_combinada = M.sqrt((pow(incerteza_padrao, 2) + pow(incerteza_teste, 2) + pow(incerteza_res, 2) + pow(incerteza_deriva, 2)))
        return resultado_incerteza_combinada
    
def veff(incerteza_combinada, incerteza_teste, num_ciclos):
    resultado_veff = (pow(incerteza_combinada, 4) / (pow(incerteza_teste, 4) / (num_ciclos - 1)))
    return round(resultado_veff)

def incerteza(incerteza_combinada, amp):
    resultado_incerteza = (((2 * incerteza_combinada) / amp) * 100)
    return resultado_incerteza

def incerteza_abs(fator_k, incerteza_combinada):
    resultado_incerteza_abs = fator_k * incerteza_combinada
    return resultado_incerteza_abs

def resultado_calibracao():
    
    # medicoes -> lista de valores pegos na calibracao 
    medicoes = [50, 60, 50]
    #  incerteza_p -> resultado da incerteza do padrao utilizado para calibracao 
    u_smp_calc = (0.00011 / 2.00)
    # media_a -> Media dos valores pegos na calibracao
    media_a = media(medicoes)
    #  desvio_p -> valor do desvio padrao tirado apartir da média
    desvio_p = desvio_padrao(medicoes, media_a)
    # incerteza_tes -> incerteza 
    incerteza_tes = incerteza_teste(desvio_p)
    # incerteza_der = incerteza_deriva(incerteza_p)
    variacao_temp = 0
    u_temperatura = (0.000002 / M.sqrt(6)) * (variacao_temp / M.sqrt(3)) * 0.5
    u_res_smc = incerteza_res(0.02)
    e_smp_calc = (0.00002 / M.sqrt(3))  
    erro = (media_a - 50)
    u_rep_smc = (desvio_p / M.sqrt(3))
    # erro = min(erro)
    #incerteza_real = incerteza(incerteza_comb, amp)
    #erro_fiducial_var = erro_fiducial(erro, amp)
    incerteza_comb = incerteza_combinada(u_smp_calc, e_smp_calc, u_rep_smc, u_res_smc, u_temperatura)
    
    veff_var = veff(incerteza_comb, u_rep_smc, len(medicoes))
    fatork = fator_k(veff_var)
    return f'{medicoes} -> incerteza : ;\n media-aritmetica : {media_a} \n desvio padrao: {desvio_p} \n incerteza teste: {incerteza_tes} \n incerteza deriva :  \n incerteza resolução : {u_res_smc} \n incerteza combinada: {incerteza_comb} \n rep:  \n hist:  \n erro_fiducial : \n incerteza real:  \n veff: {veff_var} \n fator_K: {fatork} \n incerteza do padrao no p: {u_smp_calc} \n resp_smc = {u_res_smc} \n u_rep_smc: {u_rep_smc} \n temperatura: {u_temperatura}'
    #return incerteza_comb
print(resultado_calibracao())