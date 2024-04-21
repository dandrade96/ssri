from sklearn.svm import SVC

class AnalisadorComportamental:
    def __init__(self):
        # Inicialize o classificador SVM (Support Vector Machine)
        self.classificador = SVC(kernel='linear')

    def analisar(self, caracteristicas, labels):
        # Treinar o classificador SVM com as características faciais e seus rótulos correspondentes
        self.classificador.fit(caracteristicas, labels)

        # Retornar o classificador treinado
        return self.classificador
