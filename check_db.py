from PyQt5 import QtCore
from handler.db_handler import login, register


class ValidateThread(QtCore.QThread):
    signal = QtCore.pyqtSignal(str)

    def thr_login(self, username, password):
        """ валидация для авторизации """
        login(username, password, self.signal)

    def thr_register(self, username, password):
        """ валидация для регистрации """
        register(username, password, self.signal)