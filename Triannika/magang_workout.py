from PyQt6 import QtCore, QtGui, QtWidgets
import csv

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 400)  # Resizing to a more spacious initial size
        Form.setWindowTitle("Workout Planner")

        # Main layout
        self.mainLayout = QtWidgets.QVBoxLayout(Form)

        # Table widget setup
        self.tableWidget = QtWidgets.QTableWidget()
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)  # Start with 0 rows
        self.tableWidget.setHorizontalHeaderLabels(["Gerakan", "Hari", "Repetisi"])
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)  # Disable direct editing
        # Make columns stretch and adjust responsively
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)

        # Enable vertical scrollbar if content exceeds table height
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)

        self.mainLayout.addWidget(self.tableWidget)

        # Buttons layout
        self.buttonsLayout = QtWidgets.QHBoxLayout()

        self.addButton = QtWidgets.QPushButton("Tambah")
        self.addButton.setObjectName("addButton")
        self.buttonsLayout.addWidget(self.addButton)

        self.editButton = QtWidgets.QPushButton("Edit")
        self.editButton.setObjectName("editButton")
        self.buttonsLayout.addWidget(self.editButton)

        self.deleteButton = QtWidgets.QPushButton("Hapus")
        self.deleteButton.setObjectName("deleteButton")
        self.buttonsLayout.addWidget(self.deleteButton)

        self.mainLayout.addLayout(self.buttonsLayout)

        # Save and load buttons layout
        self.saveLoadLayout = QtWidgets.QHBoxLayout()

        self.saveButton = QtWidgets.QPushButton("Simpan")
        self.saveButton.setObjectName("saveButton")
        self.saveLoadLayout.addWidget(self.saveButton)

        self.loadButton = QtWidgets.QPushButton("Muat")
        self.loadButton.setObjectName("loadButton")
        self.saveLoadLayout.addWidget(self.loadButton)

        self.mainLayout.addLayout(self.saveLoadLayout)

        # Connecting buttons to methods
        self.addButton.clicked.connect(self.add_row)
        self.editButton.clicked.connect(self.open_edit_popup)
        self.deleteButton.clicked.connect(self.delete_row)
        self.saveButton.clicked.connect(self.save_data)
        self.loadButton.clicked.connect(self.load_data)

    def add_row(self):
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)

        # Pre-fill new row with placeholders
        self.tableWidget.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem("Gerakan"))
        self.tableWidget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem("Hari"))  # Default "Hari"
        self.tableWidget.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem("Repetisi"))

    def open_edit_popup(self):
        selected = self.tableWidget.selectionModel().selectedRows()
        if selected:
            row = selected[0].row()
            self.show_edit_dialog(row)

    def show_edit_dialog(self, row):
        dialog = QtWidgets.QDialog()
        dialog.setWindowTitle("Edit Data")
        dialog.resize(300, 200)

        layout = QtWidgets.QVBoxLayout(dialog)

        gerakan_label = QtWidgets.QLabel("Gerakan:")
        self.gerakan_input = QtWidgets.QLineEdit(self.tableWidget.item(row, 0).text())

        hari_label = QtWidgets.QLabel("Hari:")
        self.hari_input = QtWidgets.QLineEdit(self.tableWidget.item(row, 1).text())

        repetisi_label = QtWidgets.QLabel("Repetisi:")
        self.repetisi_input = QtWidgets.QLineEdit(self.tableWidget.item(row, 2).text())

        save_button = QtWidgets.QPushButton("Simpan")
        save_button.clicked.connect(lambda: self.save_edits(dialog, row))

        layout.addWidget(gerakan_label)
        layout.addWidget(self.gerakan_input)
        layout.addWidget(hari_label)
        layout.addWidget(self.hari_input)
        layout.addWidget(repetisi_label)
        layout.addWidget(self.repetisi_input)
        layout.addWidget(save_button)

        dialog.exec()

    def save_edits(self, dialog, row):
        self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(self.gerakan_input.text()))
        self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(self.hari_input.text()))
        self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(self.repetisi_input.text()))
        dialog.accept()

    def delete_row(self):
        selected = self.tableWidget.selectionModel().selectedRows()
        if selected:
            for index in sorted(selected, reverse=True):
                self.tableWidget.removeRow(index.row())

    def save_data(self):
        filePath, _ = QtWidgets.QFileDialog.getSaveFileName(None, "Simpan Data", "", "CSV Files (*.csv)")
        if filePath:
            with open(filePath, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["Gerakan", "Hari", "Repetisi"])  # Header
                for row in range(self.tableWidget.rowCount()):
                    row_data = [
                        self.tableWidget.item(row, 0).text() if self.tableWidget.item(row, 0) else "",
                        self.tableWidget.item(row, 1).text() if self.tableWidget.item(row, 1) else "",
                        self.tableWidget.item(row, 2).text() if self.tableWidget.item(row, 2) else ""
                    ]
                    writer.writerow(row_data)

    def load_data(self):
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Muat Data", "", "CSV Files (*.csv)")
        if filePath:
            with open(filePath, "r", encoding="utf-8") as file:
                reader = csv.reader(file)
                headers = next(reader, None)  # Skip header
                self.tableWidget.setRowCount(0)  # Clear current data
                for row_data in reader:
                    rowPosition = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(rowPosition)
                    for col, data in enumerate(row_data):
                        self.tableWidget.setItem(rowPosition, col, QtWidgets.QTableWidgetItem(data))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
