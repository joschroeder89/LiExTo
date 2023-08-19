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
    def __init__(self):
        super().__init__()
        self.label = QLabel(self)

        self.width = 1348
        self.height = 900
        self.screen = QApplication.primaryScreen()
        self.x_pos = (self.screen.size().width() // 2) - (self.width // 2)
        self.y_pos = (self.screen.size().height() // 2) - (self.height // 2)

        # image and icon paths and fonts
        self.bg_img = QImage("./images/cars.png")
        self.icon = QIcon("./images/amg.png")
        self.setWindowIcon(self.icon)

        self.font_big = QFont("Roboto Mono", 26)
        self.font_small = QFont("Roboto Mono", 16)
        self.font_tiny = QFont("Roboto Mono", 10)

        # files
        self.livery_files = []
        self.car_file = ""

        # set background image and stylesheet
        self.palette = QPalette()
        self.palette.setBrush(QPalette.Window, QBrush(self.bg_img))
        self.setPalette(self.palette)
        self.setStyleSheet("QMainWindow{border: 2px solid rgb(47, 196, 223);}")
        self.setWindowTitle("Livery Exchange Tool")
        self.setWindowIcon(self.icon)
        self.setFixedSize(self.width, self.height)
        self.resize(self.width, self.height)

        # buttons and banner
        self.banner = QPushButton("Livery Exchange Tool", self)
        self.banner.setFont(self.font_big)
        self.banner.move(400, 75)
        self.banner.resize(600, 75)
        self.banner.setStyleSheet(
            "QPushButton{background-color: rgb(197, 25, 102);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}"
        )

        # upload button
        self.upload_button = QPushButton("Upload", self)
        self.upload_button.setFont(self.font_big)
        self.upload_button.setToolTip("Upload your livery files.")
        self.upload_button.setStyleSheet(
            "QPushButton{background-color: rgb(197, 25, 102);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}"
        )
        self.upload_button.move(200, 750)
        self.upload_button.resize(250, 75)
        self.upload_button.pressed.connect(self.upload_clicked)

        # download button
        self.download_button = QPushButton("Download", self)
        self.download_button.setFont(self.font_big)
        self.download_button.setToolTip("Download a livery pack.")
        self.download_button.setStyleSheet(
            "QPushButton{background-color: rgb(197, 25, 102);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}"
        )
        self.download_button.move(550, 750)
        self.download_button.resize(300, 75)
        self.download_button.pressed.connect(self.download_clicked)

        # config button
        self.server_button = QPushButton("Config", self)
        self.server_button.setFont(self.font_big)
        self.server_button.setToolTip("Configure Exchange Server.")
        self.server_button.setStyleSheet(
            "QPushButton{background-color: rgb(197, 25, 102);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}"
        )
        self.server_button.move(950, 750)
        self.server_button.resize(250, 75)
        self.server_button.pressed.connect(self.server_conf)

    def download_clicked(self):
        self.download_button.setStyleSheet(
            "QPushButton{background-color: rgb(218, 65, 133);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}"
        )
        self.download_button.released.connect(self.download_clicked_color_reset)

    def download_clicked_color_reset(self):
        self.download_button.setStyleSheet(
            "QPushButton{background-color: rgb(197, 25, 102);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}"
        )
        self.download_button.released.disconnect(self.download_clicked_color_reset)
        self.download_handler = gui.download_window.DownloadWindow()
        self.download_handler.show()
        self.close()

    def server_conf(self):
        self.server_button.setStyleSheet(
            "QPushButton{background-color: rgb(218, 65, 133);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}"
        )
        self.server_button.released.connect(self.server_button_color_reset)

    def server_button_color_reset(self):
        self.server_button.setStyleSheet(
            "QPushButton{background-color: rgb(197, 25, 102);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}"
        )
        self.server_button.released.disconnect(self.server_button_color_reset)
        self.server_config = gui.server_config.ServerConfig()
        self.server_config.show()
        self.close()

    def upload_clicked(self):
        self.upload_button.setStyleSheet(
            "QPushButton{background-color: rgb(218, 65, 133);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}"
        )
        self.upload_button.released.connect(self.upload_button_color_reset)

    def upload_button_color_reset(self):
        self.upload_button.setStyleSheet(
            "QPushButton{background-color: rgb(197, 25, 102);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}"
        )
        self.upload_button.released.disconnect(self.upload_button_color_reset)
        self.upload = gui.upload_window.UploadWindow()
        self.upload.show()
        self.close()
