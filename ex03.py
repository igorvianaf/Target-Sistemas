import numpy as np

#lista de faturamento mensal
faturamento_mes = np.array([19978, 23009, 38274, 12093, 0, 12234, 32232, 0, 12302, 12192, 12203])

#retirar valores zerados
filtro_faturamento = faturamento_mes[faturamento_mes > 0]

#checar menor e maior faturamento
menor_faturamento = np.min(filtro_faturamento)
maior_faturamento = np.max(filtro_faturamento)

#checar media mensal de faturamento
media_mensal = np.mean(filtro_faturamento)

#checar valores acima da media
dias_acima_da_media = np.sum(filtro_faturamento > media_mensal)

print("Menor valor de faturamento:", menor_faturamento)
print("Maior valor de faturamento:", maior_faturamento)
print("Número de dias com faturamento acima da média:", dias_acima_da_media)