import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit

class Ventana(QWidget):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana
        self.setWindowTitle("Nivel 1 - Saludo")
        self.setGeometry(600, 600, 350, 200)

        # Texto
        self.etiqueta = QLabel("Haz clic para saludar", self)
        self.input_nombre = QLineEdit(self)
        self.input_nombre.setPlaceholderText("Escribe tu nombre")
        self.input_nombre.move(100, 75)
        self.input_nombre.resize(150, 25)
        self.etiqueta.move(100, 50)

        # Botón
        self.boton = QPushButton("Saludar", self)
        self.boton.move(130, 100)

        # Evento: cuando dan clic
        self.boton.clicked.connect(self.saludar)

    def saludar(self):
        nombre = self.input_nombre.text()
        if nombre:
            self.etiqueta.setText(f"Hola, {nombre} 👋")
        else:
            self.etiqueta.setText("Escribe tu nombre 🙂")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())