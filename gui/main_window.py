from PyQt5.QtWidgets import (
    QMainWindow,
    QLabel,
    QPushButton,
    QApplication
)
from PyQt5.QtGui import (
    QPixmap,
    QIcon,
    QFont,
    QImage,
    QPalette,
    QBrush
)
import gui.download_window
import gui.server_config
import gui.upload_window

class MainWindow(QMainWindow):
    def __init__(self, livery_files=[], car_file=""):
        super().__init__()
        self.label = QLabel(self)

        # variables
        self.livery_files = livery_files
        self.car_file = car_file
        print(self.livery_files)
        print(self.car_file)

        self.width = 1348
        self.height = 900
        self.screen = QApplication.primaryScreen()
        self.x_pos = (self.screen.size().width() // 2) - (self.width // 2)
        self.y_pos = (self.screen.size().height() // 2) - (self.height // 2)

        # image and icon paths and fonts
        self.bg_img = QImage("./images/cars.png")
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
        self.style_sheet = "QPushButton{background-color: rgb(197, 25, 102);\
                                        color: rgb(47, 196, 223);\
                                        border: 2px solid rgb(47, 196, 223);}"
        self.style_sheet_bright = "QPushButton{background-color: rgb(218, 65, 133);\
                                               color: rgb(47, 196, 223);\
                                               border: 2px solid rgb(47, 196, 223);}"

        # set background image and stylesheet
        self.palette = QPalette()
        self.palette.setBrush(QPalette.Window, QBrush(self.bg_img))
        self.setPalette(self.palette)
        self.setStyleSheet("QMainWindow{border: 2px solid rgb(47, 196, 223);}")
        self.setWindowTitle("Livery Exchange Tool")
        self.setWindowIcon(self.icon)
        self.setFixedSize(self.width, self.height)
        self.resize(self.width, self.height)

        # banner
        self.banner = QPushButton("Livery Exchange Tool", self)
        self.banner.setFont(self.font_banner)
        self.banner.move(300, 25)
        self.banner.resize(800, 200)
        self.banner.setStyleSheet(self.style_sheet_banner)

        # upload button
        self.upload_button = QPushButton("Upload", self)
        self.upload_button.setFont(self.font_big)
        self.upload_button.setToolTip("Upload your livery files.")
        self.upload_button.setStyleSheet(self.style_sheet)
        self.upload_button.move(200, 750)
        self.upload_button.resize(250, 75)
        self.upload_button.pressed.connect(self.upload_clicked)

        # download button
        self.download_button = QPushButton("Download", self)
        self.download_button.setFont(self.font_big)
        self.download_button.setToolTip("Download a livery pack.")
        self.download_button.setStyleSheet(self.style_sheet)
        self.download_button.move(550, 750)
        self.download_button.resize(300, 75)
        self.download_button.pressed.connect(self.download_clicked)

        # config button
        self.server_button = QPushButton("Config", self)
        self.server_button.setFont(self.font_big)
        self.server_button.setToolTip("Configure Exchange Server.")
        self.server_button.setStyleSheet(self.style_sheet)
        self.server_button.move(950, 750)
        self.server_button.resize(250, 75)
        self.server_button.pressed.connect(self.server_conf)

    def update_livery_files(self, livery_files):
        if livery_files:
            self.livery_files = livery_files
        return self.livery_files

    def download_clicked(self):
        self.download_button.setStyleSheet(self.style_sheet_bright)
        self.download_button.released.connect(self.download_clicked_color_reset)

    def download_clicked_color_reset(self):
        self.download_button.setStyleSheet(self.style_sheet)
        self.download_button.released.disconnect(self.download_clicked_color_reset)
        self.download_handler = gui.download_window.DownloadWindow()
        self.download_handler.show()
        self.close()

    def server_conf(self):
        self.server_button.setStyleSheet(self.style_sheet_bright)
        self.server_button.released.connect(self.server_button_color_reset)

    def server_button_color_reset(self):
        self.server_button.setStyleSheet(self.style_sheet)
        self.server_button.released.disconnect(self.server_button_color_reset)
        self.server_config = gui.server_config.ServerConfig()
        self.server_config.show()
        self.close()

    def upload_clicked(self):
        self.upload_button.setStyleSheet(self.style_sheet_bright)
        self.upload_button.released.connect(self.upload_button_color_reset)

    def upload_button_color_reset(self):
        self.upload_button.setStyleSheet(self.style_sheet)
        self.upload_button.released.disconnect(self.upload_button_color_reset)
        self.upload = gui.upload_window.UploadWindow(self.livery_files, self.car_file)
        self.upload.show()
        self.close()
