# coding=gbk
from PyQt5.QtWidgets import (QApplication, QPushButton,
                             QHBoxLayout, QVBoxLayout,
                             QWidget, QFileDialog,
                             QLineEdit, QLabel,
                             QMessageBox)
import sys
import re
from Pillow import *

class GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.pillow = Picture()
        self.pic_path = ''
        self.width = None
        self.height = None
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 250)
        self.setWindowTitle('Picture Processing')

        selectButton = QPushButton('Select Picture')
        turnButton = QPushButton('Turn')
        introductionButton = QPushButton('Introduction')
        #introductionButton.resize(100, 20)

        selectButton.clicked.connect(self.get_file)
        turnButton.clicked.connect(lambda :self.get_message())
        introductionButton.clicked.connect(self.show_message)

        lb = QLabel('Picture\'s Path:')
        self.le = QLineEdit()
        lb2 = QLabel('Character Picture width:')
        self.le2 = QLineEdit()
        lb3 = QLabel('Character Picture height:')
        self.le3 = QLineEdit()

        hbox = QHBoxLayout()
        hbox.addWidget(lb)
        hbox.addWidget(self.le)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(lb2)
        hbox2.addWidget(self.le2)

        hbox3 = QHBoxLayout()
        hbox3.addWidget(lb3)
        hbox3.addWidget(self.le3)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addWidget(selectButton)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)

        vbox.addStretch(1)
        vbox.addWidget(introductionButton)
        vbox.addWidget(turnButton)
        self.setLayout(vbox)

        self.show()

    def get_file(self):
        url = QFileDialog.getOpenFileUrl(self, '选择图片', '', 'Images (*.png *.jpg *.jpeg)')

        print(type(str(url[0])))
        print(url[0])
        result = re.search(r"(?<=PyQt5.QtCore.QUrl\('file:///)[\S]*[^')]", str(url[0])).group(0)
        print(result)
        self.le.setText(str(result))
        self.pic_path = result
        return result

    def get_message(self):
        pic_path = self.pic_path
        pic_width = int(self.le2.text())
        pic_height = int(self.le3.text())

        if pic_width == '' or pic_height == '':
            #defualt
            pic_width = 200
            pic_height = 100

        self.pillow.drew(pic_path, pic_width, pic_height)

    def show_message(self):
        QMessageBox.about(self, 'Introduction', 'This tiny program is coded by Python that '
                                                'can convert normal picture to character picture.\n'
                                                'To ensure the character picture quality, '
                                                'please choose the picture that as simple as possible.\n'
                                                'The landscape picture may a bad style for character picture.\n'
                                                'The default size of character picture is (width:200 height:100),'
                                                'you can input your own size for it.')
'''
if __name__ == '__main__':
    app = QApplication(sys.argv)
    g = GUI()
    sys.exit(app.exec_())
'''
app = QApplication(sys.argv)
g = GUI()
sys.exit(app.exec_())