import time
from pyqtgraph.Qt import QtCore, QtGui, QtWidgets
import sys

from MainWindow import MainWindow

app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())
