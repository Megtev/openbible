from PyQt5 import (QtWidgets, QtCore, QtGui,)


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
        self.left_layout = QtWidgets.QVBoxLayout()
        self.general_layout = QtWidgets.QHBoxLayout()
        self._central_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(self._central_widget)
        self._central_widget.setLayout(self.general_layout)
        self.general_layout.addLayout(self.left_layout, 3)

        # Create temp line for testing
        self._create_combo_boxes()
        self._create_text_inputs() # Temporary
        self._create_buttons()

        # self.temp_layout.addWidget(QtWidgets.QWidget(self), 2)

        # Create screens for preview
        self._create_screens()
        self._preview.set_text('some', 'this', 5)
        self._view.set_text('some', 'this', 5)

    # Function to create UI

    def _create_screens(self):
        # Create 2 screens
        self._preview = MiniSecondWindow(self)
        self._view = MiniSecondWindow(self)

        # Add screens to layout
        self.screen_layout = QtWidgets.QVBoxLayout()
        self.screen_layout.addWidget(self._view)
        self.screen_layout.addWidget(self._preview)
        self.screen_layout.addStretch()
        self.general_layout.addLayout(self.screen_layout, 1)

    def _create_combo_boxes(self):
        """Widget to create combobox to choose book/chapter/verse"""
        # Create combo boxes
        self._tr = QtWidgets.QComboBox(self)
        self.book = QtWidgets.QComboBox(self)
        self.chapter = QtWidgets.QComboBox(self)
        self.verse = QtWidgets.QComboBox(self)

        # Add layout and arrange combo boxes
        self._ref_layout = QtWidgets.QHBoxLayout()
        self._ref_layout.addWidget(self._tr, 1)
        self._ref_layout.addWidget(self.book, 5)
        self._ref_layout.addWidget(self.chapter, 1)
        self._ref_layout.addWidget(self.verse, 1)

        self.left_layout.addLayout(self._ref_layout)

    def add_translations(self, translations: list):
        # Add basic data to combo boxes
        for i in range(len(translations)):     # Add translates
            self._tr.addItem(translations[i], i)

    def set_translation(self, tr):
        """Select translation by index"""
        self._tr.setCurrentIndex(tr)

    def set_books(self, books: list):
        self.book.clear()
        for i in range(len(books)):     # Add books
            self.book.addItem(books[i], i)

    def set_chapters(self, chapters: int):
        self.chapter.clear()
        for i in range(1, chapters + 1):    # Add chapters
            self.chapter.addItem(str(i), i)

    def set_verses(self, verses):
        self.verse.clear()
        for i in range(1, len(verses) + 1):   # Add verses, but only numbers
            self.verse.addItem(str(i), i)

    def _create_text_inputs(self):
        # Create 2 input lines
        self._verse_input = QtWidgets.QLineEdit()
        self._verse_ref = QtWidgets.QLineEdit()
        self.send_verse_button = QtWidgets.QPushButton('Send')

        # Add layout and arrange lines
        self._verse_layout = QtWidgets.QHBoxLayout()
        self._verse_layout.addWidget(self._verse_input, 3)
        self._verse_layout.addWidget(self._verse_ref, 1)
        self._verse_layout.addWidget(self.send_verse_button, 1)

        self.left_layout.addLayout(self._verse_layout)

    def _create_buttons(self):
        # Create 2 buttons
        self.show_button = QtWidgets.QPushButton('Show')
        self.hide_button = QtWidgets.QPushButton('Hide')

        # Add layout and arrange them
        self._button_layout = QtWidgets.QHBoxLayout()
        self._button_layout.addWidget(self.show_button)
        self._button_layout.addWidget(self.hide_button)

        # Add _button_layout to general_layout
        self.left_layout.addLayout(self._button_layout)

    # Functions for process

    def get_verse_ref(self):
        verse = self._verse_input.text()
        ref = self._verse_ref.text()
        return (verse, ref)

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


class MiniSecondWindow(QtWidgets.QWidget):
    """Window for preview in UI."""

    def __init__(self, parent=None):  # TODO better __init__
        super(MiniSecondWindow, self).__init__(parent=parent)
        self.general_layout = QtWidgets.QGridLayout()
        self._verse = QtWidgets.QLabel(self)
        self.general_layout.addWidget(self._verse)
        self.setLayout(self.general_layout)

        self._verse.setText('')  # Set default text empty
        self._verse.setWordWrap(True)
        self._verse.setAlignment(  # Set text in the center of window
            QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter
        )
        self._verse.setFrameStyle(QtWidgets.QLabel.Box)
        font = QtGui.QFont('Arial', 5)  # Default font
        font.setBold(True)  # TODO add ability to change fonts

    def set_text(self, verse: str, ref: str, font_size: int):
        font = QtGui.QFont('Arial', 50)  # Default font
        font.setBold(True)  # TODO add ability to change fonts
        font.setPointSize(font_size)
        self._verse.setFont(font)
        self._verse.setText('{}\n{}'.format(verse, ref))

    # Build-in funtion

    def resizeEvent(self, event: QtGui.QResizeEvent) -> None:
        # Change size of text while resizing
        width = self.width()
        self.resize(width, int(width / 16 * 9))
        # self.updateGeomentry()
        super(MiniSecondWindow, self).resizeEvent(event)
        return
