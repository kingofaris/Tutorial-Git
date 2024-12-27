import sys
from PyQt6.QtWidgets import QApplication
from controller import TodoListApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = TodoListApp()
    controller.show() 
    sys.exit(app.exec())