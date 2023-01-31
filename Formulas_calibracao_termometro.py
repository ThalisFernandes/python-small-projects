import math as M
import statistics as S
import numpy as np
from scipy.stats import t


def incerteza_combinada(l1, l2, l3, incerteza, k, erro, resolucao, uniformidade, estabilidade):
    mediaCombinadaIncerteza = pow(S.stdev([l1,l2,l3])/2, 2)
    incerteza_k = pow((incerteza/k),2)
    erro2 = pow((erro/M.sqrt(3)),2)
    resolucao_2 = pow((resolucao/ M.sqrt(12)), 2)
    uniformidade_p = pow((uniformidade / M.sqrt(3)), 2)
    estabilidade_p = pow((estabilidade / M.sqrt(3)), 2)
    incerteza_combinada_resultado = M.sqrt(mediaCombinadaIncerteza + incerteza_k + erro2 + resolucao_2 + uniformidade_p + estabilidade_p)
    return round(incerteza_combinada_resultado, 4)


def valor_k(veff_final):
    resultado = 0
    if veff_final == 'infinito':
        resultado = 2
    else:
        resultado = t.ppf(4.55, veff_final)
        
    return resultado  

def valor_veff(l1, l2, l3, incerteza_combinada):
    resultado = 0
    if S.stdev([l1,l2,l3]) == 0:
        resultado = 'infinito'
    else:
        vlr_veff =((pow(incerteza_combinada, 4))/(M.pow((S.stdev([l1,l2,l3]) / 2), 4) /3))
        resultado = vlr_veff
    return resultado


def valor_veff_final(vlr_veff):
    resultado = 0
    if vlr_veff == 'infinito':
        resultado = 'infinito'
    elif vlr_veff <= 100:
        resultado = vlr_veff 
    else:
        resultado = 'infinito'
        
    return resultado
    ...

def incerteza_expandida(incerteza_combinada, fator_k):
    resultado = (incerteza_combinada * fator_k)
    return resultado

incert_vl1 =  incerteza_combinada(-10.21, -10.21, -10.21, 0.2, 2, 0.5, 0.0001, 0.1, 0.8)
veff_vl1 = valor_veff(-10.21, -10.21, -10.21, incert_vl1)
veff_final_vl1 = valor_veff_final(veff_vl1)
k_vl1 = valor_k(veff_final_vl1)
incert_vl2 = incerteza_combinada(0.03, 0.02, 0.04, 0.2, 2, 0.5, 0.0001, 0.1, 0.8)
veff_vl2 = valor_veff(-10.21, -10.21, -10.21, incert_vl2)
veff_final_vl2 = valor_veff_final(veff_vl2)
k_vl2 = valor_k(veff_final_vl2)


print(f'Incerteza vl1 : {incerteza_combinada(-10.21, -10.21, -10.21, 0.2, 2, 0.5, 0.0001, 0.1, 0.8)}; Veff : {valor_veff(-10.21, -10.21, -10.21, incert_vl1)}; Veff Final : {valor_veff_final(veff_vl1)}; K : {valor_k(veff_final_vl1)}; Incerteza Expandida : {incerteza_expandida(incert_vl1, k_vl1)} \n')
print(f'Incerteza vl2 {incerteza_combinada(0.03, 0.02, 0.04, 0.2, 2, 0.5, 0.0001, 0.1, 0.8)} ; Veff : {valor_veff(0.03, 0.02, 0.04, incert_vl2)}; Veff Final : {valor_veff_final(veff_vl2)} ; K : {valor_k(veff_final_vl2)}; Incerteza Expandida : {incerteza_expandida(incert_vl2, k_vl2)} \n')
print(f'Incerteza vl3 {incerteza_combinada(50.12, 50.14, 50.4, 0.2, 2, 0.5, 0.0001, 0.1, 0.8)} ; Veff : {valor_k("infinito")};')
print(f'Incerteza vl4 {incerteza_combinada(100.12, 100.15, 101, 0.2, 2, 0.5, 0.0001, 0.1, 0.8)}; Veff : {valor_k("infinito")};')
print(f'Incerteza vl5 {incerteza_combinada(200.5, 150, 200.4, 0.2, 2, 0.5, 0.0001, 0.1, 0.8)} ; Veff : {valor_k("infinito")};')


