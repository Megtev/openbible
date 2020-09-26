import abc
import functools
from PyQt5 import QtWidgets, QtCore


class BasePlugin(abc.ABC):
    """Plugins have to implement some default function to work with the app"""

    def __init__(self, mediator=None) -> None:
        self._mediator = mediator
        return

    @property
    def mediator(self):
        return self._mediator

    @mediator.setter
    def mediator(self, mediator) -> None:
        self._mediator = mediator

    @abc.abstractmethod
    def is_widget(self):
        pass


class ButtonsPlugin(BasePlugin):
    """The plugin implement basic show/hide buttons to control additional
    window"""

    def __init__(self, mediator=None) -> None:
        super().__init__(mediator)
        self._widget = QtWidgets.QWidget()  # Create basic widget
        self.show_button = QtWidgets.QPushButton('Show')  # Create 2 buttons
        self.hide_button = QtWidgets.QPushButton('Hide')

        layout = QtWidgets.QGridLayout()         # Add buttons to basic widget
        layout.addWidget(self.show_button, 0, 0)
        layout.addWidget(self.hide_button, 1, 0)
        self._widget.setLayout(layout)

        self.show_button.clicked.connect(   # Connect buttons to mediator
            functools.partial(self._mediator.show, self)  # methods
        )
        self.hide_button.clicked.connect(
            functools.partial(self._mediator.hide, self)
        )

        # self.show_button.setFixedSize(QtCore.QSize(80, 25))
        self._widget.setSizePolicy(
            QtWidgets.QSizePolicy(
                QtWidgets.QSizePolicy.Fixed,
                QtWidgets.QSizePolicy.Fixed
            )
        )
        self.arrangement = (12, 24)


    def is_widget(self):
        """return True if the plugin is a widget"""
        return True

    def get_widget(self):
        return self._widget


class NullPlugin(BasePlugin):

    def __init__(self, mediator=None) -> None:
        super().__init__(mediator)
        self._widget = QtWidgets.QWidget()  # Create basic widget

        layout = QtWidgets.QGridLayout()
        self._widget.setLayout(layout)
        self.arrangement = (0, 0)
        self._widget.setSizePolicy(
            QtWidgets.QSizePolicy(
                QtWidgets.QSizePolicy.Minimum,
                QtWidgets.QSizePolicy.Minimum
            )
        )

    def is_widget(self):
        return True

    def get_widget(self):
        return self._widget