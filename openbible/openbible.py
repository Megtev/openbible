import sys
from PyQt5 import QtWidgets

from ui import OpenBibleUI
from controller import OpenBibleCtrl
from second_window import OpenBibleSecondWindow


def main():
    """Main function."""
    openbible = QtWidgets.QApplication(sys.argv)


    view = OpenBibleUI()
    view.show()

    sview = OpenBibleSecondWindow()
    ctrl = OpenBibleCtrl(view, sview)
    sys.exit(openbible.exec_())


if __name__ == '__main__':
    main()
    app = QtWidgets.QApplication(sys.argv)
