import cv2
from detector_facial import DetectorRostos

def main():
    # Inicialize o detector de rostos
    detector_rostos = DetectorRostos()

    # Inicialize a fonte de vídeo (por exemplo, webcam)
    video_capture = cv2.VideoCapture(0)

    while True:
        # Captura frame por frame
        ret, frame = video_capture.read()

        # Detecção de rostos
        rostos = detector_rostos.detectar(frame)

        # Exibir resultados, por exemplo, desenhar retângulos ao redor dos rostos detectados
        for rosto in rostos:
            x, y, w, h = rosto.left(), rosto.top(), rosto.width(), rosto.height()
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Exibir o frame resultante
        cv2.imshow('Video', frame)

        # Pare o loop quando a tecla 'q' for pressionada
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Libere o objeto de captura de vídeo e feche todas as janelas
    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
