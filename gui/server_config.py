from PyQt5.QtWidgets import (
    QMainWindow,
    QLabel,
    QPushButton,
    QLineEdit,
    QApplication
)
from PyQt5.QtGui import (
    QIcon,
    QFont,
    QImage,
    QPalette,
    QBrush
)
from component.dropbox_config import DropboxConfig
import gui.main_window

class ServerConfig(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel(self)
        self.drpbx_api_token = ""

        self.width = 1348
        self.height = 900
        self.screen = QApplication.primaryScreen()
        self.x_pos = (self.screen.size().width() // 2) - (self.width // 2)
        self.y_pos = (self.screen.size().height() // 2) - (self.height // 2)

        # image and icon paths
        self.bg_img = QImage("./images/server.png")
        self.icon = QIcon("./images/amg.png")
        self.setWindowIcon(self.icon)

        self.font_big = QFont("Roboto Mono", 26)
        self.font_small = QFont("Roboto Mono", 16)
        self.font_tiny = QFont("Roboto Mono", 10)

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
        self.banner = QPushButton("Server Config", self)
        self.banner.setFont(self.font_big)
        self.banner.move(400, 75)
        self.banner.resize(600, 75)
        self.banner.setStyleSheet(
            "QPushButton{background-color: rgb(159, 47, 223);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}"
        )

        # text input for dropbox link
        self.server_textbox = QLineEdit(self)
        self.server_textbox.move(50, 225)
        self.server_textbox.resize(525, 50)
        self.server_textbox.setFont(self.font_small)
        self.server_textbox.setStyleSheet(
            "QLineEdit{background-color: rgb(159, 47, 223);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}"
        )
        self.server_textbox.setPlaceholderText("Enter Dropbox API Token here...")

        # save dropbox link
        self.save_drpbx_link_button = QPushButton("Save", self)
        self.save_drpbx_link_button.setFont(self.font_tiny)
        self.save_drpbx_link_button.setStyleSheet(
            "QPushButton{background-color: rgb(159, 47, 223);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}"
        )
        self.save_drpbx_link_button.move(600, 225)
        self.save_drpbx_link_button.resize(100, 50)
        self.save_drpbx_link_button.pressed.connect(self.drpbox_link_button_pressed)

        # save config button
        self.save_config_button = QPushButton("Save", self)
        self.save_config_button.setFont(self.font_big)
        self.save_config_button.setStyleSheet(
            "QPushButton{background-color: rgb(159, 47, 223);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}"
        )
        self.save_config_button.move(1000, 750)
        self.save_config_button.resize(250, 75)
        self.save_config_button.pressed.connect(self.save_config_clicked)

        # back button
        self.back_button = QPushButton("Back", self)
        self.back_button.setFont(self.font_big)
        self.back_button.setStyleSheet(
            "QPushButton{background-color: rgb(159, 47, 223);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}"
        )
        self.back_button.move(150, 750)
        self.back_button.resize(250, 75)
        self.back_button.pressed.connect(self.go_back)

    def drpbox_link_button_pressed(self):
        self.save_drpbx_link_button.setStyleSheet(
            "QPushButton{background-color: rgb(177, 105, 219);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}"
        )
        self.save_drpbx_link_button.released.connect(self.drpbox_link_button_released)
        api_token = self.server_textbox.text()
        self.drpbx_handler = DropboxConfig(api_token)

    def drpbox_link_button_released(self):
        self.save_drpbx_link_button.setStyleSheet(
            "QPushButton{background-color: rgb(159, 47, 223);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}"
        )
        self.save_drpbx_link_button.released.disconnect(self.drpbox_link_button_released)

    def save_config_clicked(self):
        self.save_config_button.setStyleSheet(
            "QPushButton{background-color: rgb(177, 105, 219);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}"
        )
        self.save_config_button.released.connect(self.save_config_button_reset)

    def save_config_button_reset(self):
        self.save_config_button.setStyleSheet(
            "QPushButton{background-color: rgb(159, 47, 223);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}"
        )

    def go_back(self):
        self.back_button.setStyleSheet(
            "QPushButton{background-color: rgb(177, 105, 219);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}"
        )
        self.back_button.released.connect(self.back_button_reset)

    def back_button_reset(self):
        self.back_button.setStyleSheet(
            "QPushButton{background-color: rgb(159, 47, 223);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}"
        )
        self.main = gui.main_window.MainWindow()
        self.main.show()
        self.close()
