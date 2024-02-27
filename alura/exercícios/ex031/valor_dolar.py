#A API https://economia.awesomeapi.com.br/last/USD-BRL é uma interface que fornece informações sobre a última cotação de câmbio entre o dólar americano (USD) e o real brasileiro (BRL). Em outras palavras, ela retorna o valor mais recente de 1 dólar em reais, com base nas taxas de câmbio disponíveis no momento da solicitação.

import requests

url = "https://economia.awesomeapi.com.br/last/USD-BRL"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    cotacao = float(data['USDBRL']['bid'])
    mensagem = f'U$ 1 dólar corresponde a R${cotacao:.2f}'
    print(mensagem)
else:
    print(f'Falha na requisição dos dados. {response.status_code}')
