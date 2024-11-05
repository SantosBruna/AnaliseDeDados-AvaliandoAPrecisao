import pandas as pd
import numpy as np

# Função para calcular o erro quadrático
def calcular_erro_quadratico(real_x, real_y, real_z, virtual_x, virtual_y, virtual_z):
    erro_quadratico = (real_x - virtual_x)**2 + (real_y - virtual_y)**2 + (real_z - virtual_z)**2
    return erro_quadratico

#df = pd.read_csv('../preparacao-dos-dados/dados - objeto parado - 16w - camera em movimento.csv')
df = pd.read_csv('../preparacao-dos-dados/dados - objeto em movimento - luz ambiente - camera parada.csv')
#df = pd.read_csv('../preparacao-dos-dados/dados - objeto parado - luz ambiente - camera em movimento.csv')

# Aplica a função para calcular o erro quadrático para cada linha do DataFrame
df['erro_quadratico'] = df.apply(lambda row: calcular_erro_quadratico(row['real_x'], row['real_y'], row['real_z'],
                                                                     row['virtual_x'], row['virtual_y'], row['virtual_z']), axis=1)

# Calcula a Raiz do Erro Quadrático Médio (RMSE)
rmse = np.sqrt(df['erro_quadratico'].mean())

# Exibição do resultado
print(f"Raiz do Erro Quadrático Médio (RMSE): {rmse:.2f}")
