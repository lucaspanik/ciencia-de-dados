#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import json
import locale
import pandas as pd

# 1) Obtenha os dados a partir da página https://www.kaggle.com/mateuspgomes/brazil-thrift-stores-data .
#    É importante estar atento às descrições na página para conhecer melhor do que tratam os dados.
# 2) Utilizaremos somente o arquivo Thrift_Store_A.csv nesta análise.
#    Mas, fiquem livres para explorar os outros.
tsa = pd.read_csv("./Projects/UNISUAM/Python_P1910338/Thrift_Store_A.csv", delimiter=";")

# 3) Utilizando a linguagem de programação Python 3, analisem os dados para responder as seguintes perguntas:
print("a) Quantas linhas possui o arquivo?")
print("R: Total de " +str(len(tsa))+" linhas\n")

print("b) Quais são as colunas / nomes dos campos presentes no arquivo?")
print("R: As colunas são:")
for column in tsa.columns.values:
    print(str(column))
print("\n")

print("c) Imprima algumas linhas para análise, observe o conteúdo dos campos.")
print(tsa.head(5))
print("\n")

print("d) Quantos produtos diferentes existem?")
#print(tsa.info())
nameOfTheSinglePieces = tsa.nomeDaPeca.unique()
print("Existem "+str(len(nameOfTheSinglePieces)-1)+" produtos diferentes")
print("\n")

print("e) Quais são os valores possíveis para o campo Status?")
statusNames = tsa.Status.unique()
print("R: Os valores possíveis para status são:")
for status in tsa.Status.unique():
    print(str(status))
print("\n")
#print("Existem "+str(len(nameOfTheSinglePieces)-1)+" produtos diferentes")

print("f) Imprima alguns registros com status PAGINA_NAO_DISPONIVEL. Veja que podem não ser muito úteis.")
print(tsa[tsa.Status == "PAGINA_NAO_DISPONIVEL"].head(5))
#print(str(len(tsa[tsa.Status == "PAGINA_NAO_DISPONIVEL"])))
print("\n")

print("g) Remova os registros com status PAGINA_NAO_DISPONIVEL. Reserve o restante dos dados para utilização nos próximos exercícios.")
tsaWhitoutPageNotFound = tsa[tsa.Status != "PAGINA_NAO_DISPONIVEL"]
print(str(len(tsaWhitoutPageNotFound)))
print("\n")

def currencyStringToFloat(currency):
    return float(str(currency).replace('POR:','').replace('R$','').replace('.','').replace(',','.').strip())


print("h) Qual o produto mais caro e o mais barato vendido (preço com desconto)?")
discountPrices = tsa[tsa.precoComDesconto.notna()].precoComDesconto
discountPrices = discountPrices.apply(lambda x: currencyStringToFloat(x))
discountPrices = discountPrices.astype(float)
#print(discountPrices)

def convertToBrazilianCurrency(value):
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    return "R$ "+str(locale.currency(value, grouping=True, symbol=None))

print("O preco mais caro foi:")
print(convertToBrazilianCurrency(discountPrices.max()))
print("O preco mais barato foi:")
print(convertToBrazilianCurrency(discountPrices.min()))
print("\n")


# i) Qual é o preço médio de uma camiseta?
#    Observe que existe mais de uma descrição possível para camiseta,
#    queremos obter o preço médio de todos os produtos que contenham camiseta no nome.
# @todo Tentar entender o porque só funcionou com o parâmetro "case=False"
#
shirts = tsa[tsa.nomeDaPeca.str.contains('camiseta', na=False, case=False)]

shirtsWhithoutDiscountPrices = shirts.precoSemDesconto.apply(lambda x: currencyStringToFloat(x))
shirtsWhithDiscountPrices    = shirts.precoComDesconto.apply(lambda x: currencyStringToFloat(x))
#shirts['precoComDesconto'] = shirts.precoComDesconto.astype(float)
#shirts = shirts.precoSemDesconto.apply(lambda x: x.replace('POR: R$ ','').replace('R$ ','').replace('.','').replace(',','.')).astype(float)

print("Preco medio sem desconto das camisas:")
print(convertToBrazilianCurrency(shirtsWhithoutDiscountPrices.mean()))

print("Preco medio com desconto das camisas:")
print(convertToBrazilianCurrency(shirtsWhithDiscountPrices.mean()))
print("\n")

# j) Qual o preço médio por produto?
# l) Quais são as 10 marcas com preços médios maiores?
# m) Quais foram os maiores descontos concedidos?
#
# 4) Ao concluir a atividade , envie as respostas e o código utilizado para
#    roosevelt.pos@souunisuam.com.br até o início da próxima aula (13/07 8h).
#
