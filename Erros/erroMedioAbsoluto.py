import pandas as pd


# Função para calcular o erro absoluto
def calcular_erro_absoluto(real_x, real_y, real_z, virtual_x, virtual_y, virtual_z):
    erro = abs(real_x - virtual_x) + abs(real_y - virtual_y) + abs(real_z - virtual_z)
    return erro


#df = pd.read_csv('../preparacao-dos-dados/dados - objeto em movimento-16W-camera parada.csv')
df = pd.read_csv('../preparacao-dos-dados/dados - objeto parado - 16w - camera em movimento.csv')
#df = pd.read_csv('../preparacao-dos-dados/dados - objeto em movimento - luz ambiente - camera parada.csv')
#df = pd.read_csv('../preparacao-dos-dados/dados - objeto parado - luz ambiente - camera em movimento.csv')

# Aplica a função para calcular o erro absoluto para cada linha do DataFrame
df['erro_absoluto'] = df.apply(lambda row: calcular_erro_absoluto(row['real_x'], row['real_y'], row['real_z'],
                                                                  row['virtual_x'], row['virtual_y'], row['virtual_z']), axis=1)

# Calcula o Erro Médio Absoluto (MAE)
mae = df['erro_absoluto'].mean()

# Exibição do resultado
print(f"Erro Médio Absoluto (MAE): {mae:.2f}")
