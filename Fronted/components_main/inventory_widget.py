from PySide6.QtWidgets import QFrame, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from PySide6.QtCore import Qt

class InventoryWidget(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(10)

        title_label = QLabel("Inventario")
        font = title_label.font()
        font.setPointSize(16)
        font.setBold(True)
        title_label.setFont(font)
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)

        buttons_layout = QHBoxLayout()
        
        add_button = QPushButton("Agregar")
        delete_button = QPushButton("Eliminar")

        buttons_layout.addWidget(add_button)
        buttons_layout.addWidget(delete_button)
        
        main_layout.addLayout(buttons_layout) 