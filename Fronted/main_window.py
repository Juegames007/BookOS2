from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QApplication
from PySide6.QtCore import Qt
from PySide6.QtGui import QScreen
from .components_main.inventory_widget import InventoryWidget

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BookOS 2.0")
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        
        # Llamar a un método para configurar la UI
        self._setup_ui() # Aquí se llama al nuevo método

    def _configsize(self):
        # Dimensiones de la ventana (igual que antes)
        window_width = 800
        window_height = 600

        # 1. Obtener la geometría de la pantalla principal
        screen = QApplication.primaryScreen()
        screen_geometry = screen.geometry() 
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()

        # 2. Calcular las coordenadas X e Y para centrar la ventana
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # 3. Establecer la geometría de la ventana con las nuevas coordenadas calculadas
        self.setGeometry(x, y, window_width, window_height)


    def _setTitle(self):
        # Título de la aplicación
        title_label = QLabel("BookOS")
        font = title_label.font()
        font.setPointSize(24)
        font.setBold(True)
        title_label.setFont(font)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: #333;")  # Estilo de color
        return title_label

    def _setup_ui(self):
        """Configura la interfaz de usuario de la ventana principal."""
        self._configsize()  # Llamar al método para configurar el tamaño y posición de la ventana

        # Crear el Layout principal
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)

        # Establecer el título de la ventana
        title_label = self._setTitle()  # Llamar al método para obtener el título
        main_layout.addWidget(title_label)

        # Agregar el contendedor de inventario
        inventory_section = InventoryWidget()
        main_layout.addWidget(inventory_section)

        main_layout.addStretch()

        self.setLayout(main_layout)