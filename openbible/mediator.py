from PyQt5 import QtWidgets


class AdditionalWindow(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(900, 900, 960, 520)
        self.setWindowTitle('AdditionalWindow')

    def show_second_windows(self):
        self.show()


class GuiPluginMediator:
    """Mediator to control all plugins"""

    def __init__(self, plugins: list) -> None:
        # Get all plugins and arrange them and create second window
        self._additional_window = AdditionalWindow()

        self._widgets = []
        self._plugins = []
        for plugin in plugins:
            self._plugins.append(plugin(self))

        for plugin in self._plugins:
            if plugin.is_widget():
                self._widgets.append(plugin.get_widget())

    def notify(self, sender, event) -> None:
        # Notify the mediator about changes
        pass

    def show(self, sender) -> None:
        self._additional_window.show()

    def hide(self, sender) -> None:
        self._additional_window.hide()

    def close(self, sender) -> None:
        self._additional_window.close()

    def get_widgets(self):
        return self._widgets

    def get_plugins(self):
        return self._plugins
