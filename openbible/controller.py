from functools import partial

from ui import OpenBibleUI
from second_window import OpenBibleSecondWindow


class OpenBibleCtrl:
    """OpenBIble controller class."""

    def __init__(self, view: OpenBibleUI, view2: OpenBibleSecondWindow):
        """Controller initializer."""
        self._view = view
        self._sview = view2

        # Connect signals and slots
        self._connectSignals()

    def _connectSignals(self):
        self._view.show_button.clicked.connect(self._sview.show_text)
        self._view.hide_button.clicked.connect(self._sview.hide)
