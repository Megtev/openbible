import sys
from PyQt5 import QtWidgets


class OpenBibleMainGui(QtWidgets.QWidget):
    """The main Gui"""

    def __init__(self):
        super().__init__()
        self.show_button = QtWidgets.QPushButton('Show', self)
        self.hide_button = QtWidgets.QPushButton('Hide', self)
        self.just_button = QtWidgets.QPushButton('Just button', self)
        self.init_ui()
        self.show_info = ShowInfo()

    def init_ui(self):
        # init main UI
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('OpenBible')

        self.show_button.move(50, 50)
        self.show_button.clicked.connect(self.show_slides)

        self.hide_button.move(50, 75)
        self.hide_button.clicked.connect(self.hide_slides)

        self.just_button.move(50, 100)
        self.just_button.hide()
        # self.show_button.setText('Hide')

        self.show()

    def show_slides(self):
        # Create new windows that shows text on second screen
        # TODO
        print('Show')
        self.show_info.show()
        self.just_button.show()
        # self.show_button.setText('Hide')

    def hide_slides(self):
        # Hide additional window
        print('Hide')
        self.show_info.hide()
        self.just_button.hide()

    # Build-in functions

    def closeEvent(self, event):
        # Require additional confirmation to exit
        reply = QtWidgets.QMessageBox.question(
            self, 'Message',
            "Are you sure to quit?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


class ShowInfo(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(900, 900, 300, 250)
        self.setWindowTitle('ShowInfo')
        # self.show()

    def show_second_windows(self):
        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = OpenBibleMainGui()
    sys.exit(app.exec_())
