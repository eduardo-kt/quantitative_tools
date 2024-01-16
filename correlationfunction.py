import pandas as pd
import numpy as np

def correlation_function(serie1,serie2,window):
    '''
    Uma função que calcula a correlação entre duas séries (ativos) rolando os dados de acordo com window
    
    Parâmtetros:
    - serie1, serie2: séries de dados
    - window: intervalo (número de períodos) de cada rolagem

    Output:
    - série com correlações para cada bloco de cada rolagem

    Referência: 
    Clenow, A. F. (2019). Trading evolved: Anyone can build killer trading strategies in Python.
    '''

    return1 = serie1.pct_change()
    return2 = serie2.pct_change()

    correlation = return1.roling(window).corr(serie2)

    return correlation