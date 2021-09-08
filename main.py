from PyQt5 import QtWidgets
from PyQt5.QtGui import QImage, QPalette, QPixmap
from reader import Reader
import sys
from PyQt5.QtWidgets import QComboBox, QDialogButtonBox, QFormLayout, QGroupBox, QLineEdit, QMainWindow, QApplication, QPushButton, QScrollArea, QSizePolicy, QSpinBox, QWidget, QAction, QTabWidget, QVBoxLayout, QLabel

# Creating the main window

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'OHLC'
        self.left = 0
        self.top = 0
        self.width = 600
        self.height = 600
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # self.graphWidget = pg.PlotWidget()
        # self.setCentralWidget(self.graphWidget)
        # hour = [1,2,3,4,5,6,7,8,9,10]
        # temperature = [30,32,34,32,33,31,29,32,35,45]
        # self.graphWidget.plot(hour, temperature)

        self.tab_widget = MyTabWidget(self)
        self.setCentralWidget(self.tab_widget)

        self.showMaximized()


# Creating tab widgets
class MyTabWidget(QWidget):

	def getBySymbol(self):
		reader = Reader()
		reader.showChartsBySymbol(self.tab1.nameLineEdit.text())
		self.tab1.pixmap = QPixmap('chart.png')
		self.tab1.label.setPixmap(self.tab1.pixmap)
		self.tab1.label.resize(self.tab1.pixmap.width(),
                          self.tab1.pixmap.height())

	def getByDate(self):
		reader = Reader()
		reader.showChartByDates(self.tab2.nameLineEdit.text(),self.tab2.dateStartLineEdit.text(),self.tab2.dateEndLineEdit.text())
		self.tab2.label.setGeometry(200, 200)
		self.tab2.pixmap = QPixmap('chart.png')
		self.tab2.label.setPixmap(self.tab2.pixmap)
		self.tab2.label.resize(self.tab2.pixmap.width(),
                          self.tab2.pixmap.height())

	def __init__(self, parent):

		super(QWidget, self).__init__(parent)
		self.layout = QVBoxLayout(self)

        # Initialize tab screen
		self.tabs = QTabWidget()
		self.tab1 = QWidget()
		self.tab2 = QWidget()
		self.tab3 = QWidget()
		self.tabs.resize(300, 200)

        # Add tabs
		self.tabs.addTab(self.tab1, "Page 1")
		self.tabs.addTab(self.tab2, "Page 2")
		self.tabs.addTab(self.tab3, "Page 3")

		# self.tab1.layout = QVBoxLayout(self)
		# self.tab1.l = QLineEdit()
		# self.tab1.layout.addWidget(self.tab1.l)
		# self.tab1.setLayout(self.tab1.layout)

		self.tab1.formGroupBox = QGroupBox("Form 1")


		self.tab1.ageSpinBar = QSpinBox()
		self.tab1.degreeComboBox = QComboBox()
		self.tab1.degreeComboBox.addItems(["BTech", "MTech", "PhD"])
		self.tab1.nameLineEdit = QLineEdit()
		layout = QFormLayout()



		layout.addRow(QLabel("Symbol"), self.tab1.nameLineEdit)
		self.tab1.formGroupBox.setLayout(layout)

		self.tab1.buttonBox = QDialogButtonBox(
            QDialogButtonBox.Ok)

		self.tab1.label = QLabel(self.tab1)
		

		self.tab1.buttonBox.accepted.connect(self.getBySymbol)

		mainLayout = QVBoxLayout()
		mainLayout.addWidget(self.tab1.formGroupBox)
		mainLayout.addWidget(self.tab1.buttonBox)
		self.tab1.setLayout(mainLayout)


		# --------------TAB2----------------


		self.tab2.formGroupBox = QGroupBox("Form 1")


		self.tab2.ageSpinBar = QSpinBox()
		self.tab2.degreeComboBox = QComboBox()
		self.tab2.degreeComboBox.addItems(["BTech", "MTech", "PhD"])
		self.tab2.nameLineEdit = QLineEdit()
		self.tab2.dateStartLineEdit = QLineEdit()
		self.tab2.dateEndLineEdit = QLineEdit()
		layout = QFormLayout()



		layout.addRow(QLabel("Symbol"), self.tab2.nameLineEdit)
		layout.addRow(QLabel("Start Date"), self.tab2.dateStartLineEdit)
		layout.addRow(QLabel("End Date"), self.tab2.dateEndLineEdit)
		self.tab2.label = QLabel(self.tab2)
		self.tab2.formGroupBox.setLayout(layout)

		self.tab2.buttonBox = QDialogButtonBox(
            QDialogButtonBox.Ok)

		

		self.tab2.buttonBox.accepted.connect(self.getByDate)

		mainLayout = QVBoxLayout()
		mainLayout.addWidget(self.tab2.formGroupBox)
		mainLayout.addWidget(self.tab2.buttonBox)
		self.tab2.setLayout(mainLayout)


        # Add tabs to widget
		self.layout.addWidget(self.tabs)
		self.setLayout(self.layout)

	


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

