# bibliotecas

import numpy as np



def sharpe_ratio(returns, free_risk_i, dias_ano = 256):
    '''
    Função que calcula sharpe ratio (medida de desempenho ajustada ao risco) anualizado de um ativo ou portfolio.
    
    Parâmetros:    
    - returns: retornos diários do ativo ou portfolio
    - free_risk_i: taxa de juros livre de risco 
    - dias_ano: número de dias úteis no ano (padrão 256 dias)

    Referência:
    - Bell, S. (2016). Quantitative finance for dummies. John Wiley & Sons.

    Observação:
    - Taxa livre de risco no Brasil (SELIC).
    - Futuro: automatizar scrap de SELIC (https://www.bcb.gov.br/estabilidadefinanceira/selicdadosdiarios).

    '''
    # converter free_risk_i para seu valor médio diário
    free_risk_i /= dias_ano
    
    # calcular sharpe ratio anualizado
    sharpe = np.sqrt(dias_ano) * (returns.mean()- free_risk_i) / returns.std()

    # margem de erro do sharpe ratio
    sharpe_error_margin = np.sqrt(256/len(returns))

    return sharpe, sharpe_error_margin







