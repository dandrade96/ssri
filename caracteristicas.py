import dlib

class ExtratorCaracteristicas:
    def __init__(self):
        # Inicialize o extrator de características faciais do Dlib
        self.predictor = dlib.shape_predictor("caminho_para_o_arquivo_shape_predictor.dat")

    def extrair(self, rostos, frame):
        # Extrair características faciais dos rostos detectados
        caracteristicas = []
        for rosto in rostos:
            # Detectar pontos-chave do rosto
            pontos_chave = self.predictor(frame, rosto)
            # Adicionar os pontos-chave à lista de características
            caracteristicas.append(pontos_chave)
        return caracteristicas
