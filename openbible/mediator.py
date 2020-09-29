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

        self.widget = QtWidgets.QWidget(self)
        self.grid = QtWidgets.QGridLayout()
        verse_label = QtWidgets.QLabel()
        verse_label.setText(self.test_verse)
        verse_label.setWordWrap(True)
        verse_label.setAlignment(
            QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter
        )
        verse_label.setFrameStyle(QtWidgets.QLabel.Box)
        font = QtGui.QFont('Arial', 50)
        font.setBold(True)
        font_size = self.get_good_font_size(font, self.rect(), self.test_verse)
        font.setPointSize(font_size)

        verse_label.setFont(font)
        self.grid.addWidget(verse_label)
        self.widget.setLayout(self.grid)
        self.setCentralWidget(self.widget)

    def get_good_font_size(
            self, font: QtGui.QFont, rect: QtCore.QRect, text: str,
            *, step=5, max_size=80, min_size=0
    ) -> int:
        """Return the max size of the font that text can fit"""
        current_font_size = max_size + 5
        while True:
            current_font_size -= 5
            font.setPointSize(current_font_size)
            font_metrics = QtGui.QFontMetrics(font)

            sized_rect = font_metrics.boundingRect(
                rect,
                QtCore.Qt.AlignCenter | QtCore.Qt.TextWordWrap,
                text
            )
            if (sized_rect.height() < rect.height()
                    and sized_rect.width() < rect.width()):
                break
        return font.pointSize()

    def show_text(self):
        pass


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
        # self._additional_window.showFullScreen()

    def hide(self, sender) -> None:
        self._additional_window.hide()

    def close(self, sender) -> None:
        self._additional_window.close()

    def get_widgets(self):
        return self._widgets

    def get_plugins(self):
        return self._plugins
