import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../preparacao-dos-dados/posicoes1.csv')

# Exibir as primeiras linhas do DataFrame para verificar se foi lido corretamente
print(df.head())

real_x = df['real_x'].tolist()
real_y = df['real_y'].tolist()
real_z = df['real_z'].tolist()

virtual_x = df['virtual_x'].tolist()
virtual_y = df['virtual_y'].tolist()
virtual_z = df['virtual_z'].tolist()


plt.figure(figsize=(12, 8))

# Coordenada X
plt.subplot(3, 1, 1)
plt.plot(real_x, label='Objeto Real X', color='blue')
plt.plot(virtual_x, label='Objeto Virtual X', color='red')
plt.legend()

# Coordenada Y
plt.subplot(3, 1, 2)
plt.plot(real_y, label='Objeto Real Y', color='blue')
plt.plot(virtual_y, label='Objeto Virtual Y', color='red')
plt.legend()

# Coordenada Z
plt.subplot(3, 1, 3)
plt.plot(real_z, label='Objeto Real Z', color='blue')
plt.plot(virtual_z, label='Objeto Virtual Z', color='red')
plt.legend()

plt.tight_layout()
plt.show()



