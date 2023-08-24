from PyQt5.QtWidgets import (
    QMainWindow,
    QLabel,
    QPushButton,
    QListWidget,
    QLineEdit,
    QMessageBox,
    QApplication,
    QProgressBar
)
from PyQt5.QtGui import (
    QIcon,
    QFont,
    QBrush,
    QPalette,
    QImage
)
from PyQt5.QtCore import Qt
from component.dropbox_handler import DropboxHandler
from component.file_handler import FileHandler
import configparser
import gui.main_window
import os
import time

class UploadWindow(QMainWindow):
    def __init__(self, livery_files: list, car_file: str):
        super().__init__()
        self.label = QLabel(self)
        self.list = QListWidget(self)

        # variables
        self.livery_files = livery_files
        self.car_file = car_file

        self.width = 1348
        self.height = 900
        self.screen = QApplication.primaryScreen()
        self.x_pos = (self.screen.size().width() // 2) - (self.width // 2)
        self.y_pos = (self.screen.size().height() // 2) - (self.height // 2)

        # folder and config parser
        self.toplevel_folder = os.getcwd()
        self.dropbox_config = configparser.ConfigParser()
        if os.path.exists(os.path.join(self.toplevel_folder, "dropbox.ini")):
            self.dropbox_config.read(os.path.join(self.toplevel_folder, "dropbox.ini"))
            self.api_token = self.dropbox_config["DROPBOX"]["TOKEN"]
            self.share_link = self.dropbox_config["DROPBOX"]["SHARELINK"]
            if self.api_token:
                self.dropbox_handler = DropboxHandler(self.api_token)

        # image and icon paths
        self.bg_img = QImage("./images/upload.png")
        self.icon = QIcon("./images/amg.png")
        self.setWindowIcon(self.icon)

        # fonts
        self.font_big = QFont("Roboto Mono", 26)
        self.font_small = QFont("Roboto Mono", 16)
        self.font_tiny = QFont("Roboto Mono", 10)
        self.font_banner = QFont("Roboto Mono", 40)

        # style sheets
        self.style_sheet_banner = "QPushButton{background-color: rgba(197, 25, 102, 0);\
                                               color: rgb(253, 214, 38);}"
        self.style_sheet = "QPushButton{background-color: rgb(159, 47, 223);\
                                        color: rgb(47, 196, 223);\
                                        border: 2px solid rgb(47, 196, 223);}"
        self.style_sheet_list = "QListWidget{background-color: rgb(159, 47, 223);\
                                             color: rgb(47, 196, 223);\
                                             border: 2px solid rgb(47, 196, 223);}"
        self.style_sheet_line = "QLineEdit{background-color: rgb(159, 47, 223);\
                                           color: rgb(47, 196, 223);\
                                           border: 2px solid rgb(47, 196, 223);}"
        self.style_sheet_bright = "QPushButton{background-color: rgb(177, 105, 219);\
                                               color: rgb(47, 196, 223);\
                                               border: 2px solid rgb(47, 196, 223);}"
        self.style_sheet_progress_bar = "QProgressBar{background-color: rgb(159, 47, 223);\
                                                      color: rgb(47, 196, 223);\
                                                      border: 2px solid rgb(47, 196, 223);}\
                                        QProgressBar::chunk{background-color: rgb(71, 243, 128);\
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

        # list widget
        self.list.setStyleSheet(self.style_sheet_list)
        self.list.setFont(self.font_tiny)
        self.list.resize(825, 250)
        self.list.move(425, 225)
        if self.livery_files:
            # item_list = [item.split('/')[-1] for item in self.livery_files]
            # folder_list = [folder.split('/')[-2] for folder in self.livery_files]
            # name_list = [name.split('/')[-3] for name in self.livery_files]
            # items = [f"{name}/{folder}/{item}" for item, name, folder in zip(item_list, name_list, folder_list)]
            self.list.addItems(self.livery_files)

        # progress bar
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setStyleSheet(self.style_sheet_progress_bar)
        self.progress_bar.move(178, 600)
        self.progress_bar.resize(1000, 80)
        self.progress_bar.setFont(self.font_banner)
        self.progress_bar.setAlignment(Qt.AlignCenter)

        # clear items
        self.clear_items_button = QPushButton("Clear Items", self)
        self.clear_items_button.setFont(self.font_small)
        self.clear_items_button.setToolTip("Clear all items.")
        self.clear_items_button.setStyleSheet(self.style_sheet)
        self.clear_items_button.resize(350, 50)
        self.clear_items_button.move(50, 335)
        self.clear_items_button.pressed.connect(self.clear_files)

        # livery upload button
        self.banner = QPushButton("Livery Upload", self)
        self.banner.setFont(self.font_banner)
        self.banner.move(300, 25)
        self.banner.resize(800, 200)
        self.banner.setStyleSheet(self.style_sheet_banner)

        # button for choosing livery images
        self.upload_livery_files = QPushButton("Select Livery Images", self)
        self.upload_livery_files.setFont(self.font_small)
        self.upload_livery_files.setToolTip("Upload your livery files.")
        self.upload_livery_files.setStyleSheet(self.style_sheet)
        self.upload_livery_files.move(50, 225)
        self.upload_livery_files.resize(350, 50)
        self.upload_livery_files.pressed.connect(self.livery_files_clicked)

        # button for choosing car.json
        self.upload_livery_json = QPushButton("Select Car.json File", self)
        self.upload_livery_json.setFont(self.font_small)
        self.upload_livery_json.setToolTip("Upload your livery files.")
        self.upload_livery_json.setStyleSheet(self.style_sheet)
        self.upload_livery_json.move(50, 280)
        self.upload_livery_json.resize(350, 50)
        self.upload_livery_json.pressed.connect(self.livery_json_clicked)

        # text input for server adress
        self.server_textbox = QLineEdit(self)
        self.server_textbox.move(178, 520)
        self.server_textbox.resize(1000, 50)
        self.server_textbox.setFont(self.font_small)
        self.server_textbox.setStyleSheet(self.style_sheet_line)
        self.server_textbox.setPlaceholderText("Enter Dropbox Share Link here...")

        # start upload button
        self.upload_button = QPushButton("Upload", self)
        self.upload_button.setFont(self.font_big)
        self.upload_button.setStyleSheet(self.style_sheet)
        self.upload_button.move(1000, 750)
        self.upload_button.resize(250, 75)
        self.upload_button.pressed.connect(self.start_upload)

        # back button
        self.back_button = QPushButton("Back", self)
        self.back_button.setFont(self.font_big)
        self.back_button.setStyleSheet(self.style_sheet)
        self.back_button.move(125, 750)
        self.back_button.resize(250, 75)
        self.back_button.pressed.connect(self.go_back)

    def start_upload(self):
        self.upload_button.setStyleSheet(self.style_sheet_bright)
        self.upload_button.released.connect(self.upload_check)
        self.server_name_input = self.server_textbox.text()

    def upload_check(self):
        for i in range(101):
            time.sleep(0.05)
            self.progress_bar.setValue(i)
        self.upload_button.setStyleSheet(self.style_sheet)

    def livery_files_clicked(self):
        self.upload_livery_files.setStyleSheet(self.style_sheet_bright)
        self.upload_livery_files.released.connect(self.livery_files_reset)

    def livery_files_reset(self):
        self.upload_livery_files.setStyleSheet(self.style_sheet)
        self.upload_handler_liveries()
        self.upload_livery_files.released.disconnect(self.livery_files_reset)

    def upload_handler_liveries(self):
        self.file_handler = FileHandler(self, self.livery_files, self.car_file)
        self.livery_files = self.file_handler.add_livery_files()
        if not self.livery_files:
            return
        if self.livery_files:
            # item_list = [item.split('/')[-1] for item in self.livery_files]
            # folder_list = [folder.split('/')[-2] for folder in self.livery_files]
            # name_list = [name.split('/')[-3] for name in self.livery_files]
            # items = [f"{name}/{folder}/{item}" for item, name, folder in zip(item_list, name_list, folder_list)]
            self.livery_files = list(set(self.livery_files))
            self.list.addItems(self.livery_files)
            self.livery_files = [self.list.item(x).text() for x in range(self.list.count())]
            # self.livery_files = list(set(self.livery_files))
            # for item in items:
            #     if item not in self.livery_files:
            #         self.livery_files.append(item)
        # return

    def livery_json_clicked(self):
        self.upload_livery_json.setStyleSheet(self.style_sheet_bright)
        self.upload_livery_json.released.connect(self.livery_json_reset)

    def livery_json_reset(self):
        self.upload_livery_json.setStyleSheet(self.style_sheet)
        if self.LIVERY_STATUS_OK and bool(self.livery_files):
            self.upload_handler_car_json()
        else:
            self.error_livery_first()
        self.upload_livery_json.released.disconnect(self.livery_json_reset)

    def upload_handler_car_json(self):
        self.car_file_handler = FileHandler(self, "cars")
        if self.car_file_handler.check_car_file(self.livery_files):
            self.livery_files.append(self.car_file)
        # self.car_file = self.car_file_handler.check_car_file(self.livery_files)
        self.CARS_STATUS_OK = True
        if self.car_file != '' and self.car_file is not None:
            self.list.addItem(f"{self.car_file.split('/')[-2]}/"
                              f"{self.car_file.split('/')[-1]}")
        if self.car_file == "":
            return
        if not self.CARS_STATUS_OK:
            self.error_livery_first()

    def go_back(self):
        self.back_button.setStyleSheet(self.style_sheet_bright)
        self.back_button.released.connect(self.back_button_reset)

    def back_button_reset(self):
        self.back_button.setStyleSheet(self.style_sheet)
        self.main = gui.main_window.MainWindow(self.livery_files)
        self.main.show()
        self.close()

    def clear_files(self):
        self.clear_items_button.setStyleSheet(self.style_sheet_bright)
        self.clear_items_button.released.connect(self.clear_files_clicked)

    def clear_files_clicked(self):
        self.clear_items_button.setStyleSheet(self.style_sheet)
        self.list.clear()
        self.livery_files = []

    def error_livery_first(self):
        self.msg = QMessageBox()
        self.msg.setWindowTitle("Upload Livery Files First!")
        self.msg.setIcon(QMessageBox.Critical)
        self.msg.setText("Upload Livery Files First!")
        self.msg.resize(200, 200)
        self.msg.exec_()
