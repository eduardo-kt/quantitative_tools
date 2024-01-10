# bibliotecas
import numpy as np
import pandas as pd


def absolute_differenc_first_last_price(serie):
    '''
    diferença absoluta entre a primeira e a última observação de uma série
    '''
    return abs(serie.iloc[-1]-serie.iloc[0])

def absolute_sum_price_difference(serie):
    '''
    somatório dos valores absolutos das diferenças entre duas observações consecutivas de uma série
    '''
    return abs(serie.diff()).sum()


def ef_ratio(serie, window):
    '''
    Implementação do Efficiency Ratio.
    
    Parâmetros:
    - serie = uma série de dados (e.g. preços de fechamento)
    - window = número de dias para a rolagem dos dados
    
    Referência:
    - Kaufman, P. J. (2020). Trading systems and methods (Sixth edition). Wiley.


    Observação:
    - ef_ratio varia entre 0 (noise extremo alto) e 1 (noise extremo baixo ou sem noise)
    '''
    
    ef_ratio_numerator = serie.rolling(window).agg(absolute_differenc_first_last_price)
    ef_ratio_denominator = serie.rolling(window).agg(absolute_sum_price_difference)

    return ef_ratio_numerator/ef_ratio_denominator


