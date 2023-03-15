import sys

from PyQt5.QtWidgets import QApplication,QAction,qApp,QMainWindow


class Menu(QMainWindow):

    def __init__(self):

        super().__init__()

        menubar = self.menuBar()

        dosya = menubar.addMenu("Dosya")
        duzenle = menubar.addMenu("Düzenle")

        dosya_ac = QAction("Dosya Aç",self)

        dosya_ac.setShortcut("Ctrl+O")

        dosya_kaydet = QAction("Dosya Kaydet",self)
        dosya_kaydet.setShortcut("Ctrl+S")
        cikis = QAction("Çıkış", self)
        cikis.setShortcut("Ctrl+Q")

        dosya.addAction(dosya_ac) # eklememmizi sağalr
        dosya.addAction(dosya_kaydet) # eklememizi sağlar
        dosya.addAction(cikis) # eklememizi sağlar


        ara_ve_degistir = duzenle.addMenu("Ara ve Değiştir") #düzenlenin altın amenü oluşturur

        ara = QAction("Ara",self)

        degistir = QAction("Değiştir",self)

        temizle = QAction("Temizle",self)

        ara_ve_degistir.addAction(ara) #ekler

        ara_ve_degistir.addAction(degistir) #ekler
        duzenle.addAction(temizle) # eklemeyi sağlar



        cikis.triggered.connect(self.cikis_yap) #özellik eklemek için eklenir

        dosya.triggered.connect(self.response) # dosyada herhangi bir işlem yapıldığında

        self.setWindowTitle("Menüler")

        self.show()

    def cikis_yap(self):
        qApp.quit()
    def response(self,action):

        if action.text() == "Dosya Aç":
            print("Dosya Aç'a basıldı.")
        elif action.text() == "Dosya Kaydet":
            print("Dosya Kaydet'e basıldı.")
        elif action.text() == "Çıkış":
            print("Çıkış'a basıldı.")



app = QApplication(sys.argv)

menu = Menu()


sys.exit(app.exec_())
