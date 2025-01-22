import sys
from PyQt6.QtWidgets import QApplication, \
                            QLabel, \
                            QLineEdit, \
                            QMainWindow, \
                            QPushButton


def solve(str_obj, i = 2):
    if type(str_obj) is str and len(str_obj) > 0:
        if i <= 0:
            return (0, str_obj)
    else:
        return (1, "Введите строку!")
    copied_str = str_obj * i
    result = copied_str[::-i]
    return (0, result)


class Ui_intrerface(QMainWindow):
    def __init__(self):
        super().__init__()
        # инициализируем окно
        self.setWindowTitle('Работа со строками')
        self.setGeometry(300, 300, 400, 200)
        self.str_obj_label = QLabel(self)
        self.i_label = QLabel(self)
        self.result_label = QLabel(self)
        self.input_str = QLineEdit(self)
        self.input_i = QLineEdit(self)
        self.result = QLineEdit(self)
        self.result.setReadOnly(True)
        self.run_btn = QPushButton(self)
        self.restart_btn = QPushButton(self)
        self.str_obj_label.setGeometry(20, 20, 150, 20)
        self.i_label.setGeometry(20, 60, 150, 20)
        self.result_label.setGeometry(20, 100, 150, 20)
        self.run_btn.setGeometry(50, 150, 160, 30)
        self.input_str.setGeometry(200, 20, 155, 20)
        self.input_i.setGeometry(200, 60, 155, 20)
        self.result.setGeometry(200, 100, 155, 20)
        self.restart_btn.setGeometry(250, 150, 120, 30)
        self.run_btn.setText('Преобразовать строку')
        self.restart_btn.setText('Очистить поля')
        self.str_obj_label.setText('Введите строку (str_obj)')
        self.i_label.setText('Введите число i')
        self.result_label.setText('Полученный результат')
        self.restart_btn.clicked.connect(self.restart)
        self.run_btn.clicked.connect(self.run)

    def restart(self): # очистка
        self.input_str.clear()
        self.input_i.clear()
        self.result.clear()
        self.statusBar().clearMessage()

    def run(self):
        self.result.clear()
        string = self.input_str.text()
        i = self.input_i.text()
        if i == '':
            i = '2'
        try:
            i = int(i)
            self.error, self.res = solve(string, int(i))
            if not(self.error):
                self.result.setText(self.res)
                self.statusBar().clearMessage()
            else:
                self.statusBar().showMessage('Введите строку') # проверка строки
        except Exception:
            self.statusBar().showMessage('Аргумент i должен быть целым числом') # проверка i 


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ui_intrerface()
    ex.show()
    sys.exit(app.exec())