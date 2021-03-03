import sys
import os

from PyQt5 import QtWidgets

from ui import OpenBibleUI
from second_window import OpenBibleSecondWindow
from controller import OpenBibleCtrl
from model import OpenBibleModel


def main():
    """Main function."""
    openbible = QtWidgets.QApplication(sys.argv)

    view = OpenBibleUI()    # Create View
    view.show()

    sview = OpenBibleSecondWindow()  # Create second window
    model = OpenBibleModel(os.path.join(os.path.abspath(
        os.path.dirname(__file__)), 'translations')
    )
    ctrl = OpenBibleCtrl(view, sview, model)    # Create controller
                                                # between view and sview
    print(__file__)
    sys.exit(openbible.exec_())


if __name__ == '__main__':
    main()
