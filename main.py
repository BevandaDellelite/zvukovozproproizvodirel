from PyQt5.QtWidgets import QApplication,QFileDialog
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow

from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtCore import QUrl 

class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.player = QMediaPlayer()#обєкт медіаплеєру
        self.ui.pushButton_3.clicked.connect(self.select_music)
        self.ui.pushButton.clicked.connect(self.play_music)
        self.ui.pushButton_2.clicked.connect(self.stop_music)
        self.ui.horizontalSlider.valueChanged.connect(self.select_volume)

    def select_music(self):
        file, _= QFileDialog.getOpenFileName(self, "Select Audi File","","Audio Files(*.mp3 *.wav *)")
        if file:
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(file)))
      
    def stop_music(self):
        self.player.stop()       

    def play_music(self):
        if self.player.state() == QMediaPlayer.PlayingState:
            self.player.pause()
        else:
            self.player.play()

    def select_volume(self,value):
        self.player.setVolume(value)


app = QApplication([])
ex = Widget()
ex.show()
app.exec_()