import cv2
import os

def extract_frames(video_path, output_folder):
    # Verifica se a pasta de saída existe, caso contrário, cria-a
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Abre o vídeo
    video_capture = cv2.VideoCapture(video_path)
    frame_number = 0

    while True:
        success, frame = video_capture.read()
        if not success:
            break

        # Salva o frame como uma imagem
        frame_filename = os.path.join(output_folder, f"frame_{frame_number:04d}.jpg")
        cv2.imwrite(frame_filename, frame)
        frame_number += 1

    video_capture.release()
    print(f"Extração concluída. {frame_number} frames foram salvos em '{output_folder}'.")

# Caminho do vídeo e pasta de saída
video_path = 'teste5.mp4' #'teste1.mp4' #'tracking-simples.mp4'
output_folder = 'frames_extraidos_teste5'

# Chama a função para extrair frames
extract_frames(video_path, output_folder)
