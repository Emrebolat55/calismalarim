import sys

from PyQt5.QtWidgets import QWidget,QApplication,QRadioButton,QLabel,QPushButton,QVBoxLayout

class Pencere(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.init__ui()
        
    def init__ui(self):
        
        self.radio_yazısıs = QLabel("Hangi Dili Daha Çok seviyorsun")
        self.java = QRadioButton("Java")
        self.python = QRadioButton("Python")
        self.php = QRadioButton("Php")
        
        self.yazı_alanı = QLabel("")
        
        self.buton = QPushButton("Gönder")
        
        v_box = QVBoxLayout()
        
        v_box.addWidget(self.radio_yazısıs)
        v_box.addWidget(self.java)
        v_box.addWidget(self.python)
        v_box.addWidget(self.php)
        v_box.addStretch()
        v_box.addWidget(self.yazı_alanı)
        v_box.addWidget(self.buton)
        
        self.setLayout(v_box)
        
        self.buton.clicked.connect(lambda :self.click(self.python.isChecked(),self.java.isChecked(),self.php.isChecked(),self.yazı_alanı))
        
        self.setWindowTitle("Radio Button")
        
        self.show()
    def click(self,python,java,php,yazı_alanı):
        if python:
            yazı_alanı.setText("Python")
        if php:
            yazı_alanı.setText("Php")    
        if java:
            yazı_alanı.setText("Java")
            
app =QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())