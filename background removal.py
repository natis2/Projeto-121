# importe o cv2 para capturar o feed de vídeo
import cv2

import numpy as np

# anexe a câmera indexada como 0
camera = cv2.VideoCapture(0)

# definindo a largura do quadro e a altura do quadro como 640 X 480
camera.set(3 , 640)
camera.set(4 , 480)

# carregando a imagem da montanha
mountain = cv2.imread('download.jpeg')

# redimensionando a imagem da montanha como 640 X 480
mountain =cv2.resize(mountain ,(640,480))

while True:

    # ler um quadro da câmera conectada
    status , frame = camera.read()

    # se obtivermos o quadro com sucesso
    if status:

        # inverta-o
        frame = cv2.flip(frame , 1)

        # convertendo a imagem em RGB para facilitar o processamento
        frame_rgb = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)

        # criando os limites
        lower_bound = np.array([100,100,100])
        upper_bound = np.array([255,255,255])
     
        # imagem dentro do limite
        frame = cv2.inRange(lower_bound, upper_bound)
       
        # invertendo a máscara
        frame = np.flip(frame, axis=1)
        # bitwise_and - operação para extrair o primeiro plano / pessoa
        pessoa=cv2.bitwise_and(frame)
        # imagem final
        frame = cv2.addWeighted(pessoa)
        # exiba-a
        cv2.imshow('quadro' , frame)

        # espera de 1ms antes de exibir outro quadro
        code = cv2.waitKey(1)
        if code  ==  32:
            break

# libere a câmera e feche todas as janelas abertas
camera.release()
cv2.destroyAllWindows()
