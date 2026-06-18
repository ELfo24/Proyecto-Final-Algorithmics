import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, 
                            QWidget, QLineEdit, QHBoxLayout, QGroupBox, QRadioButton, QListWidget)

from text import *
from ventana_1 import *
from ventana_2 import *

class Ventana3(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()
        