import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton

class Browser(QWidget):
    def __init__(self):
        super().__init__()

        # Crear QWebEngineView
        self.view = QWebEngineView(self)

        # Establecer la URL para cargar
        self.view.setUrl(QUrl("https://www.google.com"))

        # Crear la barra de URL
        self.url_bar = QLineEdit(self)

        # Crear el boton "Ir"
        self.go_button = QPushButton("Ir", self)
        self.go_button.clicked.connect(self.load_url)

        # Crear el botón "Atrás"
        self.back_button = QPushButton("Atrás", self)
        self.back_button.clicked.connect(self.view.back)

        # Crear el botón "Adelante"
        self.forward_button = QPushButton("Adelante", self)
        self.forward_button.clicked.connect(self.view.forward)

        # Crear el botón "Actualizar"
        self.refresh_button = QPushButton("Actualizar", self)
        self.refresh_button.clicked.connect(self.view.reload)

        # Crear el diseño
        layout = QVBoxLayout(self)
        nav_layout = QHBoxLayout()
        nav_layout.addWidget(self.url_bar)
        nav_layout.addWidget(self.go_button)
        nav_layout.addWidget(self.back_button)
        nav_layout.addWidget(self.forward_button)
        nav_layout.addWidget(self.refresh_button)
        layout.addLayout(nav_layout)
        layout.addWidget(self.view)

        self.setLayout(layout)

    def load_url(self):
        # Obtener la URL de la barra de URL
        url = self.url_bar.text()

        # Establezca la URL en QWebEngineView
        self.view.setUrl(QUrl(url))

app = QApplication(sys.argv)
browser = Browser()
browser.show()
app.exec_()
