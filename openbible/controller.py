from functools import partial

from ui import OpenBibleUI
from second_window import OpenBibleSecondWindow


class OpenBibleCtrl:
    """OpenBible controller class."""

    def __init__(self, view: OpenBibleUI, view2: OpenBibleSecondWindow):
        """Controller initializer."""
        self._view = view
        self._sview = view2

        # Connect signals and slots
        self._connect_signals()

    def _connect_signals(self):  # Connect some buttons to second window
        self._view.show_button.clicked.connect(self._sview.show)
        self._view.hide_button.clicked.connect(self._sview.hide)
        self._view.close_accept.connect(self._sview.close)  # Close all windows
        self._view.send_verse_button.clicked.connect(
            lambda: self._sview.set_text(*self._view.get_verse_ref())
        )   # Send verse to second window
