# Nome do arquivo de entrada e saída
input_file = 'dados - objeto em movimento-16W-camera parada.txt'
output_file = 'dados - objeto em movimento-16W-camera parada.txt'

# Ler o arquivo de entrada
with open(input_file, 'r') as file:
    lines = file.readlines()

# Remover linhas em branco
non_empty_lines = [line for line in lines if line.strip()]

# Escrever o resultado em um novo arquivo
with open(output_file, 'w') as file:
    file.writelines(non_empty_lines)

print(f"Linhas em branco removidas. Arquivo salvo como: {output_file}")
