from PyQt5 import (QtWidgets, QtCore)

from plugins import ButtonsPlugin


class OpenBibleUI(QtWidgets.QMainWindow):
    """OpenBible View (GUI)."""

    close_accept = QtCore.pyqtSignal()  # Signal to close additional windows

    def __init__(self):
        """View initializer."""
        super(OpenBibleUI, self).__init__()

        # Set some properties
        self.setWindowTitle("OpenBible")
        self.resize(600, 400)

        # Set central widget and general layout
        self.general_layout = QtWidgets.QVBoxLayout()
        self._central_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(self._central_widget)
        self._central_widget.setLayout(self.general_layout)

        # Create temp line for testing
        self._create_buttons()

    def _create_buttons(self):
        # Create 2 buttons
        self.show_button = QtWidgets.QPushButton('Show')
        self.hide_button = QtWidgets.QPushButton('Hide')

        # Add layout and arrange them
        self._button_layout = QtWidgets.QHBoxLayout()
        self._button_layout.addWidget(self.show_button)
        self._button_layout.addWidget(self.hide_button)

        # Add _button_layout to general_layout
        self.general_layout.addLayout(self._button_layout)

    # Build-in funtion

    def closeEvent(self, event):
        # Require additional confirmation to exit
        reply = QtWidgets.QMessageBox.question(
            self, 'Message',
            "Are you sure to quit?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            self.close_accept.emit()    # Close additional windows
            event.accept()
        else:
            event.ignore()
