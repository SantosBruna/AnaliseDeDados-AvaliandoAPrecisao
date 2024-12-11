import os
import cv2
import numpy as np
from skimage import io

# Caminho da pasta onde as imagens estão armazenadas
folder_path = "record_2"


# Função para verificar a qualidade da imagem
def is_high_quality(image_path):
    try:
        image = io.imread(image_path)

        # Parâmetro 1: Resolução mínima
        min_resolution = (400, 300)  # Reduzido para testes
        if image.shape[0] < min_resolution[0] or image.shape[1] < min_resolution[1]:
            return False

        # Parâmetro 2: Detecção de bordas (nitidez)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 100, 150)  # Limiares ajustados para ser mais permissivo
        edge_density = np.mean(edges)
        if edge_density < 5:  # Valor mais baixo para testes
            return False

        # Parâmetro 3: Contraste
        contrast = image.max() - image.min()
        if contrast < 30:  # Valor ajustado para ser mais permissivo
            return False

        return True

    except Exception as e:
        print(f"Erro ao processar a imagem {image_path}: {e}")
        return False


# Função para filtrar imagens de alta qualidade
def filter_high_quality_images(folder_path):
    high_quality_images = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join(folder_path, filename)
            if is_high_quality(image_path):
                high_quality_images.append(image_path)
    return high_quality_images


# Listar todas as imagens de alta qualidade na pasta
high_quality_images = filter_high_quality_images(folder_path)
print("Imagens de alta qualidade:", high_quality_images)
print(f"\nQuantidade total de imagens: {len(high_quality_images)}")

if 'record_2\\image_00401.jpg' in high_quality_images:
    print("ENCONTREI")
else:
    print("não achei")