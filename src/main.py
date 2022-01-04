import json
from os import read
from PyQt5 import QtWidgets
from PyQt5.QtGui import QImage, QPalette, QPixmap
import mplfinance as mpf
from reader import Reader
import sys
from PyQt5.QtWidgets import QComboBox, QDialogButtonBox, QFormLayout, QGroupBox, QLineEdit, QMainWindow, QApplication, QPushButton, QScrollArea, QSizePolicy, QSpinBox, QWidget, QAction, QTabWidget, QVBoxLayout, QLabel
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import pandas as pd

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

        self.tab_widget = MyTabWidget(self)
        self.setCentralWidget(self.tab_widget)

        self.showMaximized()

class MyTabWidget(QWidget):

	def getInfo(self):
		reader = Reader()
		self.tab3.label.setVisible(True)
		r = reader.getCompanyInfo(self.tab3.nameLineEdit.text())
		r = json.loads(r)
		df = pd.json_normalize(r)
		self.tab3.label.setText(df.iloc[0,:].to_string())

	def getBySymbol(self):
		reader = Reader()
		df = reader.showChartsBySymbol(self.tab1.nameLineEdit.text())
		self.tab1.tabs.setVisible(True)
		self.tab1.tab1 = QWidget()
		self.tab1.tab2 = QWidget()
		self.tab1.tab3 = QWidget()
		self.tab1.tab4 = QWidget()
		self.tab1.tab5 = QWidget()
		self.tab1.tabs.resize(300, 200)

        # Add tabs
		self.tab1.tabs.addTab(self.tab1.tab1, "OHLC")
		self.tab1.tabs.addTab(self.tab1.tab2, "BAR GRAPH")
		self.tab1.tabs.addTab(self.tab1.tab3, "COLORED BAR GRAPH")
		self.tab1.tabs.addTab(self.tab1.tab4, "CANDLE STICKS")
		self.tab1.tabs.addTab(self.tab1.tab5, "VERTEX LINE")

		fig,_ = mpf.plot(df,title=f'{self.tab1.nameLineEdit.text()}',returnfig = True)
		canavas = FigureCanvasQTAgg(fig)

		mainLayout = QVBoxLayout()
		mainLayout.addWidget(canavas)
		self.tab1.tab1.setLayout(mainLayout)

		fig,_ = mpf.plot(df,type='candle',volume=True, title=f'{self.tab1.nameLineEdit.text()}',returnfig = True)
		canavas = FigureCanvasQTAgg(fig)

		mainLayout = QVBoxLayout()
		mainLayout.addWidget(canavas)
		self.tab1.tab2.setLayout(mainLayout)

		kwargs = dict(type='candle',volume=True,figratio=(11,8),figscale=0.85)
		fig,_ = mpf.plot(df,**kwargs,style='charles',title=f'{self.tab1.nameLineEdit.text()}',returnfig = True)
		canavas = FigureCanvasQTAgg(fig)

		mainLayout = QVBoxLayout()
		mainLayout.addWidget(canavas)
		self.tab1.tab3.setLayout(mainLayout)

		fig,_ = mpf.plot(df,**kwargs,style='classic',title=f'{self.tab1.nameLineEdit.text()}',returnfig = True)
		canavas = FigureCanvasQTAgg(fig)

		mainLayout = QVBoxLayout()
		mainLayout.addWidget(canavas)
		self.tab1.tab4.setLayout(mainLayout)

		fig,_ = mpf.plot(df,mav=(3, 5),title=f'{self.tab1.nameLineEdit.text()}',returnfig = True)
		canavas = FigureCanvasQTAgg(fig)

		mainLayout = QVBoxLayout()
		mainLayout.addWidget(canavas)
		self.tab1.tab5.setLayout(mainLayout)

	def getByDate(self):
		reader = Reader()
		df = reader.showChartByDates(self.tab2.nameLineEdit.text(),self.tab2.dateStartLineEdit.text(),self.tab2.dateEndLineEdit.text())
		self.tab2.tabs.setVisible(True)
		self.tab2.tab1 = QWidget()
		self.tab2.tab2 = QWidget()
		self.tab2.tab3 = QWidget()
		self.tab2.tab4 = QWidget()
		self.tab2.tab5 = QWidget()
		self.tab2.tabs.resize(300, 200)

        # Add tabs
		self.tab2.tabs.addTab(self.tab2.tab1, "OHLC")
		self.tab2.tabs.addTab(self.tab2.tab2, "BAR GRAPH")
		self.tab2.tabs.addTab(self.tab2.tab3, "COLORED BAR GRAPH")
		self.tab2.tabs.addTab(self.tab2.tab4, "CANDLE STICKS")
		self.tab2.tabs.addTab(self.tab2.tab5, "VERTEX LINE")

		fig,_ = mpf.plot(df,title=f'{self.tab2.nameLineEdit.text()}',returnfig = True)
		canavas = FigureCanvasQTAgg(fig)

		mainLayout = QVBoxLayout()
		mainLayout.addWidget(canavas)
		self.tab2.tab1.setLayout(mainLayout)

		fig,_ = mpf.plot(df,type='candle',volume=True, title=f'{self.tab2.nameLineEdit.text()}',returnfig = True)
		canavas = FigureCanvasQTAgg(fig)

		mainLayout = QVBoxLayout()
		mainLayout.addWidget(canavas)
		self.tab2.tab2.setLayout(mainLayout)

		kwargs = dict(type='candle',volume=True,figratio=(11,8),figscale=0.85)
		fig,_ = mpf.plot(df,**kwargs,style='charles',title=f'{self.tab2.nameLineEdit.text()}',returnfig = True)
		canavas = FigureCanvasQTAgg(fig)

		mainLayout = QVBoxLayout()
		mainLayout.addWidget(canavas)
		self.tab2.tab3.setLayout(mainLayout)

		fig,_ = mpf.plot(df,**kwargs,style='classic',title=f'{self.tab2.nameLineEdit.text()}',returnfig = True)
		canavas = FigureCanvasQTAgg(fig)

		mainLayout = QVBoxLayout()
		mainLayout.addWidget(canavas)
		self.tab2.tab4.setLayout(mainLayout)

		fig,_ = mpf.plot(df,mav=(3, 5),title=f'{self.tab2.nameLineEdit.text()}',returnfig = True)
		canavas = FigureCanvasQTAgg(fig)

		mainLayout = QVBoxLayout()
		mainLayout.addWidget(canavas)
		self.tab2.tab5.setLayout(mainLayout)

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
		self.tabs.addTab(self.tab1, "View Stock By Symbol")
		self.tabs.addTab(self.tab2, "View Stock based on timeline")
		self.tabs.addTab(self.tab3, "Get Company Details")

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
		self.tab1.label = QLabel(self.tab1)
		self.tab1.formGroupBox.setLayout(layout)

		self.tab1.buttonBox = QDialogButtonBox(
            QDialogButtonBox.Ok)

		
		

		self.tab1.buttonBox.accepted.connect(self.getBySymbol)

		self.tab1.tabs = QTabWidget()
		self.tab1.tabs.setVisible(False)

		mainLayout = QVBoxLayout()
		mainLayout.addWidget(self.tab1.formGroupBox)
		mainLayout.addWidget(self.tab1.buttonBox)
		mainLayout.addWidget(self.tab1.tabs)
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

		self.tab2.tabs = QTabWidget()
		self.tab2.tabs.setVisible(False)

		mainLayout = QVBoxLayout()
		mainLayout.addWidget(self.tab2.formGroupBox)
		mainLayout.addWidget(self.tab2.buttonBox)
		mainLayout.addWidget(self.tab2.tabs)

		self.tab2.setLayout(mainLayout)

		#Tab3------------


		self.tab3.formGroupBox = QGroupBox("Form 1")

		self.tab3.nameLineEdit = QLineEdit()
		layout = QFormLayout()

		layout.addRow(QLabel("Symbol"), self.tab3.nameLineEdit)
		self.tab3.label = QLabel(self.tab3)
		self.tab3.formGroupBox.setLayout(layout)

		self.tab3.buttonBox = QDialogButtonBox(
            QDialogButtonBox.Ok)

		self.tab3.buttonBox.accepted.connect(self.getInfo)

		mainLayout = QVBoxLayout()
		self.tab3.label = QLabel()
		self.tab3.label.setText("AAA")
		self.tab3.label.setVisible(False)
		mainLayout.addWidget(self.tab3.formGroupBox)
		mainLayout.addWidget(self.tab3.buttonBox)
		mainLayout.addWidget(self.tab3.label)

		self.tab3.setLayout(mainLayout)


        # Add tabs to widget
		self.layout.addWidget(self.tabs)
		self.setLayout(self.layout)

	


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


