from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_JanelaPrincipal(object):
    def setupUi(self, JanelaPrincipal):
        JanelaPrincipal.setObjectName("JanelaPrincipal")
        JanelaPrincipal.resize(427, 395)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        JanelaPrincipal.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(JanelaPrincipal)
        self.centralwidget.setObjectName("centralwidget")
        self.fundo = QtWidgets.QLabel(self.centralwidget)
        self.fundo.setGeometry(QtCore.QRect(-110, -20, 581, 551))
        self.fundo.setText("")
        self.fundo.setPixmap(QtGui.QPixmap("fundo.png"))
        self.fundo.setScaledContents(True)
        self.fundo.setObjectName("fundo")
        self.texto_sobre = QtWidgets.QLabel(self.centralwidget)
        self.texto_sobre.setGeometry(QtCore.QRect(50, 80, 331, 291))
        self.texto_sobre.setStyleSheet("font: 75 9pt \"Sitka Text\";color: rgb(255, 255, 255);")
        self.texto_sobre.setObjectName("texto_sobre")
        self.icone = QtWidgets.QLabel(self.centralwidget)
        self.icone.setGeometry(QtCore.QRect(180, 30, 61, 61))
        self.icone.setMinimumSize(QtCore.QSize(31, 0))
        self.icone.setText("")
        self.icone.setPixmap(QtGui.QPixmap("icone.png"))
        self.icone.setScaledContents(True)
        self.icone.setObjectName("icone")
        JanelaPrincipal.setCentralWidget(self.centralwidget)
        JanelaPrincipal.setFixedSize(JanelaPrincipal.width(), JanelaPrincipal.height())

        self.retranslateUi(JanelaPrincipal)
        QtCore.QMetaObject.connectSlotsByName(JanelaPrincipal)

    def retranslateUi(self, JanelaPrincipal):
        _translate = QtCore.QCoreApplication.translate
        JanelaPrincipal.setWindowTitle(_translate("JanelaPrincipal", "Sobre"))
        self.texto_sobre.setText(_translate("JanelaPrincipal", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">Decodificador morse 2021 - Versão 1.0.0</span></p><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">Built on March 05, 2021</span></p><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">Instituto Federal do Rio Grande do Norte</span></p><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">Class: 2.02401.1M</span></p><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">Developers: </span></p><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">André Luís, Cauã Vinícius, João Victor, </span></p><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">Lucas Alexandre, Pablo Lucas, Rafael Araújo</span></p><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">Copyright © 2021-2021</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])

    sobre = QtWidgets.QMainWindow()
    ui = Ui_JanelaPrincipal()
    ui.setupUi(sobre)

    sobre.show()
    sys.exit(app.exec_())