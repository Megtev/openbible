from PyQt5 import (QtWidgets, QtGui, QtCore)


class OpenBibleSecondWindow(QtWidgets.QWidget):
    """OpenBible Second View for second window"""

    test_verse = (
        'For God so loved the world, that he gave his only begotten Son,'
        ' that whosoever believeth in him should not perish, but have'
        ' everlasting life.\nJohn 3:16'
    )

    def __init__(self, parent=None):
        """Second View initializer."""
        super(OpenBibleSecondWindow, self).__init__(parent=parent)

        # Set general layout and add small widget
        self.general_layout = QtWidgets.QGridLayout()
        self._verse = QtWidgets.QLabel(self)
        self.general_layout.addWidget(self._verse)
        self.setLayout(self.general_layout)

        # TODO add ability to show full screen on other monitors
        display_monitor = 1     # Num of the monitor
        monitor = QtWidgets.QDesktopWidget().screenGeometry(display_monitor)

        self.move(monitor.left(), monitor.top())

        self.show_window()
        self._verse.setText('')     # Set default text empty
        self._font_size = None
        # self.resize(960, 540)       # Temporary set size of second window

    def show_window(self):
        self._verse.setWordWrap(True)
        self._verse.setAlignment(       # Set text in the center of window
            QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter
        )
        self._verse.setFrameStyle(QtWidgets.QLabel.Box)

        # Set font
        font = QtGui.QFont('Arial', 50)     # Default font
        font.setBold(True)                  # TODO add ability to change fonts
        font_size = self.get_good_font_size(font,
                                            self.rect(),
                                            self._verse.text())
        font.setPointSize(font_size)
        self._font_size = font_size

        self._verse.setFont(font)

    def get_good_font_size(     # TODO increase stability and speed
            self, font: QtGui.QFont, rect: QtCore.QRect, text: str,
            *, step=5, max_size=80, min_size=0
    ) -> int:
        """Return the max size of the font that text can fit"""
        current_font_size = max_size + 5    # Set max size of the font
        while True:     # Iterate size font while it fit into additional window
            current_font_size -= 5
            font.setPointSize(current_font_size)
            font_metrics = QtGui.QFontMetrics(font)

            sized_rect = font_metrics.boundingRect(  # Return rect of text with
                rect,                                # current font
                QtCore.Qt.AlignCenter | QtCore.Qt.TextWordWrap,
                text
            )
            if (sized_rect.height() < rect.height()  # Check if font is not
                    and sized_rect.width() < rect.width()):  # too large
                break
        return font.pointSize()

    def set_text(self, verse: str, ref: str) -> None:
        """Set new text in the window"""
        self._verse.setText('{}\n{}'.format(verse, ref))
        self.show_window()

    # Build-in functions

    def resizeEvent(self, event: QtGui.QResizeEvent) -> None:
        # Change size of text while resizing
        super(OpenBibleSecondWindow, self).resizeEvent(event)
        self.show_window()
        return
