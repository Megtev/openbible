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
        for tr in translations:
            self._translations[tr.lower()] = tr

        self._current_translation_json = []
        self._init_books(self.get_current_translation())

    def get_translations(self):
        """Get available translations."""
        return self._translations

    def get_current_translation(self):  # TODO get default translations
        """Get current translation."""
        # return self._translations[0]

    def get_books(self, translation: str):  # TODO get list of books by
        """Get list of books by translation."""     # translation
        pass

    def _init_books(self, tr):  # TODO implement books initializating
        # self._current_translation_json = json.loads()
        pass