import os
import json


class OpenBibleModel:   # TODO Implement OpenBible Model
    """OpenBible Model class."""

    def __init__(self, tr_path: str):
        """Initialize Model."""
        self._tr_path = tr_path  # Save path

        # Every folder represent translation
        translations = os.listdir(self._tr_path)
        translations.remove('README.MD')  # Remove default file
        self._translations = {}
        for tr in translations:     # TODO check config.json and all files
            self._translations[tr.lower()] = tr

        self._current_translation_json = {}
        self._current_book_json = {}
        # self._init_books(self.get_current_translation())
        self._current_translation = 'kjv'
        self._current_book = 0
        self._current_chapter = 0
        self._current_verse = 0

    def get_translations(self):
        """Get available translations."""
        return self._translations

    def get_current_translation(self):  # TODO get default translations
        """Get current translation."""
        # return self._translations[0]
        return self._current_translation    # Temporary send KJV translation

    def set_translation(self, tr):
        self._current_translation = tr
        self._init_books(tr)
        self.set_book(self._current_book)

    def get_books(self):  # TODO get list of books by translation
        """Get list of books by translation."""
        return [book['full_name'] for book
                in self._current_translation_json['books']
                ]

    def set_book(self, book: int):
        """Set current book."""
        self._current_book = book
        self._current_book_json = json.load(open(os.path.join(
            self._tr_path,                          # Load book from file and
            self.get_current_translation().upper(), # return json of the book
            self._current_translation_json['books']
                [self._current_book]['file_name']),
            mode='rt', encoding='utf-8'
        ))

    def get_chapters(self) -> int:
        """Get quantity of chapters in current book."""
        return (self._current_translation_json['books']
                [self._current_book]['chapters_qty']
        )

    def set_chapter(self, chapter: int):
        self._current_chapter = chapter

    def get_verses(self) -> list:
        """Get verses in given book and chapter."""
        try:
            book_verses = self._current_book_json['chapters']
            return book_verses[self._current_chapter]
        except IndexError:
            self._current_chapter = 0
            self._current_verse = 0
            book_verses = self._current_book_json['chapters']
            return book_verses[self._current_chapter]

    def get_verse(self):
        """Return only selected verse"""
        return (self._current_book_json['chapters'][self._current_chapter]
            [self._current_verse]
        )

    def set_verse(self, verse: int):    # Set current verse, not affect
        """Set current verse."""        # second screen
        self._current_verse = verse

    def get_ref(self):
        """Get reference for current verse"""
        return '{} {}:{}'.format(
            self._current_book_json['name'],
            self._current_chapter + 1,
            self._current_verse + 1
        )

    def show_verse(self):
        pass

    def _init_books(self, tr):  # TODO implement books initializating
        # self._current_translation_json = json.loads()
        self._current_translation_json = json.load(  # Load books info from
            open(os.path.join(self._tr_path,         # config.json file
                              self.get_current_translation().upper(),
                              'config.json'
                              ), mode='rt', encoding='utf-8'
            )
        )
