import requests
import pandas as pd
from bs4 import BeautifulSoup

url_base = 'https://lista.mercadolivre.com.br/'

produto_nome = input('Qual produto você deseja? ')

response = requests.get(url_base + produto_nome)

site = BeautifulSoup(response.text, 'html.parser')

produtos = site.findAll('div', attrs={'class': 'andes-card andes-card--flat andes-card--default ui-search-result ui-search-result--core andes-card--padding-default'})

tabela_produtos = []

for produto in produtos:
    titulo = produto.find('h2', attrs={'class': 'ui-search-item__title'})
    link = produto.find('a', attrs={'class': 'ui-search-link'})

    real = produto.find('span', attrs={'class': 'price-tag-fraction'})
    centavos = produto.find('span', attrs={'class': 'price-tag-cents'})

    # print(produto.prettify())
    # print('Título do produto:', titulo.text)
    # print('Link do produto:', link['href'])

    if (centavos):
        tabela_produtos.append([titulo.text, link.text, real.text, centavos.text])
    else:
        tabela_produtos.append([titulo.text, link.text, real.text])


precos_produtos = pd.DataFrame(tabela_produtos, columns=['Nome', 'Link', 'Reais', 'Centavos'])

precos_produtos.to_excel('tabela_de_preços_produtos.xlsx')

print(precos_produtos)