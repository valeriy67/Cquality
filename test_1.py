import sys

from PyQt5.Qt import QVBoxLayout, QLabel, QDialog, QDialogButtonBox, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication


class InfoDialog(QDialog):

    def __init__(self, info_str, parent=None):
        super(InfoDialog, self).__init__(parent)

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel(info_str))

        buttons = QDialogButtonBox(QDialogButtonBox.Ok, Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)

        layout.addWidget(buttons)


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon('RM.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(qApp.quit)

        infoAction = QAction(QIcon(), "Info", self)
        infoAction.triggered.connect(self.onInfoAction)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)
        self.toolbar.addAction(infoAction)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Toolbar')
        self.show()

    def onInfoAction(self):
        w = InfoDialog("Some information", self)
        w.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())