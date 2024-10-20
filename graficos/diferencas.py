import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('../preparacao-dos-dados/posicoes1.csv')

# Exibir as primeiras linhas do DataFrame para verificar se foi lido corretamente
#print(df.head())

real_x = df['real_x'].tolist()
real_y = df['real_y'].tolist()
real_z = df['real_z'].tolist()

virtual_x = df['virtual_x'].tolist()
virtual_y = df['virtual_y'].tolist()
virtual_z = df['virtual_z'].tolist()


diff_x = [real - virtual for real, virtual in zip(real_x, virtual_x)]
diff_y = [real - virtual for real, virtual in zip(real_y, virtual_y)]
diff_z = [real - virtual for real, virtual in zip(real_z, virtual_z)]

dist = [np.sqrt(dx**2 + dy**2 + dz**2) for dx, dy, dz in zip(diff_x, diff_y, diff_z)]

print(f'Diferença no eixo x:{diff_x}\nDiferença no eixo y: {diff_y}\nDiferença no eixo z:{diff_z}\nDistância euclidianada: {dist}')


plt.figure(figsize=(12, 8))

plt.subplot(4, 1, 1)
plt.plot(diff_x, label='Diferença X')
plt.legend()

plt.subplot(4, 1, 2)
plt.plot(diff_y, label='Diferença Y')
plt.legend()

plt.subplot(4, 1, 3)
plt.plot(diff_z, label='Diferença Z')
plt.legend()

plt.subplot(4, 1, 4)
plt.plot(dist, label='Distância Euclidiana')
plt.legend()

plt.tight_layout()
plt.show()
