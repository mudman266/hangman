# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\school\hangman\main_screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(477, 479)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnGuess = QtWidgets.QPushButton(self.centralwidget)
        self.btnGuess.setGeometry(QtCore.QRect(170, 210, 101, 61))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btnGuess.setFont(font)
        self.btnGuess.setStyleSheet("QPushButton {\n"
"color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"background: qradialgradient(cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,radius: 1.35, stop: 0 #fff, stop: 1 #888);\n"
"padding: 5px;\n"
"}")
        self.btnGuess.setObjectName("btnGuess")
        self.linInput = QtWidgets.QLineEdit(self.centralwidget)
        self.linInput.setGeometry(QtCore.QRect(170, 180, 113, 20))
        self.linInput.setObjectName("linInput")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 150, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineBase = QtWidgets.QFrame(self.centralwidget)
        self.lineBase.setGeometry(QtCore.QRect(170, 130, 81, 20))
        self.lineBase.setAutoFillBackground(True)
        self.lineBase.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lineBase.setLineWidth(3)
        self.lineBase.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineBase.setObjectName("lineBase")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(200, 40, 16, 101))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(210, 30, 31, 16))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(230, 40, 16, 16))
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(3)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setObjectName("line_3")
        self.btnHead = QtWidgets.QPushButton(self.centralwidget)
        self.btnHead.setGeometry(QtCore.QRect(230, 50, 21, 21))
        self.btnHead.setStyleSheet("QPushButton {\n"
"color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 10px;\n"
"border-style: outset;\n"
"background: qradialgradient(cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
");\n"
"padding: 5px;\n"
"}")
        self.btnHead.setText("")
        self.btnHead.setFlat(True)
        self.btnHead.setObjectName("btnHead")
        self.lblLettersGuessedTitle = QtWidgets.QLabel(self.centralwidget)
        self.lblLettersGuessedTitle.setGeometry(QtCore.QRect(150, 280, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(12)
        self.lblLettersGuessedTitle.setFont(font)
        self.lblLettersGuessedTitle.setObjectName("lblLettersGuessedTitle")
        self.lblLetters = QtWidgets.QLabel(self.centralwidget)
        self.lblLetters.setGeometry(QtCore.QRect(70, 310, 321, 21))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblLetters.setFont(font)
        self.lblLetters.setText("")
        self.lblLetters.setAlignment(QtCore.Qt.AlignCenter)
        self.lblLetters.setObjectName("lblLetters")
        self.lblLettersGuessedTitle_2 = QtWidgets.QLabel(self.centralwidget)
        self.lblLettersGuessedTitle_2.setGeometry(QtCore.QRect(20, 380, 441, 61))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblLettersGuessedTitle_2.setFont(font)
        self.lblLettersGuessedTitle_2.setText("")
        self.lblLettersGuessedTitle_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lblLettersGuessedTitle_2.setObjectName("lblLettersGuessedTitle_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 477, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnGuess.setText(_translate("MainWindow", "Guess"))
        self.label.setText(_translate("MainWindow", "Enter A Letter"))
        self.lblLettersGuessedTitle.setText(_translate("MainWindow", "Letters Guessed"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
