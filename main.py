import sys
from PyQt5.QtWidgets import QApplication
import gui.main_window

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = gui.main_window.MainWindow()
    main_window.show()
    sys.exit(app.exec_())
