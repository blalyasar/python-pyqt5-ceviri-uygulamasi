"""BİLAL YAŞAR"""
""" 27/09/2019"""
from textblob import TextBlob
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):

        form = QFormLayout()

        self.giris1 = QLineEdit()
        self.giris2 = QLineEdit()

        ceviriyap = QPushButton("Çeviriyi Yap:")

        self.yazi1 = QLabel("İngilizce Metin Giriniz: ")
        self.yazi1.setFont(QFont("Helvetica",15,QFont.Bold))

        self.yazi2 = QLabel("Türkçe Metin Giriniz: ")
        self.yazi2.setFont(QFont("Robota",15,QFont.Bold))


        self.r1 = QRadioButton("ENGLİSH-TURKCE")
        self.r2 = QRadioButton("TÜRKÇE-ENGLİSH")

        self.r1.setChecked(True)

        self.sonuc = QLabel("CEVİRİ")
        self.sonuc.setAlignment(Qt.AlignCenter)

        
        form.addRow(self.yazi1,self.giris1)
        form.addRow(self.yazi2,self.giris2)
        
        h_box3 = QHBoxLayout()

        h_box3.addWidget(self.r1)
        h_box3.addWidget(self.r2)


        form.addRow(h_box3)
        form.addRow(self.sonuc)
        form.addRow(ceviriyap)

        ceviriyap.clicked.connect(self.cevirifonk)
        
        self.setLayout(form)

        self.setWindowTitle("İngilizce-Türkçe Çeviri Uygulaması")
        self.show()

    def cevirifonk(self):
        if self.r1.isChecked():
            

            cümle1 = self.giris1.text()
            text1 = TextBlob(cümle1)
            cevir1 = text1.translate(to="tr")
            print(cevir1)
            cevir1 = str(cevir1)
            self.sonuc.setText(cevir1)

        elif self.r2.isChecked():
            
            cümle2 = self.giris2.text()
            text2 = TextBlob(cümle2)  
            cevir2 = text2.translate(from_lang="tr", to="en")
            print(cevir2)
            cevir2 = str(cevir2)
            self.sonuc.setText(cevir2)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = Pencere()
    sys.exit(app.exec())
