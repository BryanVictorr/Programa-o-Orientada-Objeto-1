# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_historico.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Tela_Extrato(object):
    def setupUi(self, Extrato):
        Extrato.setObjectName("Extrato")
        Extrato.setEnabled(True)
        Extrato.resize(351, 268)
        Extrato.setStyleSheet("background-color: rgb(0, 70, 112);")
        self.extrato_Edit = QtWidgets.QTextEdit(Extrato)
        self.extrato_Edit.setEnabled(True)
        self.extrato_Edit.setGeometry(QtCore.QRect(40, 70, 261, 151))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        self.extrato_Edit.setFont(font)
        self.extrato_Edit.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.extrato_Edit.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.extrato_Edit.setObjectName("extrato_Edit")
        self.label = QtWidgets.QLabel(Extrato)
        self.label.setGeometry(QtCore.QRect(130, 30, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.voltar_Button = QtWidgets.QPushButton(Extrato)
        self.voltar_Button.setEnabled(True)
        self.voltar_Button.setGeometry(QtCore.QRect(130, 230, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        self.voltar_Button.setFont(font)
        self.voltar_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.voltar_Button.setStyleSheet("QPushButton{\n"
"\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:10px\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.voltar_Button.setObjectName("voltar_Button")

        self.retranslateUi(Extrato)
        QtCore.QMetaObject.connectSlotsByName(Extrato)

    def retranslateUi(self, Extrato):
        _translate = QtCore.QCoreApplication.translate
        Extrato.setWindowTitle(_translate("Extrato", "Form"))
        self.extrato_Edit.setHtml(_translate("Extrato", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Berlin Sans FB\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label.setText(_translate("Extrato", "Extrato"))
        self.voltar_Button.setText(_translate("Extrato", "Voltar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Extrato = QtWidgets.QWidget()
    ui = Ui_Tela_Extrato()
    ui.setupUi(Extrato)
    Extrato.show()
    sys.exit(app.exec_())

