from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt
from .components_main.inventory_widget import InventoryWidget

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BookOS 2.0")
        self.setGeometry(100, 100, 800, 600)

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)

        title_label = QLabel("BookOS")
        font = title_label.font()
        font.setPointSize(24)
        font.setBold(True)
        title_label.setFont(font)
        title_label.setAlignment(Qt.AlignCenter)
        
        main_layout.addWidget(title_label)

        inventory_section = InventoryWidget()
        main_layout.addWidget(inventory_section)

        main_layout.addStretch()

        self.setLayout(main_layout)