import sys
from PyQt5 import QtWidgets


class OpenBibleMainGui(QtWidgets.QWidget):
    """The main Gui"""

    def __init__(self):
        super().__init__()

        # Set basic geometry of the main window
        self.resize(600, 400)
        self.setWindowTitle('OpenBible')

        # Add menu bar
        # TODO implement all standart features
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.addMenu('File')

        # Add grid layout
        main_grid = QtWidgets.QGridLayout()
        main_grid.setHorizontalSpacing(12)
        main_grid.setVerticalSpacing(24)
        self.setLayout(main_grid)

        # Add second window to show info
        # TODO driver to show and control all info in second window
        self.show_info = ShowInfo()

        # Add some test buttons -----------------
        show_button = QtWidgets.QPushButton('Show', self)
        hide_button = QtWidgets.QPushButton('Hide', self)
        just_button = QtWidgets.QPushButton('Just button', self)

        # self.show_button.move(50, 50)
        show_button.clicked.connect(self.show_slides)
        hide_button.clicked.connect(self.hide_slides)

        main_grid.addWidget(show_button, 1, 1)
        main_grid.addWidget(hide_button, 2, 1)
        # main_grid.add
        # hide_button.hide()
        just_button.hide()
        # End of test button code ---------------

        # Move main window to the center of display and show the window
        self.move_to_center()

    def show_slides(self):
        # Create new windows that shows text on second screen
        # TODO
        print('Show')
        self.show_info.show()
        # self.just_button.show()

    def hide_slides(self):
        # Hide additional window
        print('Hide')
        self.show_info.hide()
        # self.just_button.hide()

    def move_to_center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # Build-in functions

    def closeEvent(self, event):
        # Require additional confirmation to exit
        reply = QtWidgets.QMessageBox.question(
            self, 'Message',
            "Are you sure to quit?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            self.show_info.close()
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
    main_window.show()
    sys.exit(app.exec_())
