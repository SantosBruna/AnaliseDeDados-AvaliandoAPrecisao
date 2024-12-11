import pandas as pd
from sklearn.metrics import mean_squared_error

#df = pd.read_csv('../preparacao-dos-dados/dados - objeto em movimento-16W-camera parada.csv')
df = pd.read_csv('../preparacao-dos-dados/dados - objeto parado - 16w - camera em movimento.csv')
#df = pd.read_csv('../preparacao-dos-dados/dados - objeto em movimento - luz ambiente - camera parada.csv')
#df = pd.read_csv('../preparacao-dos-dados/dados - objeto parado - luz ambiente - camera em movimento.csv')

# Extração das coordenadas reais e virtuais
x_real = df[['real_x', 'real_y', 'real_z']].values
x_virtual = df[['virtual_x', 'virtual_y', 'virtual_z']].values

# Calcula o Mean Squared Error (MSE)
mse = mean_squared_error(x_real, x_virtual)

# Exibição do resultado
print(f"Mean Squared Error (MSE): {mse:.6f}")
