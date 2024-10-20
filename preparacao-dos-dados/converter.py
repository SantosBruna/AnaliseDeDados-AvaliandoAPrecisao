import re
import pandas as pd

# Ler o arquivo de texto original
with open('dados - objeto parado - 16w - camera em movimento.txt', 'r') as file:
    data = file.read()

# Adicionar uma quebra de linha entre cada conjunto de dados para facilitar o processamento
data = re.sub(r'(Posicao do objeto Real no Unity: X=-?\d+,\d+, Y=-?\d+,\d+, Z=-?\d+,\d+)', r'\1\n', data)

# Usar expressões regulares para extrair as posições virtuais e reais separadamente
virtual_pattern = r'Posicao do objeto Virtual: X=(-?\d+,\d+), Y=(-?\d+,\d+), Z=(-?\d+,\d+)'
real_pattern = r'Posicao do objeto Real no Unity: X=(-?\d+,\d+), Y=(-?\d+,\d+), Z=(-?\d+,\d+)'

virtual_matches = re.findall(virtual_pattern, data)
real_matches = re.findall(real_pattern, data)

# Verificação se encontramos os dados
if not virtual_matches or not real_matches:
    print("Erro: Não foram encontradas correspondências para os padrões de 'Virtual' ou 'Real'.")
else:
    # Criar listas para os dados
    virtual_x, virtual_y, virtual_z = [], [], []
    real_x, real_y, real_z = [], [], []

    # Preencher as listas com os valores extraídos
    for virtual_match in virtual_matches:
        # Substituir a vírgula decimal por ponto decimal
        vx, vy, vz = map(lambda x: float(x.replace(',', '.')), virtual_match)
        virtual_x.append(vx)
        virtual_y.append(vy)
        virtual_z.append(vz)

    for real_match in real_matches:
        # Substituir a vírgula decimal por ponto decimal
        rx, ry, rz = map(lambda x: float(x.replace(',', '.')), real_match)
        real_x.append(rx)
        real_y.append(ry)
        real_z.append(rz)

    # Certificar-se de que o número de capturas é o mesmo
    if len(virtual_x) != len(real_x):
        print(f"Erro: Número de posições virtuais ({len(virtual_x)}) e reais ({len(real_x)}) não é o mesmo.")
    else:
        # Criar um DataFrame com os dados
        df = pd.DataFrame({
            'real_x': real_x,
            'real_y': real_y,
            'real_z': real_z,
            'virtual_x': virtual_x,
            'virtual_y': virtual_y,
            'virtual_z': virtual_z
        })

        # Salvar o DataFrame em um arquivo CSV
        df.to_csv('posicoes1.csv', index=False)

        print("Arquivo CSV gerado com sucesso!")
