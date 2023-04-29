from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QDialog, QWidget, QPushButton

from new_arch.views.widgets.my_label import MyLabel


class GameOverDialog(QDialog):
    def __init__(self, widget: QWidget = None):
        super().__init__(widget)
        self.setFixedSize(350, 200)
        self.title = MyLabel(20, 'Game over', self)
        self.title.setGeometry(QtCore.QRect(0, 0, 350, 40))

        self.winner = MyLabel(15, 'Winner is', self)
        self.winner.setGeometry(QtCore.QRect(0, 70, 350, 40))

        self.back_menu_button = QPushButton(self)
        self.back_menu_button.setGeometry(QRect(80, 140, 200, 40))
        self.back_menu_button.setFont(QFont(None, 15))
        self.back_menu_button.setText('Menu')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = GameOverDialog()
    # ui = Ui_Dialog()
    # ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())