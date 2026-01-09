import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel

class Ventana(QWidget):
    def __init__(self):
        super().__init__()

        # Ventana
        self.setWindowTitle("Nivel 2 - Contador de clics")
        self.setGeometry(200, 200, 350, 200)

        # Estado (variable que guarda el conteo)
        self.contador = 0

        # Label del título
        self.titulo = QLabel("Contador de clics", self)
        self.titulo.move(120, 30)

        # Label del número
        self.lbl_numero = QLabel(str(self.contador), self)
        self.lbl_numero.move(165, 65)
        self.lbl_numero.setStyleSheet("font-size: 28px;")

        # Botón sumar
        self.btn_sumar = QPushButton("Sumar +1", self)
        self.btn_sumar.move(60, 120)
        self.btn_sumar.clicked.connect(self.sumar)

        # Botón reiniciar
        self.btn_reiniciar = QPushButton("Reiniciar", self)
        self.btn_reiniciar.move(190, 120)
        self.btn_reiniciar.clicked.connect(self.reiniciar)

    def sumar(self):
        self.contador += 1
        self.lbl_numero.setText(str(self.contador))

    def reiniciar(self):
        self.contador = 0
        self.lbl_numero.setText(str(self.contador))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())