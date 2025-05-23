import yt_dlp # Biblioteca para download de video/audios do Youtube
import os #Biblioteca padrão para interação com o sistema operacional
from PyQt5 import QtCore, QtGui, QtWidgets # Componentes da interface gráfica com PyQt5


# Configuração da Janela Principal
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(697, 572)
        MainWindow.setStyleSheet("background-color: #1e1e1e;\n"
"color: #ffffff;\n"
"font-family: Segoe UI, sans-serif;\n"
"font-size: 14px;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bt_download = QtWidgets.QPushButton(self.centralwidget)
        self.bt_download.setGeometry(QtCore.QRect(290, 290, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.bt_download.setFont(font)
        self.bt_download.setStyleSheet("QPushButton {\n"
"    background-color: #007acc;\n"
"    color: #ffffff;\n"
"    border-radius: 10px;\n"
"    padding: 8px 16px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0099ff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #005f99;\n"
"}\n"
"")
        self.bt_download.setObjectName("bt_download")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 210, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
"    color: #f2f2f2;\n"
"    font-weight: bold;\n"
"    font-size: 16px;\n"
"}")
        self.label.setObjectName("label")
        self.txt_link = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_link.setGeometry(QtCore.QRect(40, 240, 391, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        self.txt_link.setFont(font)
        self.txt_link.setStyleSheet("QLineEdit {\n"
"    background-color: #2a2a2a;\n"
"    border: 2px solid #444;\n"
"    border-radius: 8px;\n"
"    padding: 6px;\n"
"    color: #ffffff;\n"
"}\n"
"")
        self.txt_link.setText("")
        self.txt_link.setObjectName("txt_link")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(440, 140, 241, 211))
        self.label_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_3.setObjectName("label_3")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 280, 61, 54))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        self.layoutWidget.setFont(font)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.rb_mp3 = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.rb_mp3.setFont(font)
        self.rb_mp3.setStyleSheet("QRadioButton {\n"
"    spacing: 6px;\n"
"    color: #ffffff;\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    border-radius: 7px;\n"
"    border: 2px solid #888;\n"
"    background-color: #1e1e1e;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #007acc;\n"
"    border: 2px solid #007acc;\n"
"}")
        self.rb_mp3.setObjectName("rb_mp3")
        self.verticalLayout.addWidget(self.rb_mp3)
        self.rb_mp4 = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.rb_mp4.setFont(font)
        self.rb_mp4.setStyleSheet("QRadioButton {\n"
"    spacing: 6px;\n"
"    color: #ffffff;\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    border-radius: 7px;\n"
"    border: 2px solid #888;\n"
"    background-color: #1e1e1e;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #007acc;\n"
"    border: 2px solid #007acc;\n"
"}")
        self.rb_mp4.setObjectName("rb_mp4")
        self.verticalLayout.addWidget(self.rb_mp4)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(570, 500, 111, 20))
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setStyleSheet("QLabel {\n"
"    color: #f2f2f2;\n"
"    font-weight: bold;\n"
"    font-size: 10px;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.layoutWidget.raise_()
        self.label_3.raise_()
        self.bt_download.raise_()
        self.label.raise_()
        self.txt_link.raise_()
        self.label_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 697, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        ### Botão Download ###
        self.bt_download.clicked.connect(self.download)   
    
    ### Função de Download ###
    
    def download(self):
        if self.rb_mp4.isChecked() == True:
            url = self.txt_link.text()
            QtWidgets.QMessageBox.information(None, "Sucesso", "Download iniciado!")
            yt_dlp.YoutubeDL(
                {'outtmpl': 'Musicas/%(title)s.%(ext)s',
                 'noplaylist': True,
                 'format': 'mp4',
                 'skip_download': False}).download([url])
            
    ### Download MP3 ####
        elif self.rb_mp3.isChecked() == True:
            url = self.txt_link.text()
            QtWidgets.QMessageBox.information(None, "Sucesso", "Download iniciado!")
            yt_dlp.YoutubeDL(
                {'outtmpl': 'Musicas/%(title)s.%(ext)s',
                 'noplaylist': True,
                 'format': 'm4a',
                 'skip_download': False}).download([url])
        else:
            QtWidgets.QMessageBox.warning(None, "Aviso", "Selecione MP3 ou MP4!")
            return
            
    ### Mensagem de Download concluido ### 
        QtWidgets.QMessageBox.information(None, "Sucesso", "Download concluído com sucesso!")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bt_download.setText(_translate("MainWindow", "Download"))
        self.label.setText(_translate("MainWindow", "Link do Youtube:"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/youtube/youtube-folder-v2.png\"width=\"200\" height=\"200\"/></p></body></html>"))
        self.rb_mp3.setText(_translate("MainWindow", "MP3"))
        self.rb_mp4.setText(_translate("MainWindow", "MP4"))
        self.label_2.setText(_translate("MainWindow", "caiosd0 -  Version 1.0"))
import youtube


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
