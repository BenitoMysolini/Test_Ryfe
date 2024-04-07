from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import Qt 

class SecondWindow(QWidget):
    def __init__(self, *args, **qwargs):
        super(). __init__(*args, **qwargs)
        self.initUI()
    def initUI(self):
        main_layout = QHBoxLayout()
        left_layout = QVBoxLayout()
        right_layout = QVBoxLayout()

        label_name = QLabel("Введите Ф.И.О.")
        input_name = QLineEdit()
        input_name.setPlaceholderText("Акакиев Акикий Акакиевич")

        label_age = QLabel("Полных лет:")
        input_age = QLineEdit()
        input_age.setPlaceholderText("69")

        label_inst_1 = QLabel("Инструкция №1")

        button_test1 = QPushButton("Начать первый тест")

        input_test1 = QLineEdit()

        label_inst_2 = QLabel("Инструкция №2")

        button_test2 = QPushButton("Начать второй тест")

        label_inst_3 = QLabel("Инструкция №3")     
   
        button_test3 = QPushButton("Начать финальный тест")

        input_test2 = QLineEdit()
        input_test3 = QLineEdit()

        button_result = QPushButton('Получить результат:') 

        left_layout.addWidget(label_name, alignment=Qt.AlignLeft)
        left_layout.addWidget(input_name, alignment=Qt.AlignLeft)
        left_layout.addWidget(label_age, alignment=Qt.AlignLeft)
        left_layout.addWidget(input_age, alignment=Qt.AlignLeft)
        left_layout.addWidget(label_inst_1, alignment=Qt.AlignLeft)
        left_layout.addWidget(button_test1, alignment=Qt.AlignLeft)
        left_layout.addWidget(input_test1, alignment=Qt.AlignLeft)
        left_layout.addWidget(label_inst_2, alignment=Qt.AlignLeft)
        left_layout.addWidget(button_test2, alignment=Qt.AlignLeft)
        left_layout.addWidget(label_inst_3, alignment=Qt.AlignLeft)
        left_layout.addWidget(button_test3, alignment=Qt.AlignLeft)
        left_layout.addWidget(input_test2, alignment=Qt.AlignLeft)
        left_layout.addWidget(input_test3, alignment=Qt.AlignLeft)
        left_layout.addWidget(button_result, alignment=Qt.AlignLeft)

        label_timer = QLabel('00:00')
        right_layout.addWidget(label_timer, alignment=Qt.AlignLeft)

        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)

        self.setLayout(main_layout)

app = QApplication([]) 
window = SecondWindow()
window.setFont(QFont("calibri", 15))
window.show()
app.exec_()