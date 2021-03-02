import sys
from PyQt5 import QtWidgets

from ui import OpenBibleUI
from controller import OpenBibleCtrl
from second_window import OpenBibleSecondWindow


def main():
    """Main function."""
    openbible = QtWidgets.QApplication(sys.argv)

    view = OpenBibleUI()    # Create View
    view.show()

    sview = OpenBibleSecondWindow()  # Create second window
    ctrl = OpenBibleCtrl(view, sview)   # Create controller between view
                                        # and sview
    sys.exit(openbible.exec_())


if __name__ == '__main__':
    main()
