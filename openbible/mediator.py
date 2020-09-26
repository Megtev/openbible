from PyQt5 import (QtWidgets, QtGui, QtCore)


class AdditionalWindow(QtWidgets.QMainWindow):
    """Addidional window for second monitor, to show verse, lyrics..."""

    test_verse = (
        'For God so loved the world, that he gave his only begotten Son,'
        ' that whosoever believeth in him should not perish, but have'
        ' everlasting life.\nJohn 3:16'
    )

    def __init__(self):
        super().__init__()
        self.setGeometry(900, 900, 960, 520)
        self.setWindowTitle('AdditionalWindow')

        self.view = QtWidgets.QGraphicsView()

        scene = QtWidgets.QGraphicsScene()

        t = QtWidgets.QGraphicsTextItem(self.test_verse)
        # font = t.font()
        font = QtGui.QFont('Arial', 60)
        font.setBold(True)
        t.setFont(font)
        t.setTextWidth(800)
        scene.addItem(t)

        self.view.setScene(scene)
        self.setCentralWidget(self.view)


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
