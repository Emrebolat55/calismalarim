import sys

from PyQt5.QtWidgets import QWidget,QApplication,QCheckBox,QLabel,QPushButton,QVBoxLayout


class Pencere(QWidget):
    def __init__(self):

        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.checkbox = QCheckBox("Python'ı seviyor musunuz ?")
        self.yazi_alani = QLabel("")
        self.buton = QPushButton("Bana Tıkla")

        v_box = QVBoxLayout()

        v_box.addWidget(self.checkbox)
        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.buton)

        self.setLayout(v_box)

        self.setWindowTitle("Check Box")
        
        self.buton.clicked.connect(lambda : self.click(self.checkbox.isChecked(),self.yazi_alani)) # fonksiyon objesine dönüştürmek için lambda kullandık
        
        self.show()
        
    def click(self,checkbox,yazı_alanı):
        if checkbox:
            yazı_alanı.setText("Paythonu Seviyorsun")
        else:
            yazı_alanı.setText("Neden sevmiyorsun?")   
            
             
app = QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())