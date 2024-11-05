import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def calcular_erro_posicao(real_x, real_y, real_z, virtual_x, virtual_y, virtual_z):
    return math.sqrt((real_x - virtual_x)**2 + (real_y - virtual_y)**2 + (real_z - virtual_z)**2)


#df = pd.read_csv('../preparacao-dos-dados/dados - objeto parado - 16w - camera em movimento.csv')
df = pd.read_csv('../preparacao-dos-dados/dados - objeto em movimento - luz ambiente - camera parada.csv')
#df = pd.read_csv('../preparacao-dos-dados/dados - objeto parado - luz ambiente - camera em movimento.csv')

# Cálculo do erro de posição para cada linha do DataFrame
df['erro_posicao'] = df.apply(lambda row: calcular_erro_posicao(row['real_x'], row['real_y'], row['real_z'], row['virtual_x'], row['virtual_y'], row['virtual_z']), axis=1)

# Exibição dos resultados
print(df[['real_x', 'real_y', 'real_z', 'virtual_x', 'virtual_y', 'virtual_z', 'erro_posicao']])

# Resumo estatístico
summary = df['erro_posicao'].describe()
print(summary)

# histograma
plt.hist(df['erro_posicao'], bins=30, edgecolor='black')
plt.xlabel('Erro de Posição')
plt.ylabel('Frequência')
plt.title('Distribuição do Erro de Posição')
plt.show()

#gráfico de linha
plt.plot(df['erro_posicao'])
plt.xlabel('Índice')
plt.ylabel('Erro de Posição')
plt.title('Erro de Posição ao Longo do Tempo')
plt.show()


