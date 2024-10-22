import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#df = pd.read_csv('../preparacao-dos-dados/posicoes1.csv')
df = pd.read_csv('../preparacao-dos-dados/posicoes2.csv')

# Exibir as primeiras linhas do DataFrame para verificar se foi lido corretamente
print(df.head())

real_x = df['real_x'].tolist()
real_y = df['real_y'].tolist()
real_z = df['real_z'].tolist()

virtual_x = df['virtual_x'].tolist()
virtual_y = df['virtual_y'].tolist()
virtual_z = df['virtual_z'].tolist()

# Função para calcular a média móvel
def moving_average(data, window_size):
    return np.convolve(data, np.ones(window_size) / window_size, mode='valid')

# Defina o tamanho da janela (por exemplo, 5)
window_size = 5

# Aplicar média móvel
smoothed_virtual_x = moving_average(virtual_x, window_size)
smoothed_real_x = moving_average(real_x, window_size)

# Plotar os dados suavizados
plt.figure(figsize=(12, 6))

plt.plot(smoothed_real_x, label='Objeto Real (Suavizado)', color='blue')
plt.plot(smoothed_virtual_x, label='Objeto Virtual (Suavizado)', color='red')
plt.legend()

plt.xlabel('Medições')
plt.ylabel('Coordenada X (Suavizada)')
plt.title('Comparação de Coordenadas X Suavizadas')
plt.show()
