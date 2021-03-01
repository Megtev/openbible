from PyQt5 import (QtWidgets, QtGui, QtCore)


class OpenBibleSecondWindow(QtWidgets.QWidget):
    """OpenBible Second View for second window"""

    test_verse = (
        'For God so loved the world, that he gave his only begotten Son,'
        ' that whosoever believeth in him should not perish, but have'
        ' everlasting life.\nJohn 3:16'
    )

    def __init__(self):
        """Second View initializer."""
        super(OpenBibleSecondWindow, self).__init__()

        # Set general layout and add small widget
        self.general_layout = QtWidgets.QGridLayout()
        self._verse = QtWidgets.QLabel(self)
        self.general_layout.addWidget(self._verse)
        self.setLayout(self.general_layout)


    def show_text(self):
        self._verse.setText(self.test_verse)
        self._verse.setWordWrap(True)
        self._verse.setAlignment(
            QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter
        )
        self._verse.setFrameStyle(QtWidgets.QLabel.Box)

        # Set font
        font = QtGui.QFont('Arial', 50)
        font.setBold(True)
        font_size = self.get_good_font_size(font, self.rect(), self.test_verse)
        font.setPointSize(font_size)

        self._verse.setFont(font)
        self.show()

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
