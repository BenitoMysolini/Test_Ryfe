# напиши здесь код третьего экрана приложения
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import Qt 

class ResultWindiw(QWidget):
    def __init__(self, *args, **qwargs):
        super(). __init__(*args, **qwargs)
        self.initUI()
    def initUI(self):
        self.main_layout = QVBoxLayout()

        self.name_lable = QLabel("ФИО")
        self.index_lable = QLabel("ИНДЕКС РУФЬЕ")
        self.result_lable = QLabel("РАБОТОСПОСОБНОСТЬ СЕРДЦА:НИЗ.СРЕД.ВЫС.")


        self.main_layout.addWidget(self.name_lable,alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.index_lable,alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.result_lable,alignment=Qt.AlignCenter)

        self.setLayout(self.main_layout)

