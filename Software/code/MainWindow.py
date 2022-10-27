import time
from pyqtgraph.Qt import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit
import webbrowser
from statistics import mean
import datetime

# TODO
# change python lists into numpy arrays

from main import main


class MainWindow(
    QtWidgets.QMainWindow,
):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("FilaMentals")

        self.setFixedWidth(1155)

        self.graphWidget = pg.PlotWidget()
        self.graphWidget.setLabel("left", "Diameter (mm)")
        self.graphWidget.setLabel("bottom", "Cycles")
        self.setCentralWidget(self.graphWidget)
        self.graphWidget.setYRange(0, 7, padding=0)

        self.filename = "../output/data-" + datetime.datetime.now().isoformat() + ".txt"
        self.file = open(self.filename, "w")

        # list of all the diameter values to calculate the mean
        self.diameter = []
        # variables for plotting
        self.x = list(range(-100, 0))  # 100 time points
        self.y = [0] * 100  # 100 data points


        # black square to put buttons
        self.mean_diameter_label = QLabel("lalala", self)
        self.mean_diameter_label.setGeometry(QtCore.QRect(0, 0, 1080, 100))
        self.mean_diameter_label.setStyleSheet("background-color: #000000")

        # filamentals button
        self.filamentals = QPushButton("FilaMentals", self)
        self.filamentals.setStyleSheet("background-color: #1a9ca8")
        self.filamentals.setGeometry(10, 10, 260, 25)
        self.filamentals.setFont(QtGui.QFont("Ariel", 10))
        self.filamentals.clicked.connect(self.filamentalsMethod)

        # start button
        self.startbutton = QPushButton("Stop", self)
        self.startbutton.setStyleSheet("background-color: #1a9ca8")
        self.startbutton.setGeometry(10, 35, 100, 25)
        self.startbutton.setFont(QtGui.QFont("Ariel", 10))
        self.startbutton.clicked.connect(self.startMethod)

        # clear button
        self.clearbutton = QPushButton("Clear", self)
        self.clearbutton.setStyleSheet("background-color: #1a9ca8")
        self.clearbutton.setGeometry(10, 60, 100, 25)
        self.clearbutton.setFont(QtGui.QFont("Ariel", 10))
        self.clearbutton.clicked.connect(self.clearMethod)

        # label saying mean diameter
        self.mean_diameter_label = QLabel("Mean Diameter (mm): ", self)
        self.mean_diameter_label.setGeometry(QtCore.QRect(120, 35, 150, 25))
        self.mean_diameter_label.setFont(QtGui.QFont("Ariel", 10))
        self.mean_diameter_label.setStyleSheet("background-color: #b7afaf")

        # value of the mean diameter
        self.mean_diameter_number_label = QLabel("0", self)
        self.mean_diameter_number_label.setGeometry(QtCore.QRect(120, 60, 150, 25))
        self.mean_diameter_number_label.setStyleSheet("background-color: #b7afaf")
        self.mean_diameter_number_label.setFont(QtGui.QFont("Ariel", 10))

        # label saying diameter
        self.real_diameter_label = QLabel("Set Reference Diameter (in mm):", self)
        self.real_diameter_label.setGeometry(QtCore.QRect(925, 10, 220, 25))
        self.real_diameter_label.setStyleSheet("background-color: #1a9ca8")
        self.real_diameter_label.setFont(QtGui.QFont("Ariel", 10))

        # edit for the real diameter
        self.real_diameter_edit = QLineEdit(self)
        self.real_diameter_edit.setText("1.75")
        self.real_diameter_edit.setValidator(QtGui.QDoubleValidator())
        self.real_diameter_edit.setGeometry(QtCore.QRect(925, 35, 220, 25))
        self.real_diameter_edit.setStyleSheet("background-color: #ffffff")
        self.real_diameter_edit.setFont(QtGui.QFont("Ariel", 10))

        # calibrate button
        self.calibrate_button = QPushButton("Calibrate", self)
        self.calibrate_button.setGeometry(QtCore.QRect(925, 60, 220, 25))
        self.calibrate_button.setStyleSheet("background-color: #1a9ca8")
        self.calibrate_button.setFont(QtGui.QFont("Ariel", 10))
        self.calibrate_button.clicked.connect(self.calibrateMethod)

        #"record" label
        self.recording = QLabel("  O", self)
        self.recording.setGeometry(QtCore.QRect(280, 10, 75, 75))
        self.recording.setStyleSheet("background-color: #1a9ca8;" "color: #FF0000")
        self.recording.setFont(QtGui.QFont("Ariel", 25))

        # label for live diameter readout
        self.current_diameter = QLabel("Live Diameter Readout: 0", self)
        self.current_diameter.setGeometry(QtCore.QRect(355, 10, 560, 75))
        self.current_diameter.setStyleSheet("background-color: #1a9ca8")
        self.current_diameter.setFont(QtGui.QFont("Ariel", 25))

        # graph
        pen = pg.mkPen(color="#1a9ca8")

        # timer
        self.data_line = self.graphWidget.plot(self.x, self.y, pen=pen)
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

        # only for calibration purposes
        self.real_diameter = 0
        self.ratio = 1.75/65 #original ratio


    def filamentalsMethod(self):
        if self.filamentals.isEnabled():
            webbrowser.open_new_tab(
                "https://git.science.uu.nl/ued2022/ued2022/-/tree/main/projects/Filamentals_Ana_Yoldas_Zach"
            )
            print()
            print("Thanks for visiting :D")
            print()

    def startMethod(self):
        """
        method for starting and stopping the acquisition with a button
        """
        if self.startbutton.isEnabled():
            if self.startbutton.text() == "Stop":
                self.startbutton.setText("Start")
                self.timer.stop()
                self.recording.setStyleSheet("background-color: #1a9ca8;" "color: #1a9ca8")
            elif self.startbutton.text() == "Start":
                self.startbutton.setText("Stop")
                self.timer.start()
                self.recording.setStyleSheet("background-color: #1a9ca8;" "color: #FF0000")

    def clearMethod(self):
        """
        method for clearing the graph
        """
        if self.clearbutton.isEnabled():
            self.data_line.clear()
            self.diameter = []
            self.x = list(range(-100, 0))  # 100 time points
            self.y = [0] * 100
            self.file.close()
            self.filename = "../output/data-" + datetime.datetime.now().isoformat() + ".txt"
            self.file = open(self.filename, "w")

    def calibrateMethod(self):
        """
        sets the new real value for the distance and new ratio pixel/mm
        """
        if self.calibrate_button.isEnabled():
            self.real_diameter = float(self.real_diameter_edit.text())
            self.ratio = self.real_diameter / mean(self.diameter)

    def update_value(self):
        """
        update mean distance value
        """

        s = 0
        if len(self.diameter) > 0:
            self.mean_diameter_number_label.setText(
                "%.2f" % (mean(self.diameter) * self.ratio)
            )    

    def update_plot_data(self):
        """
        update data
        """

        ndiameter = main()

        if ndiameter != 0:
            self.diameter.append(ndiameter)

            self.x = self.x[1:]  # Remove the first y element.
            self.x.append(self.x[-1] + 1)
            self.y = self.y[1:]
            self.y.append(ndiameter * self.ratio)

            self.file = open(self.filename, "r")
            if not self.file.read(1):
                self.file = open(self.filename, "w")
                self.file.write(str(ndiameter * self.ratio) + "\n")
            else:
                self.file = open(self.filename, "a")
                self.file.write(str(ndiameter * self.ratio) + "\n")

            self.data_line.setData(self.x, self.y)  # Update the data.

            self.current_diameter.setText("Live Diameter Readout: %.2f" % (ndiameter * self.ratio))
        
        if (len(self.diameter) > 0):
            print("Mean of the diameter in pixels: " + str(mean(self.diameter)))
            print()

        self.update_value()
