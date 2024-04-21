import dlib

class DetectorRostos:
    def __init__(self):
        # Inicialize o detector de rostos do Dlib
        self.detector = dlib.get_frontal_face_detector()

    def detectar(self, frame):
        # Detectar rostos em um quadro de vídeo
        # Retorna uma lista de objetos dlib.rectangle representando os rostos detectados
        return self.detector(frame)
