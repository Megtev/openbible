import sys
from PyQt5 import QtWidgets

from plugins import (BasePlugin, ButtonsPlugin)


class OpenBibleMainGui(QtWidgets.QMainWindow):
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

        plugins = [ButtonsPlugin(), ]
        mediator = GuiPluginMediator(plugins)

        widget = QtWidgets.QWidget()
        plugins[0]
        main_grid.addWidget(plugins[0], 0, 0)
        widget.setLayout(main_grid)

        self.setCentralWidget(widget)
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


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = OpenBibleMainGui()
    main_window.show()
    sys.exit(app.exec_())
