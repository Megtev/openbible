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
        self._init_books(self.get_current_translation())
        self._current_book = 0

    def get_translations(self):
        """Get available translations."""
        return self._translations

    def get_current_translation(self):  # TODO get default translations
        """Get current translation."""
        # return self._translations[0]
        return 'kjv'    # Temporary send KJV translation

    def get_books(self):  # TODO get list of books by translation
        """Get list of books by translation."""
        return [book['full_name'] for book
                in self._current_translation_json['books']
                ]

    def get_chapters(self):
        """Get quantity of chapters in current book."""
        return (self._current_translation_json['books']
                [self._current_book]['chapters_qty']
        )

    def _init_books(self, tr):  # TODO implement books initializating
        # self._current_translation_json = json.loads()
        self._current_translation_json = json.load(  # Load books info from
            open(os.path.join(self._tr_path,         # config.json file
                              self.get_current_translation().upper(),
                              'config.json'
                              ), mode='rt', encoding='utf-8'
            )
        )
