import sys

from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QLabel,QPushButton,QVBoxLayout

class Pencere(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.init__ui()
        
    def init__ui(self):
        
        self.yazı_alanı = QTextEdit()
        
        self.temizle = QPushButton("Temizle")
        
        v_box = QVBoxLayout()
        
        v_box.addWidget(self.yazı_alanı)
        v_box.addWidget(self.temizle)
        
        self.setWindowTitle("Yazı Alanı")
        self.setLayout(v_box)
        self.temizle.clicked.connect(self.click)
        self.show()
    
    def click(self):
        self.yazı_alanı.clear()#metin kutusunu temizlemek için
        
app = QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())