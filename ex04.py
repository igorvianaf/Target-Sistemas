#dicionario com valores de faturamento por cidade
faturamento_mensal = {
    'SP': 67836.42,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES':27165.48,
    'OUTROS': 19849.53
}
#variavel para armazenar total de faturamento
valor_total = 0

# adicionar apenas os valores do dict ao total
for valor in faturamento_mensal.values():
    valor_total += valor

#passar por cada keys and values do dict para analisar percentual por cidade
for k, v in faturamento_mensal.items():
    percentual = (v/valor_total) * 100
    print(f'O percentual de representação de {k}, baseado no valor total mensal é de {percentual:.2f}%')