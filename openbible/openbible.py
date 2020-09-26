import sys
from PyQt5 import QtWidgets

from mediator import (GuiPluginMediator, )
from plugins import (ButtonsPlugin, NullPlugin)


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

        # TODO plugins manager
        plugins = [ButtonsPlugin, NullPlugin]
        self.mediator = GuiPluginMediator(plugins)

        main_widget = QtWidgets.QWidget()
        for (plugin, widget) in zip(self.mediator.get_plugins(),
                          self.mediator.get_widgets()):
            main_grid.addWidget(widget, *plugin.arrangement)
        main_widget.setLayout(main_grid)

        self.setCentralWidget(main_widget)
        # Move main window to the center of display and show the window
        self.move_to_center()

    def move_to_center(self):
        # Move main window to center of the display (not testet with multiple
        # displays)
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # Build-in functions

    '''
    def closeEvent(self, event):
        # Require additional confirmation to exit
        reply = QtWidgets.QMessageBox.question(
            self, 'Message',
            "Are you sure to quit?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            self.mediator.close(self)
            event.accept()
        else:
            event.ignore()
    '''


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = OpenBibleMainGui()
    main_window.show()
    sys.exit(app.exec_())
