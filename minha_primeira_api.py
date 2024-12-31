import requests
import json

#link escolhendo a moeda importada pela API
cotacao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
#formatando de json para python
cotacao = cotacao.json()

#Solicitando ao usuario um input
Moeda_escolhida= input ("Qual moeda voce deseja consultar a cotação?\n1 - Dólar Americano/Real Brasileiro\n2 - Euro/Real Brasileiro\n3 - Bitcoin/Real Brasileiro\nResposta: ")

def new_func(Moeda_escolhida):
    try :
        Moeda_escolhida = int(Moeda_escolhida)
    except ValueError:
        print("Por Favor escolha um número.")
    except IndexError:
        print('Índice não existe na lista')
    except Exception:
        print('Erro desconhecido')
    return Moeda_escolhida

while True:

    Moeda_convertida_em_int = new_func(Moeda_escolhida)

    if Moeda_convertida_em_int == 1 :
        #----------------------- Qual moeda - Qual parametro
        cotacao_dolar = cotacao ['USDBRL']["bid"]
        print(f'A cotação do dolar atualmente esta: {cotacao_dolar} URL')

    elif Moeda_convertida_em_int == 2:
        #----------------------- Qual moeda - Qual parametro
        cotacao_euro = cotacao ['EURBRL']['bid']
        print(f'A cotação do Euro atualmente esta: {cotacao_euro} EUR')

    elif Moeda_convertida_em_int == 3:
        #----------------------- Qual moeda - Qual parametro
        cotacao_bitcoin = cotacao ['BTCBRL']['bid']
        print(f'A cotação do BitCOin atualmente esta: {cotacao_bitcoin} BitCoins')

    break