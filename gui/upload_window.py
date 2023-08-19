from PyQt5.QtWidgets import (
    QMainWindow,
    QLabel,
    QPushButton,
    QListWidget,
    QLineEdit,
    QMessageBox,
    QApplication
)
from PyQt5.QtGui import (
    QPixmap,
    QIcon,
    QFont,
    QBrush,
    QPalette,
    QImage
)
from component.file_handler import FileHandler
import gui.main_window

class UploadWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel(self)
        self.list = QListWidget(self)

        self.width = 1348
        self.height = 900
        self.screen = QApplication.primaryScreen()
        self.x_pos = (self.screen.size().width() // 2) - (self.width // 2)
        self.y_pos = (self.screen.size().height() // 2) - (self.height // 2)

        # upload flags
        self.LIVERY_STATUS_OK = False
        self.CARS_STATUS_OK = False

        # image and icon paths
        self.bg_img = QImage("./images/upload.png")
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

        # list widget
        self.list.setStyleSheet("QListWidget{background-color: rgb(159, 47, 223);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}")
        self.list.setFont(self.font_tiny)
        self.list.resize(500, 200)
        self.list.move(750, 225)

        # livery upload button
        self.banner = QPushButton("Livery Upload", self)
        self.banner.setFont(self.font_big)
        self.banner.move(300, 75)
        self.banner.resize(600, 75)
        self.banner.setStyleSheet(
            "QPushButton{background-color: rgb(159, 47, 223);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}"
        )

        # button for choosing livery images
        self.upload_livery_files = QPushButton("Select Livery Images", self)
        self.upload_livery_files.setFont(self.font_small)
        self.upload_livery_files.setToolTip("Upload your livery files.")
        self.upload_livery_files.setStyleSheet(
            "QPushButton{background-color: rgb(159, 47, 223);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}"
        )
        self.upload_livery_files.move(50, 300)
        self.upload_livery_files.resize(350, 50)
        self.upload_livery_files.pressed.connect(self.livery_files_clicked)

        # button for choosing car.json
        self.upload_livery_json = QPushButton("Select Car.json File", self)
        self.upload_livery_json.setFont(self.font_small)
        self.upload_livery_json.setToolTip("Upload your livery files.")
        self.upload_livery_json.setStyleSheet(
            "QPushButton{background-color: rgb(159, 47, 223);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}"
        )
        self.upload_livery_json.move(50, 375)
        self.upload_livery_json.resize(350, 50)
        self.upload_livery_json.pressed.connect(self.livery_json_clicked)

        # text input for server adress
        self.server_textbox = QLineEdit(self)
        self.server_textbox.move(50, 225)
        self.server_textbox.resize(525, 50)
        self.server_textbox.setFont(self.font_small)
        self.server_textbox.setStyleSheet(
            "QLineEdit{background-color: rgb(159, 47, 223);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}"
        )
        self.server_textbox.setPlaceholderText("Enter Dropbox Share Link here...")

        # start upload button
        self.upload_button = QPushButton("Upload", self)
        self.upload_button.setFont(self.font_big)
        self.upload_button.setStyleSheet(
            "QPushButton{background-color: rgb(159, 47, 223);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}"
        )
        self.upload_button.move(1000, 750)
        self.upload_button.resize(250, 75)
        self.upload_button.pressed.connect(self.start_upload)

        # back button
        self.back_button = QPushButton("Back", self)
        self.back_button.setFont(self.font_big)
        self.back_button.setStyleSheet(
            "QPushButton{background-color: rgb(159, 47, 223);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}"
        )
        self.back_button.move(150, 750)
        self.back_button.resize(250, 75)
        self.back_button.pressed.connect(self.go_back)

    def start_upload(self):
        self.upload_button.setStyleSheet(
            "QPushButton{background-color: rgb(177, 105, 219);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}"
        )
        self.upload_button.released.connect(self.upload_check)
        self.server_name_input = self.server_textbox.text()

    def upload_check(self):
        self.upload_button.setStyleSheet(
            "QPushButton{background-color: rgb(159, 47, 223);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}"
        )

    def livery_files_clicked(self):
        self.upload_livery_files.setStyleSheet(
            "QPushButton{background-color: rgb(177, 105, 219);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}"
        )
        self.upload_livery_files.released.connect(self.livery_files_reset)

    def livery_files_reset(self):
        self.upload_livery_files.setStyleSheet(
            "QPushButton{background-color: rgb(159, 47, 223);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}"
        )
        self.upload_handler_liveries()
        self.upload_livery_files.released.disconnect(self.livery_files_reset)

    def upload_handler_liveries(self):
        self.livery_files_handler = FileHandler(self, "liveries")
        self.livery_files = self.livery_files_handler.check_files()
        if len(self.livery_files) == 0 or self.livery_files is None:
            return
        if len(self.livery_files):
            self.LIVERY_STATUS_OK = True
            item_list = [item.split('/')[-1] for item in self.livery_files]
            folder_list = [folder.split('/')[-2] for folder in self.livery_files]
            items = [f"{folder}/{item}" for item, folder in zip(item_list, folder_list)]
            self.list.addItems(items)
        return

    def livery_json_clicked(self):
        self.upload_livery_json.setStyleSheet(
            "QPushButton{background-color: rgb(177, 105, 219);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}"
        )
        self.upload_livery_json.released.connect(self.livery_json_reset)

    def livery_json_reset(self):
        self.upload_livery_json.setStyleSheet(
            "QPushButton{background-color: rgb(159, 47, 223);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}"
        )
        if self.LIVERY_STATUS_OK and bool(self.livery_files):
            self.upload_handler_car_json()
        self.upload_livery_json.released.disconnect(self.livery_json_reset)

    def upload_handler_car_json(self):
        self.car_file_handler = FileHandler(self.widget, "cars")
        self.car_file = self.car_file_handler.check_file(self.livery_files)
        self.CARS_STATUS_OK = True
        if self.car_file != '' and self.car_file is not None:
            self.list.addItem(f"{self.car_file.split('/')[-2]}/"
                              f"{self.car_file.split('/')[-1]}")
        if self.car_file == "":
            return
        if not self.CARS_STATUS_OK:
            self.error_livery_first()

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

    def error_livery_first(self):
        self.msg = QMessageBox()
        self.msg.setWindowTitle("Upload Livery Files First!")
        self.msg.setIcon(QMessageBox.Critical)
        self.msg.setText("Upload Livery Files First!")
        self.msg.resize(200, 200)
        self.msg.exec_()
