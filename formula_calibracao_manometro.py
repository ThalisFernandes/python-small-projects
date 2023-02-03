import math as M
import statistics as S
import numpy as np
from scipy.stats import t



"""
fórmulas para fazer calibração em manômetro,

   * Desvio padrão *
   
   µ = (ti - Ma)² / n

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
"""
 u = Maior incerteza do padrão
"""
def u():
    ...
    

def incerteza_padrao(u):
    resultado_incerteza_padrao = (u/2)
    return resultado_incerteza_padrao

def incerteza_teste(desv_padrao):
    resultado_incerteza_teste = desv_padrao / M.sqrt(4)
    return resultado_incerteza_teste

def incerteza_res(res_smc):
    resultado_incerteza_res = ((res_smc /2) / M.sqrt(6))
    return resultado_incerteza_res

def incerteza_deriva(incerteza_padrao):
    resultado_incerteza_deriva = (incerteza_padrao / M.sqrt(3))
    return resultado_incerteza_deriva

def incerteza_curva(max_curva):
    resultado_incerteza_curva = max_curva / M.sqrt(3)
    return resultado_incerteza_curva

def incerteza_combinada(incerteza_padrao, incerteza_teste, incerteza_res, incerteza_deriva, incerteza_curva):
    resultado_incerteza_combinada = 0
    
    if incerteza_curva != 0:
        resultado_incerteza_combinada = M.sqrt((pow(incerteza_padrao, 2) + pow(incerteza_teste, 2) + pow(incerteza_res, 2) + pow(incerteza_deriva, 2) + pow(incerteza_curva, 2)))
        return resultado_incerteza_combinada
    else:
        resultado_incerteza_combinada = M.sqrt((pow(incerteza_padrao, 2) + pow(incerteza_teste, 2) + pow(incerteza_res, 2) + pow(incerteza_deriva, 2)))
        return resultado_incerteza_combinada
    
def veff(incerteza_combinada, incerteza_teste, num_ciclos):
    resultado_veff = (pow(incerteza_combinada, 4) / (pow(incerteza_teste, 4) / (num_ciclos -1)))
    return resultado_veff

def incerteza(incerteza_combinada, amp):
    resultado_incerteza = (((2 * incerteza_combinada) / amp) * 100)
    return resultado_incerteza

def incerteza_abs(fator_k, incerteza_combinada):
    resultado_incerteza_abs = fator_k * incerteza_combinada
    return resultado_incerteza_abs

def rep(erro1, amp):
    resultado_rep = 0
    if erro1 == 0 and amp == 0:
        return resultado_rep
    resultado_rep = (erro1 / amp) / 100
    return resultado_rep

def hist(erro2, amp):
    resultado_hist = 0
    if erro2 ==0 and amp == 0:
        return resultado_hist
    resultado_hist = (erro2 / amp) * 100
    return resultado_hist

def erro_fiducial(erro, amp):
    resultado_erro_fiducial = (erro / amp) / 100
    return resultado_erro_fiducial

def resultado_calibracao():
    medicoes = [250, 250,250,250]
    incerteza_p = incerteza_padrao(0.04)
    media_a = media(medicoes)
    desvio_p = desvio_padrao(medicoes, media_a)
    incerteza_tes = incerteza_teste(desvio_p)
    incerteza_der = incerteza_deriva(incerteza_p)
    incerteza_reso = incerteza_res(0.1)
    incerteza_comb = incerteza_combinada(incerteza_p, incerteza_tes, incerteza_reso, incerteza_der, 0)
    erro1 = (medicoes[0] - medicoes[1])
    erro2 = (medicoes[2] - medicoes[3])
    min_amp = 0
    max_amp = max(medicoes)
    amp = (max_amp - min_amp)
    rep_var = rep(erro1, amp)
    hist_var = hist(erro2, amp)
    validacao1 = (8 - max(medicoes))
    validacao2 = (8 - min(medicoes))
    erro = [validacao1, validacao2]
    erro = min(erro)
    incerteza_real = incerteza(incerteza_comb, amp)
    erro_fiducial_var = erro_fiducial(erro, amp)
    
    return f'{medicoes} -> incerteza : {incerteza_p};\n media-aritmetica : {media_a} \n desvio padrao: {desvio_p} \n incerteza teste: {incerteza_tes} \n incerteza deriva : {incerteza_der} \n incerteza resolução : {incerteza_reso} \n incerteza combinada: {incerteza_comb} \n rep: {rep_var} \n hist: {hist_var} \n erro_fiducial : {erro_fiducial_var} \n incerteza real: {incerteza_real}'
    #return incerteza_comb
print(resultado_calibracao())
    
    
   