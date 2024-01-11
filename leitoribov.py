# bibliotecas

import pandas as pd

def leitor_ibov(path):
    '''
    Uma função para organizar uma lista de ativos em formato adequado ao yfinance e yahooquery

    Inputs:
    - arquivo csv

    Output:
    - série com os tickers dos ativos que compõem o iBovespa
    - Dataframe com os dados do iBovespa
    
    Parâmetros:
    - path: o caminho até o arquivo .csv com os dados da B3

    Referências:
    - ..

    Observação:
    - dados do iBov disponível em: https://www.b3.com.br/pt_br/market-data-e-indices/indices/indices-amplos/indice-ibovespa-ibovespa-composicao-da-carteira.htm
    - Futuro: automatizar o scrap do site da B3.
    '''
    
    # ler o arquivo (opções condizentes com o arquivo)
    data = pd.read_csv(path,sep=';',skiprows=2,skipfooter=2,encoding='latin1',engine='python', names=['code','name','type','quantity','share(%)','Unnamed: 5'])
    
    # eliminar colunas indesejáveis
    data = data.drop(columns='Unnamed: 5', axis=1)

    # modificar separador decimal de ',' para '.'
    data['share(%)'] = data['share(%)'].apply(lambda x: float(str(x).replace(',','.')))
    
    # acrescentar formatação condizente com yfinance e yahooquery
    data['code'] = data['code'].apply(lambda x: x + '.SA')

    # ordenar dados
    data = data.sort_values(by=['share(%)'], ascending=False)
    
    # eliminar índice
    data.reset_index(inplace=True, drop=True)
    
    # separar os tickers
    tickers = data['code']
    
    
    return data, tickers