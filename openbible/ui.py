from PyQt5 import QtWidgets

from plugins import ButtonsPlugin


class OpenBibleUI(QtWidgets.QMainWindow):
    """OpenBible View (GUI)."""

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
