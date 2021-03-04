from functools import partial

from ui import OpenBibleUI
from second_window import OpenBibleSecondWindow
from model import OpenBibleModel


class OpenBibleCtrl:
    """OpenBible controller class."""

    def __init__(self, view: OpenBibleUI, view2: OpenBibleSecondWindow,
                 model: OpenBibleModel):
        """Controller initializer."""
        self._view = view
        self._sview = view2
        self._model = model

        self._initialize_default_translations()  # Initialize translations
        # Connect signals and slots
        self._connect_signals()

    def _connect_signals(self):  # Connect some buttons to second window
        self._view.show_button.clicked.connect(self._sview.show)
        self._view.hide_button.clicked.connect(self._sview.hide)
        self._view.close_accept.connect(self._sview.close)  # Close all windows
        self._view.send_verse_button.clicked.connect(
            lambda: self._sview.set_text(*self._view.get_verse_ref())
        )   # Send verse to second window

        # Connect QComboBox for changing translations/books/chapters/verse
        # TODO add ability to change translations
        self._view.book.activated.connect(
            self._set_book)     # Book's changed, so change chapters and verses
        self._view.chapter.activated.connect(
            self._set_chapter)  # Chapter's changed, change verses
        self._view.verse.activated.connect(     # Show selected verse
            self._set_verse)

    def _initialize_default_translations(self):
        translations = self._model.get_translations()
        self._view.add_translations(
            translations
        )

        # TODO set translation by settings
        self._view.set_translation(translations.index('KJV'))
        self._model.set_translation('kjv')  # Set default translation

        # Add books in UI
        self._view.set_books(self._model.get_books())
        # Add chapters in UI
        self._view.set_chapters(self._model.get_chapters())
        # Add verses in UI
        self._view.set_verses(self._model.get_verses())

    def _set_book(self, book):
        """Set new book."""
        self._model.set_book(book)  # Set new book in model
        self._set_chapter(0)  # Get new chapters
        self._view.set_chapters(self._model.get_chapters())

    def _set_chapter(self, chapter):
        """Set new chapter."""
        self._model.set_chapter(chapter)    # Set chapter
        self._model.set_verse(0)    # Set first verse
        self._view.set_verses(self._model.get_verses()) # Show verses in UI

    def _set_verse(self, verse: int):
        """Set and show new verse."""
        self._model.set_verse(verse)    # Set verse
        verse = self._model.get_verse()  # Get text of the verse
        ref = self._model.get_ref()
        self._sview.set_text(verse, ref)  # Show text in second screen
