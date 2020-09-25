import abc

from PyQt5 import QtWidgets


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


class ButtonsPlugin(BasePlugin):
    """The plugin implement basic show/hide buttons to control additional
    window"""

    def __init__(self, mediator=None) -> None:

        super().__init__(mediator)

        self._widget = QtWidgets.QWidget()
        self.show_button = QtWidgets.QPushButton('Show')
        self.hide_button = QtWidgets.QPushButton('Hide')
        self.show_button.clicked.connect(self._mediator.show(self))
        self.hide_button.clicked.connect(self._mediator.hide(self))

        layout = QtWidgets.QGridLayout()
        layout.addWidget(self.show_button, 0, 0)
        layout.addWidget(self.hide_button, 0, 0)
        self._widget.setLayout(layout)

    def is_widget(self):
        return True

    def get_widget(self):
        return self._widget
