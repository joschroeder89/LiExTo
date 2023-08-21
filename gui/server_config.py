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
from component.dropbox_handler import DropboxHandler
import configparser
import gui.main_window
import os

class ServerConfig(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel(self)
        self.api_token = ""

        # folder and config parser
        self.toplevel_folder = os.getcwd()
        self.dropbox_config = configparser.ConfigParser()
        if os.path.exists(os.path.join(self.toplevel_folder, "dropbox.ini")):
            self.dropbox_config.read(os.path.join(self.toplevel_folder, "dropbox.ini"))
            self.api_token = self.dropbox_config["DROPBOX"]["TOKEN"]
            self.dropbox_handler = DropboxHandler(self.api_token)

        self.width = 1348
        self.height = 900
        self.screen = QApplication.primaryScreen()
        self.x_pos = (self.screen.size().width() // 2) - (self.width // 2)
        self.y_pos = (self.screen.size().height() // 2) - (self.height // 2)

        # image and icon paths
        self.bg_img = QImage("./images/server.png")
        self.icon = QIcon("./images/amg.png")
        self.setWindowIcon(self.icon)

        # fonts
        self.font_big = QFont("Roboto Mono", 26)
        self.font_small = QFont("Roboto Mono", 16)
        self.font_tiny = QFont("Roboto Mono", 10)
        self.font_banner = QFont("Roboto Mono", 40)

        # style sheets
        self.style_sheet_banner = "QPushButton{background-color: rgba(159, 47, 223,0);\
                                        color: rgb(47, 196, 223);}"
        self.style_sheet = "QPushButton{background-color: rgb(159, 47, 223);\
                                             color: rgb(47, 196, 223);\
                                             border: 2px solid rgb(47, 196, 223);}"
        self.style_sheet_green = "QPushButton{background-color: rgb(0, 255, 157);\
                                              color: rgb(47, 196, 223);\
                                              border: 2px solid rgb(47, 196, 223);}"
        self.style_sheet_line = "QLineEdit{background-color: rgb(159, 47, 223);\
                                      color: rgb(47, 196, 223);\
                                      border: 2px solid rgb(47, 196, 223);}"
        self.style_sheet_line_green = "QLineEdit{background-color: rgb(0, 255, 157);\
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
        self.banner = QPushButton("Server Config", self)
        self.banner.setFont(self.font_banner)
        self.banner.move(400, 75)
        self.banner.resize(600, 75)
        self.banner.setStyleSheet(self.style_sheet_banner)

        # text input for dropbox link
        self.server_textbox = QLineEdit(self)
        self.server_textbox.move(50, 225)
        self.server_textbox.resize(530, 50)
        self.server_textbox.setFont(self.font_small)
        if self.api_token:
            self.server_textbox.setStyleSheet(self.style_sheet_line_green)
        else:
            self.server_textbox.setStyleSheet(self.style_sheet_line)
        self.server_textbox.setPlaceholderText("Enter Dropbox API Token here...")
        self.server_textbox.setText(self.api_token)

        # sharefolder init
        self.sharefolder_textbox = QLineEdit(self)
        self.sharefolder_textbox.move(50, 285)
        self.sharefolder_textbox.resize(530, 50)
        self.sharefolder_textbox.setFont(self.font_small)
        self.sharefolder_textbox.setStyleSheet(self.style_sheet_line)
        self.sharefolder_textbox.setPlaceholderText("Enter Share Folder Name here...")

        # sharelink output box
        self.sharelink_textbox = QLineEdit(self)
        self.sharelink_textbox.move(50, 345)
        self.sharelink_textbox.resize(530, 50)
        self.sharelink_textbox.setFont(self.font_small)
        self.sharelink_textbox.setStyleSheet(self.style_sheet_line)
        self.sharelink_textbox.setPlaceholderText("Dropbox Share Link will appear here...")

        # save dropbox link
        if self.api_token:
            self.set_api_token_button = QPushButton("Token is set", self)
            self.set_api_token_button.setStyleSheet(self.style_sheet_green)
        else:
            self.set_api_token_button = QPushButton("Set Api Token", self)
            self.set_api_token_button.setStyleSheet(self.style_sheet)
            self.set_api_token_button.pressed.connect(self.set_dropbox_api_token)
        self.set_api_token_button.setFont(self.font_small)
        self.set_api_token_button.move(600, 225)
        self.set_api_token_button.resize(275, 50)

        # save dropbox link
        self.save_dropbox_link_button = QPushButton("Generate Share Link", self)
        self.save_dropbox_link_button.setFont(self.font_small)
        self.save_dropbox_link_button.setStyleSheet(self.style_sheet)
        self.save_dropbox_link_button.move(600, 345)
        self.save_dropbox_link_button.resize(275, 50)
        self.save_dropbox_link_button.pressed.connect(self.dropbox_link_button_pressed)

        # create share folder
        self.create_sharefolder_button = QPushButton("Create Share Folder", self)
        self.create_sharefolder_button.setFont(self.font_small)
        self.create_sharefolder_button.setStyleSheet(self.style_sheet)
        self.create_sharefolder_button.move(600, 285)
        self.create_sharefolder_button.resize(275, 50)
        self.create_sharefolder_button.pressed.connect(self.create_sharefolder)

        # save config button
        self.save_config_button = QPushButton("Save", self)
        self.save_config_button.setFont(self.font_big)
        self.save_config_button.setStyleSheet(self.style_sheet)
        self.save_config_button.move(1000, 750)
        self.save_config_button.resize(250, 75)
        self.save_config_button.pressed.connect(self.save_config_clicked)

        # back button
        self.back_button = QPushButton("Back", self)
        self.back_button.setFont(self.font_big)
        self.back_button.setStyleSheet(self.style_sheet)
        self.back_button.move(150, 750)
        self.back_button.resize(250, 75)
        self.back_button.pressed.connect(self.go_back)

    def set_dropbox_api_token(self):
        self.set_api_token_button.setStyleSheet(self.style_sheet_bright)
        self.set_api_token_button.released.connect(self.set_dropbox_api_token_clicked)
        if not os.path.exists(os.path.join(self.toplevel_folder, "dropbox.ini")):
            with open(os.path.join(self.toplevel_folder, "dropbox.ini"), "w") as ini:
                self.dropbox_config["DROPBOX"] = {}
                self.dropbox_config["DROPBOX"]["TOKEN"] = self.server_textbox.text()
                self.dropbox_config.write(ini)
            self.api_token = self.server_textbox.text()
            self.dropbox_handler = DropboxHandler(self.api_token)
            self.set_api_token_button.setText("Token is set")
            self.set_api_token_button.setStyleSheet(self.style_sheet_green)

    def set_dropbox_api_token_clicked(self):
        self.set_api_token_button.setStyleSheet(self.style_sheet)
        self.set_api_token_button.released.disconnect(self.set_dropbox_api_token_clicked)

    def dropbox_link_button_pressed(self):
        self.save_dropbox_link_button.setStyleSheet(self.style_sheet_bright)
        self.save_dropbox_link_button.released.connect(self.dropbox_link_button_released)

    def dropbox_link_button_released(self):
        self.save_dropbox_link_button.setStyleSheet(self.style_sheet)
        self.sharelink = self.dropbox_handler.get_sharelink(self.sharefolder_textbox.text())
        self.sharelink_textbox.setText(self.sharelink.url)
        self.save_dropbox_link_button.released.disconnect(self.dropbox_link_button_released)

    def save_config_clicked(self):
        self.save_config_button.setStyleSheet(self.style_sheet_bright)
        self.save_config_button.released.connect(self.save_config_button_reset)

    def save_config_button_reset(self):
        self.save_config_button.setStyleSheet(self.style_sheet)

    def create_sharefolder(self):
        self.create_sharefolder_button.setStyleSheet(self.style_sheet_bright)
        self.create_sharefolder_button.released.connect(self.create_sharefolder_clicked)

    def create_sharefolder_clicked(self):
        self.create_sharefolder_button.setStyleSheet(self.style_sheet)
        self.dropbox_handler.init_sharefolder(self.sharefolder_textbox.text())
        self.create_sharefolder_button.released.disconnect(self.create_sharefolder_clicked)

    def go_back(self):
        self.back_button.setStyleSheet(self.style_sheet_bright)
        self.back_button.released.connect(self.back_button_reset)

    def back_button_reset(self):
        self.back_button.setStyleSheet(self.style_sheet)
        self.main = gui.main_window.MainWindow()
        self.main.show()
        self.close()
