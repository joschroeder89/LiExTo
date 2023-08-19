from PyQt5.QtWidgets import (
    QMainWindow,
    QLabel,
    QPushButton,
    QApplication
)
from PyQt5.QtGui import (
    QIcon,
    QFont,
    QImage,
    QPalette,
    QBrush
)
import gui.main_window

class DownloadWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel(self)

        self.width = 1348
        self.height = 900
        self.screen = QApplication.primaryScreen()
        self.x_pos = (self.screen.size().width() // 2) - (self.width // 2)
        self.y_pos = (self.screen.size().height() // 2) - (self.height // 2)

        # image and icon paths
        self.bg_img = QImage("./images/download.png")
        self.icon = QIcon("./images/amg.png")
        self.setWindowIcon(self.icon)

        # fonts
        self.font_big = QFont("Roboto Mono", 26)
        self.font_small = QFont("Roboto Mono", 16)
        self.font_tiny = QFont("Roboto Mono", 10)
        self.font_banner = QFont("Roboto Mono", 40)

        # style sheets
        self.style_sheet_banner = "QPushButton{background-color: rgba(197, 25, 102, 0);\
                                               color: rgb(47, 196, 223);}"
        self.style_sheet = "QPushButton{background-color: rgb(159, 47, 223);\
                                        color: rgb(47, 196, 223);\
                                        border: 2px solid rgb(47, 196, 223);}"
        self.style_sheet_bright = "QPushButton{background-color: rgb(177, 105, 219);\
                                               color: rgb(47, 196, 223);\
                                               border: 2px solid rgb(47, 196, 223);}"

        # set background image and stylesheet
        self.palette = QPalette()
        self.palette.setBrush(QPalette.Window, QBrush(self.bg_img))
        self.setPalette(self.palette)
        self.setGeometry(self.x_pos, self.y_pos, self.width, self.height)
        self.setStyleSheet("QMainWindow{border: 2px solid rgb(47, 196, 223);}")
        self.setWindowTitle("Livery Exchange Tool")
        self.setWindowIcon(self.icon)
        self.setFixedSize(self.width, self.height)
        self.resize(self.width, self.height)

        # banner
        self.banner = QPushButton("Download Liveries", self)
        self.banner.setFont(self.font_banner)
        self.banner.move(400, 75)
        self.banner.resize(600, 75)
        self.banner.setStyleSheet(self.style_sheet_banner)

        # save config button
        self.download_button = QPushButton("Download", self)
        self.download_button.setFont(self.font_big)
        self.download_button.setStyleSheet(self.style_sheet)
        self.download_button.move(900, 750)
        self.download_button.resize(300, 75)
        self.download_button.pressed.connect(self.download_clicked)

        # back button
        self.back_button = QPushButton("Back", self)
        self.back_button.setFont(self.font_big)
        self.back_button.setStyleSheet(self.style_sheet)
        self.back_button.move(150, 750)
        self.back_button.resize(250, 75)
        self.back_button.pressed.connect(self.go_back)

    def update_livery_files(self, livery_files):
        if livery_files:
            self.livery_files = livery_files
        return self.livery_files

    def download_clicked(self):
        self.download_button.setStyleSheet(self.style_sheet_bright)
        self.download_button.released.connect(self.download_button_reset)

    def download_button_reset(self):
        self.download_button.setStyleSheet(self.style_sheet)

    def go_back(self):
        self.back_button.setStyleSheet(self.style_sheet_bright)
        self.back_button.released.connect(self.back_button_reset)

    def back_button_reset(self):
        self.back_button.setStyleSheet(self.style_sheet)
        self.main = gui.main_window.MainWindow()
        self.main.show()
        self.close()
