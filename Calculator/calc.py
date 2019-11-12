from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(345, 300)
        MainWindow.setMaximumSize(QtCore.QSize(345, 300))
        MainWindow.setMinimumSize(QtCore.QSize(345, 300))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_0 = QtWidgets.QPushButton(self.centralwidget)
        self.button_0.setGeometry(QtCore.QRect(10, 230, 51, 41))
        self.button_0.setObjectName("button_0")
        self.button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.button_2.setGeometry(QtCore.QRect(70, 180, 51, 41))
        self.button_2.setObjectName("button_2")
        self.button_3 = QtWidgets.QPushButton(self.centralwidget)
        self.button_3.setGeometry(QtCore.QRect(130, 180, 51, 41))
        self.button_3.setObjectName("button_3")
        self.button_1 = QtWidgets.QPushButton(self.centralwidget)
        self.button_1.setGeometry(QtCore.QRect(10, 180, 51, 41))
        self.button_1.setObjectName("button_1")
        self.button_4 = QtWidgets.QPushButton(self.centralwidget)
        self.button_4.setGeometry(QtCore.QRect(10, 130, 51, 41))
        self.button_4.setObjectName("button_4")
        self.button_5 = QtWidgets.QPushButton(self.centralwidget)
        self.button_5.setGeometry(QtCore.QRect(70, 130, 51, 41))
        self.button_5.setObjectName("button_5")
        self.button_8 = QtWidgets.QPushButton(self.centralwidget)
        self.button_8.setGeometry(QtCore.QRect(70, 80, 51, 41))
        self.button_8.setObjectName("button_8")
        self.button_9 = QtWidgets.QPushButton(self.centralwidget)
        self.button_9.setGeometry(QtCore.QRect(130, 80, 51, 41))
        self.button_9.setObjectName("button_9")
        self.button_6 = QtWidgets.QPushButton(self.centralwidget)
        self.button_6.setGeometry(QtCore.QRect(130, 130, 51, 41))
        self.button_6.setObjectName("button_6")
        self.button_7 = QtWidgets.QPushButton(self.centralwidget)
        self.button_7.setGeometry(QtCore.QRect(10, 80, 51, 41))
        self.button_7.setObjectName("button_7")
        self.button_clear = QtWidgets.QPushButton(self.centralwidget)
        self.button_clear.setGeometry(QtCore.QRect(130, 230, 51, 41))
        self.button_clear.setObjectName("button_clear")
        self.button_add = QtWidgets.QPushButton(self.centralwidget)
        self.button_add.setGeometry(QtCore.QRect(220, 170, 51, 41))
        self.button_add.setObjectName("button_add")
        self.button_minus = QtWidgets.QPushButton(self.centralwidget)
        self.button_minus.setGeometry(QtCore.QRect(280, 170, 51, 41))
        self.button_minus.setObjectName("button_minus")
        self.button_multiply = QtWidgets.QPushButton(self.centralwidget)
        self.button_multiply.setGeometry(QtCore.QRect(220, 120, 51, 41))
        self.button_multiply.setObjectName("button_multiply")
        self.button_equal = QtWidgets.QPushButton(self.centralwidget)
        self.button_equal.setGeometry(QtCore.QRect(280, 230, 51, 41))
        self.button_equal.setObjectName("button_equal")
        self.button_divide = QtWidgets.QPushButton(self.centralwidget)
        self.button_divide.setGeometry(QtCore.QRect(280, 120, 51, 41))
        self.button_divide.setObjectName("button_divide")
        self.button_ans = QtWidgets.QPushButton(self.centralwidget)
        self.button_ans.setGeometry(QtCore.QRect(220, 230, 51, 41))
        self.button_ans.setObjectName("button_ans")
        self.button_float = QtWidgets.QPushButton(self.centralwidget)
        self.button_float.setGeometry(QtCore.QRect(70, 230, 51, 41))
        self.button_float.setObjectName("button_float")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 321, 61))
        font = QtGui.QFont()
        font.setFamily("Dotum")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setIndent(5)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 342, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator 2.0"))

        self.button_0.setText(_translate("MainWindow", "0"))
        self.button_0.clicked.connect(partial(self.buttonClick, self.button_0))
        self.button_1.setText(_translate("MainWindow", "1"))
        self.button_1.clicked.connect(partial(self.buttonClick, self.button_1))
        self.button_2.setText(_translate("MainWindow", "2"))
        self.button_2.clicked.connect(partial(self.buttonClick, self.button_2))
        self.button_3.setText(_translate("MainWindow", "3"))
        self.button_3.clicked.connect(partial(self.buttonClick, self.button_3))
        self.button_4.setText(_translate("MainWindow", "4"))
        self.button_4.clicked.connect(partial(self.buttonClick, self.button_4))
        self.button_5.setText(_translate("MainWindow", "5"))
        self.button_5.clicked.connect(partial(self.buttonClick, self.button_5))
        self.button_6.setText(_translate("MainWindow", "6"))
        self.button_6.clicked.connect(partial(self.buttonClick, self.button_6))
        self.button_7.setText(_translate("MainWindow", "7"))
        self.button_7.clicked.connect(partial(self.buttonClick, self.button_7))
        self.button_8.setText(_translate("MainWindow", "8"))
        self.button_8.clicked.connect(partial(self.buttonClick, self.button_8))
        self.button_9.setText(_translate("MainWindow", "9"))
        self.button_9.clicked.connect(partial(self.buttonClick, self.button_9))
        self.button_clear.setText(_translate("MainWindow", "AC"))
        self.button_clear.clicked.connect(partial(self.buttonClick, self.button_clear))
        self.button_add.setText(_translate("MainWindow", "+"))
        self.button_add.clicked.connect(partial(self.buttonClick, self.button_add))
        self.button_minus.setText(_translate("MainWindow", "-"))
        self.button_minus.clicked.connect(partial(self.buttonClick, self.button_minus))
        self.button_multiply.setText(_translate("MainWindow", "*"))
        self.button_multiply.clicked.connect(partial(self.buttonClick, self.button_multiply))
        self.button_divide.setText(_translate("MainWindow", "/"))
        self.button_divide.clicked.connect(partial(self.buttonClick, self.button_divide))
        self.button_float.setText(_translate("MainWindow", "."))
        self.button_float.clicked.connect(partial(self.buttonClick, self.button_float))
        self.button_ans.setText(_translate("MainWindow", "Ans"))
        self.button_ans.clicked.connect(partial(self.buttonClick, self.button_ans))
        self.button_equal.setText(_translate("MainWindow", "="))
        self.button_equal.clicked.connect(partial(self.buttonClick, self.button_equal))
        self.label.setText(_translate("MainWindow", "0"))

    def buttonClick(self, button):
        currentInput = self.label.text()
        if button == self.button_0:
            if currentInput == str(0):
                pass
            else:
                self.label.setText(f"{currentInput}{0}")
        elif button == self.button_1:
            if currentInput == str(0):
                self.label.setText("1")
            else:
                self.label.setText(f"{currentInput}{1}")
        elif button == self.button_2:
            if currentInput == str(0):
                self.label.setText("2")
            else:
                self.label.setText(f"{currentInput}{2}")
        elif button == self.button_3:
            if currentInput == str(0):
                self.label.setText("3")
            else:
                self.label.setText(f"{currentInput}{3}")
        elif button == self.button_4:
            if currentInput == str(0):
                self.label.setText("5")
            else:
                self.label.setText(f"{currentInput}{4}")
        elif button == self.button_5:
            if currentInput == str(0):
                self.label.setText("6")
            else:
                self.label.setText(f"{currentInput}{5}")
        elif button == self.button_6:
            if currentInput == str(0):
                self.label.setText("6")
            else:
                self.label.setText(f"{currentInput}{6}")
        elif button == self.button_7:
            if currentInput == str(0):
                self.label.setText("7")
            else:
                self.label.setText(f"{currentInput}{7}")
        elif button == self.button_8:
            if currentInput == str(0):
                self.label.setText("8")
            else:
                self.label.setText(f"{currentInput}{8}")
        elif button == self.button_9:
            if currentInput == str(0):
                self.label.setText("9")
            else:
                self.label.setText(f"{currentInput}{9}")

        elif button == self.button_clear:
            self.label.setText("0")
        elif button == self.button_add:
            if currentInput == str(0):
                pass
            else:
                self.label.setText(f"{currentInput}{'+'}")
        elif button == self.button_minus:
            if currentInput == str(0):
                pass
            else:
                self.label.setText(f"{currentInput}{'-'}")
        elif button == self.button_multiply:
            if currentInput == str(0):
                pass
            else:
                self.label.setText(f"{currentInput}{'*'}")
        elif button == self.button_divide:
            if currentInput == str(0):
                pass
            else:
                self.label.setText(f"{currentInput}{'/'}")

        elif button == self.button_float:
            signs = ['+', '-', '/', '*']
            if currentInput == str(0):
                pass
            else:
                for sign in signs:
                    if currentInput.find(sign) != -1:
                        nums = currentInput.split(sign)
                        if nums[1].find('.') == -1:
                            self.label.setText(f"{currentInput}{'.'}")
                        else:
                            pass
                    elif currentInput.find('.') == -1:
                        self.label.setText(f"{currentInput}{'.'}")

        elif button == self.button_equal:
            if currentInput == str(0):
                pass
            else:
                if currentInput.find('+') != -1:
                    expression = currentInput.split("+")
                    answer = float(expression[0]) + float(expression[1])
                elif currentInput.find('-') != -1:
                    expression = currentInput.split("-")
                    answer = float(expression[0]) - float(expression[1])
                elif currentInput.find('*') != -1:
                    expression = currentInput.split("*")
                    answer = float(expression[0]) * float(expression[1])
                elif currentInput.find('/') != -1:
                    expression = currentInput.split("/")
                    try:
                        answer = float(expression[0]) / float(expression[1])
                    except ZeroDivisionError:
                        return self.label.setText("ERROR: Zero Division")
                if float(answer) == int(answer):
                    self.label.setText(str(int(answer)))
                else:
                    self.label.setText(str(answer))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())