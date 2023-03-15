import sys
from PyQt5 import QtWidgets,QtGui

def Pencere():
    app = QtWidgets.QApplication(sys.argv)
    
    pencere = QtWidgets.QWidget() # pencereyi oluşturur. 
    
    pencere.setWindowTitle("PyQt dersi 1") #pencerenin başlığı 
    etiket1 = QtWidgets.QLabel(pencere)
    
    etiket1.setText("PYTHON DEVELOPER") #yazı eklemeye yarar
    etiket1.move(200, 30) # yazıyı pencerede taşımayı sağlar
    
    etiket2 = QtWidgets.QLabel(pencere)
    etiket2.setPixmap(QtGui.QPixmap("python.png"))# RESİM OLUŞTURMAK İÇİN  
    etiket2.move(140, 50) # resmi pencerede yerini ayarlar
    pencere.setGeometry(200, 200, 500, 500)  
    pencere.show() #pencereyi gösterir
    
    sys.exit(app.exec_())  # pencerenin çıktısını verir
    
Pencere()