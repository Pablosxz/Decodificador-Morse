from PyQt5 import QtCore, QtGui, QtWidgets
from sobre import Ui_JanelaPrincipal

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(703, 436)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.fundo = QtWidgets.QLabel(self.centralwidget)
        self.fundo.setEnabled(True)
        self.fundo.setGeometry(QtCore.QRect(-30, -70, 751, 571))
        self.fundo.setText("")
        self.fundo.setPixmap(QtGui.QPixmap("fundo.png"))
        self.fundo.setScaledContents(True)
        self.fundo.setObjectName("fundo")
        self.caixa_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.caixa_2.setEnabled(False)
        self.caixa_2.setGeometry(QtCore.QRect(380, 130, 291, 151))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.caixa_2.setFont(font)
        self.caixa_2.setStyleSheet("background-color: rgb(140, 140, 140);\n"
"selection-color: rgb(143, 143, 143);\n"
"border-top-color: rgb(0, 255, 0);\n"
"border-color: rgb(0, 170, 0);\n"
"alternate-background-color: rgb(218, 218, 218);\n" "color: rgb(0, 0, 0);\n" "font: bold")
        self.caixa_2.setText("")
        self.caixa_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.caixa_2.setObjectName("caixa_2")
        self.caixa_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.caixa_1.setGeometry(QtCore.QRect(30, 130, 291, 151))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.caixa_1.setFont(font)
        self.caixa_1.setStyleSheet("background-color: rgb(140, 140, 140);\n"
"selection-color: rgb(143, 143, 143);\n"
"border-top-color: rgb(0, 255, 0);\n"
"border-color: rgb(0, 170, 0);\n"
"alternate-background-color: rgb(218, 218, 218);")
        self.caixa_1.setText("")
        self.caixa_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.caixa_1.setObjectName("caixa_1")
        self.texto_morse = QtWidgets.QRadioButton(self.centralwidget)
        self.texto_morse.setGeometry(QtCore.QRect(380, 300, 121, 17))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(9)
        self.texto_morse.setFont(font)
        self.texto_morse.setStyleSheet("color: rgb(255, 255, 255);")
        self.texto_morse.setObjectName("texto_morse")
        self.morse_texto = QtWidgets.QRadioButton(self.centralwidget)
        self.morse_texto.setGeometry(QtCore.QRect(200, 300, 121, 17))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(9)
        self.morse_texto.setFont(font)
        self.morse_texto.setStyleSheet("color: rgb(255, 255, 255);")
        self.morse_texto.setObjectName("morse_texto")

        self.seta = QtWidgets.QLabel(self.centralwidget)
        self.seta.setGeometry(QtCore.QRect(330, 180, 41, 51))
        self.seta.setText("")
        self.seta.setPixmap(QtGui.QPixmap("convert-arrow.png"))
        self.seta.setScaledContents(True)
        self.seta.setObjectName("seta")
        self.titulo = QtWidgets.QLabel(self.centralwidget)
        self.titulo.setGeometry(QtCore.QRect(140, 50, 441, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.titulo.setFont(font)
        self.titulo.setObjectName("titulo")
        self.botao_sobre = QtWidgets.QPushButton(self.centralwidget)
        self.botao_sobre.setGeometry(QtCore.QRect(610, 10, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.botao_sobre.setFont(font)
        self.botao_sobre.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_sobre.setStyleSheet("")
        self.botao_sobre.setObjectName("botao_sobre")
        self.botao_iniciar = QtWidgets.QPushButton(self.centralwidget)
        self.botao_iniciar.setGeometry(QtCore.QRect(330, 180, 41, 51))
        self.botao_iniciar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_iniciar.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.botao_iniciar.setText("")
        self.botao_iniciar.setObjectName("botao_iniciar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.botao_iniciar.clicked.connect(self.traduzir)
        self.botao_sobre.clicked.connect(self.abrir_sobre)
        MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.morse_code = {
            'A': '.-', 'B': '-...',
            'C': '-.-.', 'D': '-..',
            'E': '.', 'F': '..-.',
            'G': '--.', 'H': '....',
            'I': '..', 'J': '.---',
            'K': '-.-', 'L': '.-..',
            'M': '--', 'N': '-.',
            'O': '---', 'P': '.--.',
            'Q': '--.-', 'R': '.-.',
            'S': '...', 'T': '-',
            'U': '..-', 'V': '...-',
            'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..',
            '0': '-----', '1': '.----',
            '2': '..---', '3': '...--',
            '4': '....-', '5': '.....',
            '6': '-....', '7': '--...',
            '8': '---..', '9': '----.'
        }

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Decodificador Morse"))
        self.texto_morse.setText(_translate("MainWindow", "Texto para morse"))
        self.morse_texto.setText(_translate("MainWindow", "Morse para texto"))
        self.titulo.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">Decodificador e Codificador de código Morse</span></p></body></html>"))
        self.botao_sobre.setText(_translate("MainWindow", "Sobre"))

    def traduzir(self):
        if self.morse_texto.isChecked():
            self.decodificar(self.caixa_1.text())
        elif self.texto_morse.isChecked():
            self.codificar()

    def codificar(self):
        codigo_morse = ''
        for letra in self.caixa_1.text().upper():
            if letra in self.morse_code.keys():
                codigo_morse += self.morse_code[letra] + ' '
        self.caixa_2.setText(codigo_morse)

    def decodificar(self, codigo_morse):
        code = codigo_morse.split(' ')
        texto = ''
        for item in code:
            for key, value in self.morse_code.items():
                if item == value:
                    texto += key
                    break
        self.caixa_2.setText(texto.lower())

    def abrir_sobre(self):
        self.janela = QtWidgets.QMainWindow()
        self.sobre = Ui_JanelaPrincipal()
        self.sobre.setupUi(self.janela)
        self.janela.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])
    principal = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(principal)
    principal.show()
    sys.exit(app.exec_())