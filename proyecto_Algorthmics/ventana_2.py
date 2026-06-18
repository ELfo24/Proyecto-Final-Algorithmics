from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QDoubleSpinBox, QHeaderView, QMainWindow, QPushButton, QLabel, QSpinBox, QTableWidget, QVBoxLayout, 
                            QWidget, QLineEdit, QHBoxLayout, QGroupBox, QRadioButton, QListWidget, QTableWidgetItem)

from text import *
from ventana_1 import Ventana1
from ventana_3 import *

class Ventana2(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()

    def initUI(self):
        # Etiquetas para los campos de concepto, cantidad y precio
        self.lbl_concepto=QLabel(txt_concepto,self)
        self.lbl_cantidad=QLabel(txt_cantidad,self)
        self.lbl_precio=QLabel(txt_precio,self)


        # Campos de entrada para concepto, cantidad y precio
        self.btn_concepto=QLineEdit(self)
        self.btn_cantidad=QSpinBox(self)
        self.btn_precio=QDoubleSpinBox(self)

        # Botones para agregar el concepto a la tabla y para culminar la cotización/presupuesto
        self.btn_agregar=QPushButton(txt_agregar,self)
        self.btn_culminar=QPushButton(txt_terminar,self)

        # Tabla para mostrar los conceptos, cantidades, precios y totales
        self.btn_tabla=QTableWidget(self)
        self.btn_tabla.setRowCount(0)
        self.btn_tabla.setColumnCount(4)
        self.btn_tabla.setHorizontalHeaderLabels([txt_concepto, txt_cantidad, txt_precio, txt_total])
        self.btn_tabla.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Diseño de la ventana utilizando layouts
        v_line=QVBoxLayout()
        h_layout=QHBoxLayout()
        h_layout.addWidget(self.lbl_concepto)
        h_layout.addWidget(self.btn_concepto)
        h_layout.addSpacing(20)
        h_layout.addWidget(self.lbl_cantidad)
        h_layout.addWidget(self.btn_cantidad)
        h_layout.addSpacing(20)
        h_layout.addWidget(self.lbl_precio)
        h_layout.addWidget(self.btn_precio)
        h_layout.addSpacing(20)
        h_layout.addWidget(self.btn_agregar)
        h_layout.addStretch()
        v_line.addSpacing(50)
        v_line.addLayout(h_layout)
        v_line.addSpacing(50)
        v_line.addWidget(self.btn_tabla)
        v_line.addWidget(self.btn_culminar, alignment= Qt.AlignCenter)
        v_line.addStretch()
        self.setLayout(v_line)

    def agregar_click(self):
        # Función para agregar un concepto a la tabla con su cantidad, precio y total
        concepto=self.btn_concepto.text()
        cantidad=self.btn_cantidad.value()
        precio=self.btn_precio.value()

        # Calcular el total y agregar una nueva fila a la tabla con los datos ingresados
        total=cantidad*precio
        fila_pos=self.btn_tabla.rowCount()
        self.btn_tabla.insertRow(fila_pos)
        self.btn_tabla.setItem(fila_pos, 0, QTableWidgetItem(concepto))
        self.btn_tabla.setItem(fila_pos, 1, QTableWidgetItem(str(cantidad)))
        self.btn_tabla.setItem(fila_pos, 2, QTableWidgetItem(str(precio)))
        self.btn_tabla.setItem(fila_pos, 3, QTableWidgetItem(str(total)))

        # Limpiar los campos de entrada para el próximo concepto
        self.btn_concepto.clear()
        self.btn_cantidad.setValue(0)       
        self.btn_precio.setValue(0.0)

    def connects(self):
        # Funcion para conectar los botones con la funcion de agregar concepto a la tabla y con la funcion que pasa a la siguiente ventana
        self.btn_agregar.clicked.connect(self.agregar_click)
        self.btn_culminar.clicked.connect(self.nextclick)

    def nextclick(self):
        # Funcion para pasar a la siguiente ventana
        self.tw=Ventana3()
        self.hide()

    def set_appear(self):
        # Funcion para establecer la apariencia de la ventana (etiqueta, tamaño, ubicación)
        self.setWindowTitle(txt_titulo)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
