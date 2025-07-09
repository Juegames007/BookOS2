from PySide6.QtWidgets import QFrame, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from PySide6.QtCore import Qt

class InventoryWidget(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFrameShape(QFrame.StyledPanel) # Establece el marco como un panel estilizado
        self.setFrameShadow(QFrame.Raised) # Establece la sombra del marco como elevada

        # Llamar a un método para configurar la UI
        self._setup_ui() 

    def _setTitle(self):
        title_label = QLabel("Inventario")
        font = title_label.font()
        font.setPointSize(20)
        font.setBold(True)
        title_label.setFont(font)
        title_label.setAlignment(Qt.AlignCenter)
        return title_label

    def _setup_buttons(self):
        add_button = QPushButton("Agregar")
        delete_button = QPushButton("Eliminar")
        
        # Configurar el layout de los botones
        button_layout = QVBoxLayout()
        button_layout.addWidget(add_button)
        button_layout.addWidget(delete_button)
        button_layout.setAlignment(Qt.AlignCenter)
        return button_layout

    def _setup_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(10, 30, 10, 10) # Márgenes alrededor del contenido
        main_layout.setSpacing(10) # Espacio vertical entre el título y el button_layout

        # Establecer el título
        title_label = self._setTitle()
        # Alinea el título horizontalmente al centro
        main_layout.addWidget(title_label, alignment=Qt.AlignHCenter)

        # Agregar botones al layout
        button_layout = self._setup_buttons()
        # Añade el layout de botones
        main_layout.addLayout(button_layout)

        # Añadir un espaciador elástico para empujar el contenido (título y botones) hacia arriba
        main_layout.addStretch(1) 

class CajaWidget(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)

        # Llamar a un método para configurar la UI
        self._setup_ui()

    def _setTitle(self):
        title_label = QLabel("Caja")
        font = title_label.font()
        font.setPointSize(20)
        font.setBold(True)
        title_label.setFont(font)
        title_label.setAlignment(Qt.AlignCenter)
        return title_label
    
    def _setup_buttons(self):
        close_button = QPushButton("Cerrar Caja")
        funds_button = QPushButton("Fondos")
        transferir_button = QPushButton("Transferir")
        
        # Configurar el layout de los botones
        button_layout = QVBoxLayout()
        button_layout.addWidget(close_button)
        button_layout.addWidget(funds_button)
        button_layout.addWidget(transferir_button)
        button_layout.setAlignment(Qt.AlignCenter)
        return button_layout

    def _setup_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(10, 30, 10, 10) # Márgenes alrededor del contenido
        main_layout.setSpacing(10) # Espacio vertical entre el título y el button_layout

        # Establecer el título
        title_label = self._setTitle()
        # Alinea el título horizontalmente al centro
        main_layout.addWidget(title_label, alignment=Qt.AlignHCenter)

        # Agregar botones al layout
        button_layout = self._setup_buttons()
        # Añade el layout de botones
        main_layout.addLayout(button_layout)

        # Añadir un espaciador elástico para empujar el contenido (título y botones) hacia arriba
        main_layout.addStretch(1) 


class FinanzasWidget(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)

        # Llamar a un método para configurar la UI
        self._setup_ui()

    def _setTitle(self):
        title_label = QLabel("Finanzas")
        font = title_label.font()
        font.setPointSize(20)
        font.setBold(True)
        title_label.setFont(font)
        title_label.setAlignment(Qt.AlignCenter)
        return title_label
    
    def _setup_buttons(self):
        vender_button = QPushButton("Vender")
        egreso_button = QPushButton("Egreso")
        
        # Configurar el layout de los botones
        button_layout = QVBoxLayout()
        button_layout.addWidget(vender_button)
        button_layout.addWidget(egreso_button)
        button_layout.setAlignment(Qt.AlignCenter)
        return button_layout

    def _setup_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(10, 30, 10, 10) # Márgenes alrededor del contenido
        main_layout.setSpacing(10) # Espacio vertical entre el título y el button_layout

        # Establecer el título
        title_label = self._setTitle()
        # Alinea el título horizontalmente al centro
        main_layout.addWidget(title_label, alignment=Qt.AlignHCenter)

        # Agregar botones al layout
        button_layout = self._setup_buttons()
        # Añade el layout de botones
        main_layout.addLayout(button_layout)

        # Añadir un espaciador elástico para empujar el contenido (título y botones) hacia arriba
        main_layout.addStretch(1)

