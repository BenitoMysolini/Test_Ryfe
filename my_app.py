from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import Qt 

class FirstWindow(QWidget):
    def __init__(self, *args, **qwargs):
        super(). __init__(*args, **qwargs)
        self.initUI()
    def initUI(self):
        tt="Данное приложение позволит вам с помощью теста Руфье провести первичную диагностику вашего здоровья.\nПроба Руфье представляет собой нагрузочный комплекс, предназначенный для оценки работоспособности сердца при физической нагрузке.\nУ испытуемого, находящегося в положении лежа на спине в течение 5 мин, определяют частоту пульса за 15 секунд;\nзатем в течение 45 секунд испытуемый выполняет 30 приседаний.\nПосле окончания нагрузки испытуемый ложится, и у него вновь подсчитывается число пульсаций за первые 15 секунд,\nа потом — за последние 15 секунд первой минуты периода восстановления.\nВажно! Если в процессе проведения испытания вы почувствуете себя плохо (появится головокружение, шум в\nушах, сильная одышка и др.), то тест необходимо прервать и обратиться к врачу."
        first_window_layout = QVBoxLayout() 
        info_label = QLabel(tt)
        first_window_layout.addWidget(info_label)

        first_window_button = QPushButton('Начать') 
        first_window_layout.addWidget(first_window_button) 

        self.setLayout(first_window_layout)

app = QApplication([]) 
window = FirstWindow()
window.show()
app.exec_()
