from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from display import Ui_Form

class TodoListApp(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.add_task)
        self.ui.pushButton_4.clicked.connect(self.delete_task)
        self.ui.pushButton_3.clicked.connect(self.mark_done)

    def add_task(self):
        task = self.ui.lineEdit.text()
        if task:
            self.ui.listWidget.addItem(task)
            self.ui.lineEdit.clear()
        else:
            QMessageBox.warning(self, "Warning", "Task cannot be empty!")

    def delete_task(self):
        selected_task = self.ui.listWidget.currentRow()
        if selected_task >= 0:
            self.ui.listWidget.takeItem(selected_task)
        else:
            QMessageBox.warning(self, "Warning", "No task selected!")

    def mark_done(self):
        selected_task = self.ui.listWidget.currentItem()
        if selected_task:
            selected_task.setText(f"[DONE] {selected_task.text()}")
        else:
            QMessageBox.warning(self, "Warning", "No task selected!")