import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
import pyqtweb

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('MyApp')
        self.setGeometry(100, 100, 200, 100)
        self.label = QLabel('Hello, PyQt5!', self)
        self.label.move(50, 30)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = MyApp()
    myapp.show()
    webapp = pyqtweb.create_app()
    pyqtweb.qapp(app, webapp)
    pyqtweb.run()
