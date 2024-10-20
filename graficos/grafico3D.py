import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

df = pd.read_csv('../preparacao-dos-dados/posicoes1.csv')

# Exibir as primeiras linhas do DataFrame para verificar se foi lido corretamente
print(df.head())

real_x = df['real_x'].tolist()
real_y = df['real_y'].tolist()
real_z = df['real_z'].tolist()

virtual_x = df['virtual_x'].tolist()
virtual_y = df['virtual_y'].tolist()
virtual_z = df['virtual_z'].tolist()


fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plotando o objeto real
ax.plot(real_x, real_y, real_z, label='Objeto Real', color='blue')

# Plotando o objeto virtual
ax.plot(virtual_x, virtual_y, virtual_z, label='Objeto Virtual', color='red')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

plt.show()
