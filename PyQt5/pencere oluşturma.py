import sys
from PyQt5 import QtWidgets

def Pencere():
    app = QtWidgets.QApplication(sys.argv)
    
    pencere = QtWidgets.QWidget() # pencereyi oluşturur. 
    
    pencere.setWindowTitle("PyQt dersi 1") #pencerenin başlığı 
    etiket1 = QtWidgets.QLabel(pencere)
    pencere.show() #pencereyi gösterir
    
    sys.exit(app.exec_())  # pencerenin çıktısını verir
    
Pencere()