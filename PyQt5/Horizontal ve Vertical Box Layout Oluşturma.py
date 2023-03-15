import sys
from PyQt5 import QtWidgets

def Pencere():
    
    app = QtWidgets.QApplication(sys.argv)
    okay = QtWidgets.QPushButton("Tamam")
    cancel = QtWidgets.QPushButton("İptal")
    
    h_box = QtWidgets.QHBoxLayout()
    
    h_box.addStretch() # burda kullanırsak sağa yaslı olur
    h_box.addWidget(okay)
    # h_box.addStretch() # buraya koyduğumuzda ortası boş kalır
    h_box.addWidget(cancel)
    #h_box.addStretch() #butonları sola yaslar
    
    # horizontal ile verticalın birleşimi
    v_box = QtWidgets.QVBoxLayout()
    v_box.addStretch()
    v_box.addLayout(h_box)
    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("Horizon ve Vertical Box")
    
    pencere.setLayout(v_box) 
    
    
    pencere.setGeometry(100, 100, 500, 500)
    
    pencere.show()
    
    sys.exit(app.exec_())
Pencere()