import cv2

# Função utilitária para desenhar retângulos em torno dos rostos detectados
def desenhar_retangulos(frame, rostos):
    for rosto in rostos:
        x, y, w, h = rosto.left(), rosto.top(), rosto.width(), rosto.height()
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
