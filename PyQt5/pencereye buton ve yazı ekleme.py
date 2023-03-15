import sys
from PyQt5 import QtWidgets

def Pencere():
    app = QtWidgets.QApplication(sys.argv) #app ı oluşturduk
    pencere = QtWidgets.QWidget()#pencereyi oluşturduk
    pencere.setWindowTitle("Pencereye Buton ve Yazı ekleme") #pencerenin ana başlığı
    
    
    buton = QtWidgets.QPushButton(pencere) #buton oluşturur
    buton.setText("Burası bir butondur") #butona yazı ekler
    
    etiket = QtWidgets.QLabel(pencere) # pencereye yazı alanı oluşturur
    etiket.setText("Merhaba dünya") # pencereye yazı yazmamızı sağlar
    
    etiket.move(200, 50) #etiketi taşır
    buton.move(190, 80) #butonu taşır
    pencere.setGeometry(100, 100, 500, 500) #pencerenin ilk açılış yerini ayarlar
    pencere.show()#pencereyi göster
    
    sys.exit(app.exec_())
Pencere()