from PyQt5.uic import loadUiType
import sys
from os import path
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import form
import Scanner
import cv2

FORM_CLASS, _ = loadUiType(path.join(path.dirname(__file__), "gui.ui"))
front_addr = ''
back_addr = ''


class MainApp(QMainWindow, FORM_CLASS):

    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        # QMainWindow.__init__(self)
        # self.setupUi(self)
        #
        # self.front_btn.clicked.connect(self.front)
        #
        # self.back_btn.clicked.connect(self.back)
        #
        # self.generate_btn.clicked.connect(self.generate)
        self.front()
    def front(self):
        global front_addr
        # front_addr, _ = QFileDialog.getOpenFileName(self, 'Open File', '', "Image files(*.jpg *.png *.jpeg)")
        Scanner.scan("/home/mohamed/Downloads/Test set-20221116T115249Z-001/Test set/20190504_185334.jpg", "front")
        # print(front_addr)
        # front_addr = str(front_addr)[2:str(front_addr).find(',')-1]
        pixmap = QPixmap("temp_front.jpeg")
        # self.label_imgf.setPixmap(pixmap)
        # self.label_imgf.setScaledContents(True)
        self.back()
    ##

    ##        print ("____",front_addr,"____")

    def back(self):
        global back_addr
        # back_addr, _ = QFileDialog.getOpenFileName(self, 'Open File', '', "Image files(*.jpg *.png *.jpeg)")
        Scanner.scan("/home/mohamed/Downloads/Test set-20221116T115249Z-001/Test set/20190504_205804.jpg", "back")
        # back_addr = str(back_addr)[2:str(back_addr).find(',')-1]
        pixmap = QPixmap("temp_front.jpeg")
        self.generate()
        # self.label_imgb.setPixmap(pixmap)
        # self.label_imgb.setScaledContents(True)

        # print(input_file1)

    ##        print ("____",back_addr,"____")

    def generate(self):
        # global front_addr, back_addr
        # if front_addr == '' or back_addr == '':
        #     QMessageBox.about(self, "Couldn't generate", "Image is not inserted!")
        # else:
            # form.form("temp_front.jpg", "temp_back.jpg")
        form.form("temp_front.jpg", "temp_back.jpg")
        # form.form("temp_front.jpg")
        print("done")


def main():
    # app = QApplication(sys.argv)
    # window = MainApp()
    from ArabicOcr import arabicocr

    image_path = 'temp_front.jpg'
    out_image = 'out.jpg'
    results = arabicocr.arabic_ocr(image_path, out_image)
    print(results)
    words = []
    for i in range(len(results)):
        word = results[i][1]
        words.append(word)
    with open('file.txt', 'w', encoding='utf-8') as myfile:
        myfile.write(str(words))
    import cv2
    img = cv2.imread('out.jpg', cv2.IMREAD_UNCHANGED)
    cv2.imshow("arabic ocr", img)
    cv2.waitKey(0)

    # window.show()
    #
    # sys.exit(app.exec_())



if __name__ == '__main__':
    main()
