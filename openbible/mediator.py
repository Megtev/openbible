from PyQt5 import QtWidgets

from plugins import BasePlugin

class AdditionalWindow(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(900, 900, 300, 250)
        self.setWindowTitle('AdditionalWindow')
        # self.show()

    def show_second_windows(self):
        self.show()


class GuiPluginMediator():
    """Mediator to control all plugins"""

    def __init__(self, plugins : list, *, arrangement=None) -> None:
        # Get all plugins and arrange them and create second window
        self._plugins = plugins
        for plugin in plugins:
            plugin(self)

        self._additional_window = AdditionalWindow()

    def notify(self, sender : BasePlugin, event) -> None:
        # Notify the mediator about changes
        pass

    def show(self, sender : BasePlugin) -> None:
        self._additional_window.show()

    def hide(self, sender : BasePlugin) -> None:
        self._additional_window.hide()
