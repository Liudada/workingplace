import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QFileDialog, QApplication
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		self.textEdit = QTextEdit()
		self.setCentralWidget(self.textEdit)
		self.statusBar()
		openFile = QAction(QIcon('../firstprogram/data/Eva_46.png'), 'Open', self)
		openFile.setShortcut('Ctrl+O')
		openFile.setStatusTip('Open new File')
		openFile.triggered.connect(self.showDialog)
		menubar = self.menuBar()
		menubar.setNativeMenuBar(False)
		fileMenu = menubar.addMenu('&File')
		fileMenu.addAction(openFile)
		self.setGeometry(300, 300, 350, 300)
		self.setWindowTitle('File dialog')
		self.show()
	def showDialog(self):
		fname = QFileDialog.getOpenFileName(self, 'Open file', './')
		with open(fname[0], 'r') as f:
			data = f.read()
			self.textEdit.setText(data)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())