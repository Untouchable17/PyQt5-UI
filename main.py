import sys

from PyQt5 import QtWidgets

from check_db import ValidateThread
from ui_config import UIForm


class Interface(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = UIForm()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.registration)
        self.ui.pushButton_2.clicked.connect(self.authentication)
        self.base_line_edit = [self.ui.lineEdit, self.ui.lineEdit_2]

        self.check_db = ValidateThread()
        self.check_db.signal.connect(self.signal_handler)

    def validation_data(funct):
        """  Декоратор для валидации данных
        """
        def wrapper(self):
            for line_edit in self.base_line_edit:
                if len(line_edit.text()) == 0:
                    return
            funct(self)

        return wrapper

    def signal_handler(self, value):
        """ Обработчик входящих сигналов """
        QtWidgets.QMessageBox.about(self, 'Оповещение', value)

    @validation_data
    def authentication(self):
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        self.check_db.thr_login(username, password)

    @validation_data
    def registration(self):
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        self.check_db.thr_register(username, password)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mywin = Interface()
    mywin.show()
    sys.exit(app.exec_())
