from PyQt5.QtWidgets import (QApplication, QPushButton,
                             QHBoxLayout, QVBoxLayout,
                             QWidget, QFileDialog)
import sys
import re
from Pillow import *

class GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.pillow = Picture()
        self.pic_path = ''
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 250)
        self.setWindowTitle('Picture Processing')

        selectButton = QPushButton('Select Picture')
        turnButton = QPushButton('Turn')

        selectButton.clicked.connect(self.get_file)
        turnButton.clicked.connect(lambda :self.pillow.drew(self.pic_path, 200, 100))

        hbox = QHBoxLayout()
        hbox.addWidget(selectButton)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addStretch(1)
        vbox.addWidget(turnButton)
        self.setLayout(vbox)

        self.show()

    def get_file(self):
        url = QFileDialog.getOpenFileUrl(self, '选择图片', '', 'Images (*.png *.jpg *.jpeg)')

        #url = "PyQt5.QtCore.QUrl('file:///C:/Users/老旭/Pictures/JOJO.PNG')"
        print(type(str(url[0])))
        print(url[0])
        result = re.search(r"(?<=PyQt5.QtCore.QUrl\('file:///)[\S]*[^')]", str(url[0])).group(0)
        print(result)
        self.pic_path = result
        return result

if __name__ == '__main__':

    app = QApplication(sys.argv)
    g = GUI()
    #print(g.get_file())
    #print(type(g.get_file()))
    sys.exit(app.exec_())

