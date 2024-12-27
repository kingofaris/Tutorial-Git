from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(306, 261)
        Form.setStyleSheet("QWidget {\n"
"    background-color: #ffefd5; \n"
"    font-family: \"Comic Sans MS\", sans-serif;\n"
"    color: #2f4f4f;\n"
"    font-size: 14px;\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setStyleSheet("QLabel {\n"
"    color: #1e90ff;\n"
"    font-weight: bold;\n"
"    font-size: 16px;\n"
"    border: none;\n"
"    padding: 5px;\n"
"}\n"
"")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(parent=Form)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 1)
        self.listWidget = QtWidgets.QListWidget(parent=Form)
        self.listWidget.setStyleSheet("QListWidget {\n"
"    background-color: #f0e68c; \n"
"    border: 2px solid #d2691e; \n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"    font-size: 14px;\n"
"    color: #2f4f4f;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    padding: 5px;\n"
"    border: 1px solid transparent;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"    background-color: #ffa500;\n"
"    color: #ffffff; \n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background-color: #ff4500;\n"
"    color: #ffffff;\n"
"    border: 1px solid #000000; \n"
"}")
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setStyleSheet("QLabel {\n"
"    color: #1e90ff; \n"
"    font-weight: bold;\n"
"    font-size: 16px;\n"
"    border: none;\n"
"    padding: 5px;\n"
"}\n"
"")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #8a2be2;\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"    font-size: 14px;\n"
"    color: #2f4f4f;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #ffa07a;\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 4, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background-color: #ffa07a; \n"
"    border: 2px solid #cd5c5c;\n"
"    border-radius: 10px;\n"
"    color: #ffffff; \n"
"    font-weight: bold;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #f08080; \n"
"    border: 2px solid #8b0000; \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #cd5c5c; \n"
"    border: 2px solid #8b0000; \n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #d3d3d3; \n"
"    border: 2px solid #a9a9a9; \n"
"    color: #7f7f7f; \n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 5, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    background-color: #ffa07a; \n"
"    border: 2px solid #cd5c5c;\n"
"    border-radius: 10px;\n"
"    color: #ffffff; \n"
"    font-weight: bold;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #f08080; \n"
"    border: 2px solid #8b0000; \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #cd5c5c; \n"
"    border: 2px solid #8b0000; \n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #d3d3d3; \n"
"    border: 2px solid #a9a9a9; \n"
"    color: #7f7f7f; \n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 6, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"    background-color: #ffa07a; \n"
"    border: 2px solid #cd5c5c;\n"
"    border-radius: 10px;\n"
"    color: #ffffff; \n"
"    font-weight: bold;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #f08080; \n"
"    border: 2px solid #8b0000; \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #cd5c5c; \n"
"    border: 2px solid #8b0000; \n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #d3d3d3; \n"
"    border: 2px solid #a9a9a9; \n"
"    color: #7f7f7f; \n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 7, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "To-Do List Manager"))
        self.label_2.setText(_translate("Form", "New List"))
        self.pushButton_2.setText(_translate("Form", "Add"))
        self.pushButton_3.setText(_translate("Form", "Done"))
        self.pushButton_4.setText(_translate("Form", "Delete"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
