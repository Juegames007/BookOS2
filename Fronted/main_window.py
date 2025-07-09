from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QApplication, QHBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QScreen
# Importamos todos los widgets de tarjetas, incluyendo el nuevo
from .components_main.tarjetas import InventoryWidget, CajaWidget, FinanzasWidget

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BookOS 2.0")
        
        # Llamar a un método para configurar la UI
        self._setup_ui() 

    def _configsize(self):
        # Dimensiones de la ventana (igual que antes)
        window_width = 1200
        window_height = 800

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


    def _tarjetas_layout(self):
        cards_holder_layout = QHBoxLayout()
        cards_holder_layout.setSpacing(25)
        cards_holder_layout.setContentsMargins(0, 0, 0, 0)
        cards_holder_layout.addStretch(1)

        def _create_inventory_column():
            #1. Crear el layout invisible que contendrá las tarjetas
            col_widget = QWidget()
            col_layout = QVBoxLayout(col_widget)

            #2. Espaciado y márgenes dentro de la columna
            col_layout.setSpacing(15)
            col_layout.setContentsMargins(0, 0, 0, 0)

            #3. Crear la tarjeta de inventario y establecer su tamaño
            inventory_card = InventoryWidget(self)
            inventory_card.setFixedSize(275, 220)

            #4. Añadir la tarjeta al layout de la columna
            col_layout.addWidget(inventory_card)
            col_layout.addStretch(1) #Empuja la tarjeta hacia arriba

            #5. Devolver el widget de la columna para añadirlo al layout principal
            return col_widget

        def _create_caja_column(): #Solo modifica la posicion y el tamaño de los widgets
            col_widget = QWidget()
            col_layout = QVBoxLayout(col_widget)
            col_layout.setSpacing(15)
            col_layout.setContentsMargins(0, 0, 0, 0)
            caja_card = CajaWidget(self)
            caja_card.setFixedSize(250, 200)
            col_layout.addWidget(caja_card)
            col_layout.addStretch(1) 
            return col_widget

        def _create_finanzas_column(): 
            col_widget = QWidget()
            col_layout = QVBoxLayout(col_widget)
            col_layout.setSpacing(15)
            col_layout.setContentsMargins(0, 0, 0, 0)
            finanzas_card = FinanzasWidget(self)
            finanzas_card.setFixedSize(275, 220)
            col_layout.addWidget(finanzas_card)
            col_layout.addStretch(1)
            return col_widget

        cards_holder_layout.addWidget(_create_inventory_column())
        cards_holder_layout.addWidget(_create_caja_column())
        cards_holder_layout.addWidget(_create_finanzas_column())

        cards_holder_layout.addStretch(1)

        cards_container_widget = QWidget()
        cards_container_widget.setLayout(cards_holder_layout)
        return cards_container_widget


    def _setup_ui(self):
        """Configura la interfaz de usuario de la ventana principal."""
        self._configsize()

        # Layout principal vertical
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(40)  # Un espaciado vertical entre el título y las tarjetas

        # 1. AÑADIMOS UN ESPACIADOR ELÁSTICO ARRIBA
        main_layout.addStretch(1)

        # 2. Establecemos el título
        title_label = self._setTitle()
        main_layout.addWidget(title_label, alignment=Qt.AlignTop | Qt.AlignHCenter)

        # 3. Espaciador fijo para separar el título del contenido
        main_layout.addSpacing(60)

        # 4. Creamos y añadimos el widget que contiene el layout de tarjetas
        cards_widget = self._tarjetas_layout()
        main_layout.addWidget(cards_widget)

        # 5. AÑADIMOS OTRO ESPACIADOR ELÁSTICO ABAJO
        # Los dos espaciadores empujarán todo el contenido al centro vertical.
        main_layout.addStretch(3)

        self.setLayout(main_layout)