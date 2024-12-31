
# Consulta de cotação em tempo real

[Repositorio](https://github.com/LizaGomes97/ConsultaCotacao.git) utilizado para verificar a cotação em tempo real das moedas Dolar, Euro e Bitcoin.

## Linguagem

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## Importações
```
  import requests
```
```
  import json
```
## Documentação da API

```http
  GET https://economia.awesomeapi.com.br/json/last/:moedas
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `moedas` | `string` | Moedas selecionadas separado por vírgula (,) Ex.: USD-BRL,EUR-BRL,BTC-BRL

 |

#### Link da documentação

[Clique aqui]( https://docs.awesomeapi.com.br/api-de-moedas)


## Aprendizados

Constuindo esse pequeno projeto pude finalmente comprender o conceito e como utilizar uma API em meus projetos. Aprendi tambem a selecionar qual parte do retorno de dados desejo utilizar.

