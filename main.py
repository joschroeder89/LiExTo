from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap, QFont
from file_handler import FileHandler
import os
import sys


class MainWindow:
    def __init__(self):
        self.widget = QWidget()
        self.label = QLabel(self.widget)

        # image and icon paths and fonts
        self.icon = QIcon("./images/amg.png")
        self.bg_img = QPixmap("./images/cars.png")
        self.font_big = QFont("Race Sport", 26)
        self.font_small = QFont("Race Sport", 16)
        self.font_tiny = QFont("Race Sport", 10)

        # set app resolution and position
        self.width = 1348
        self.height = 900
        self.screen = QApplication.primaryScreen()
        self.x_pos = (self.screen.size().width() // 2) - (self.width // 2)
        self.y_pos = (self.screen.size().height() // 2) - (self.height // 2)

        # files
        self.livery_files = []
        self.car_file = ""
        
        # set background image and stylesheet
        self.label.setPixmap(self.bg_img)
        self.widget.setGeometry(self.x_pos, self.y_pos, self.width, self.height)
        self.widget.setStyleSheet("QWidget{border: 2px solid rgb(47, 196, 223);}")
        self.widget.setWindowTitle("Livery Exchange Tool")
        self.widget.setWindowIcon(self.icon)
        self.widget.setFixedSize(self.width, self.height)
        self.widget.resize(self.width, self.height)

        # buttons and banner
        banner = QPushButton("Livery Exchange Tool", self.widget)
        banner.setFont(self.font_big)
        banner.move(400, 75)
        banner.resize(600, 75)
        banner.setStyleSheet(
            "QPushButton{background-color: rgb(197, 25, 102);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}"
        )

        # upload button
        self.upload_button = QPushButton("Upload", self.widget)
        self.upload_button.setFont(self.font_big)
        self.upload_button.setToolTip("Upload your livery files.")
        self.upload_button.setStyleSheet(
            "QPushButton{background-color: rgb(197, 25, 102);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}"
        )
        self.upload_button.move(200, 750)
        self.upload_button.resize(250, 75)
        self.upload_button.pressed.connect(self.upload_clicked)

        # download button
        self.download_button = QPushButton("Download", self.widget)
        self.download_button.setFont(self.font_big)
        self.download_button.setToolTip("Download a livery pack.")
        self.download_button.setStyleSheet(
            "QPushButton{background-color: rgb(197, 25, 102);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}"
        )
        self.download_button.move(550, 750)
        self.download_button.resize(300, 75)
        self.download_button.pressed.connect(self.download_clicked)
        
        # config button
        self.server_button = QPushButton("Config", self.widget)
        self.server_button.setFont(self.font_big)
        self.server_button.setToolTip("Configure Exchange Server.")
        self.server_button.setStyleSheet(
            "QPushButton{background-color: rgb(197, 25, 102);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}"
        )
        self.server_button.move(950, 750)
        self.server_button.resize(250, 75)
        self.server_button.pressed.connect(self.server_conf)

        self.widget.show()

    def download_clicked(self):
        self.download_button.setStyleSheet(
            "QPushButton{background-color: rgb(218, 65, 133);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}"
        )
        self.download_button.released.connect(self.download_clicked_color_reset)
    
    def download_clicked_color_reset(self):
        self.download_button.setStyleSheet(
            "QPushButton{background-color: rgb(197, 25, 102);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}"
        )
        self.download_handler = DownloadWindow()
        self.widget.close()
        self.download_button.released.disconnect(self.download_clicked_color_reset)
    
    def server_button_color_reset(self):
        self.server_button.setStyleSheet(
            "QPushButton{background-color: rgb(197, 25, 102);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}"
        )
        self.server_config = ServerConfig()
        self.widget.close()

    def server_conf(self):
        self.server_button.setStyleSheet(
            "QPushButton{background-color: rgb(218, 65, 133);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}"
        )
        self.server_button.released.connect(self.server_button_color_reset)

    def upload_button_color_reset(self):
        self.upload_button.setStyleSheet(
            "QPushButton{background-color: rgb(197, 25, 102);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}"
        )
        self.upload = UploadWindow()
        self.widget.close()

    def upload_clicked(self):
        self.upload_button.setStyleSheet(
            "QPushButton{background-color: rgb(218, 65, 133);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}"
        )
        self.upload_button.released.connect(self.upload_button_color_reset)


class UploadWindow(MainWindow):
    def __init__(self):
        super().__init__()
        self.widget = QWidget()
        self.label = QLabel(self.widget)
        self.list = QListWidget(self.widget)
        
        # upload flags
        self.LIVERY_STATUS_OK = False
        self.CARS_STATUS_OK = False

        # image and icon paths
        self.bg_img = QPixmap("./images/upload.png")

        # set background image and stylesheet
        self.label.setPixmap(self.bg_img)
        self.widget.setGeometry(self.x_pos, self.y_pos, self.width, self.height)
        self.widget.setStyleSheet("QWidget{border: 2px solid rgb(47, 196, 223);}")
        self.widget.setWindowTitle("Livery Exchange Tool")
        self.widget.setWindowIcon(self.icon)
        self.widget.setFixedSize(self.width, self.height)
        self.widget.resize(self.width, self.height)

        # list widget 
        self.list.setStyleSheet("QListWidget{background-color: rgb(159, 47, 223);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}")
        self.list.setFont(self.font_tiny)
        self.list.resize(500, 200)
        self.list.move(750, 225)
        # self.list.setAlternatingRowColors(True)
        # self.list.setDragDropMode()
        
        # livery upload button
        self.banner = QPushButton("Livery Upload", self.widget)
        self.banner.setFont(self.font_big)
        self.banner.move(300, 75)
        self.banner.resize(600, 75)
        self.banner.setStyleSheet(
            "QPushButton{background-color: rgb(159, 47, 223);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}"
        )

        # button for choosing livery images
        self.upload_livery_files = QPushButton("Select Livery Images", self.widget)
        self.upload_livery_files.setFont(self.font_small)
        self.upload_livery_files.setToolTip("Upload your livery files.")
        self.upload_livery_files.setStyleSheet(
            "QPushButton{background-color: rgb(159, 47, 223);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}"
        )
        self.upload_livery_files.move(50, 300)
        self.upload_livery_files.resize(350, 50)
        self.upload_livery_files.pressed.connect(self.livery_files_clicked)

        # button for choosing car.json
        self.upload_livery_json = QPushButton("Select Car.json File", self.widget)
        self.upload_livery_json.setFont(self.font_small)
        self.upload_livery_json.setToolTip("Upload your livery files.")
        self.upload_livery_json.setStyleSheet(
            "QPushButton{background-color: rgb(159, 47, 223);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}"
        )
        self.upload_livery_json.move(50, 375)
        self.upload_livery_json.resize(350, 50)
        self.upload_livery_json.pressed.connect(self.livery_json_clicked)

        # text input for server adress
        self.server_textbox = QLineEdit(self.widget)
        self.server_textbox.move(50, 225)
        self.server_textbox.resize(525, 50)
        self.server_textbox.setFont(self.font_small)
        self.server_textbox.setStyleSheet(
            "QLineEdit{background-color: rgb(159, 47, 223);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}"
        )
        self.server_textbox.setPlaceholderText("Enter Servername here...")

        # start upload button
        self.upload_button = QPushButton("Upload", self.widget)
        self.upload_button.setFont(self.font_big)
        self.upload_button.setStyleSheet(
            "QPushButton{background-color: rgb(159, 47, 223);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}"
        )
        self.upload_button.move(1000, 750)
        self.upload_button.resize(250, 75)
        self.upload_button.pressed.connect(self.start_upload)

        # back button
        self.back_button = QPushButton("Back", self.widget)
        self.back_button.setFont(self.font_big)
        self.back_button.setStyleSheet(
            "QPushButton{background-color: rgb(159, 47, 223);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}"
        )
        self.back_button.move(150, 750)
        self.back_button.resize(250, 75)
        self.back_button.pressed.connect(self.go_back)

        self.widget.show()

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
        self.livery_files_handler = FileHandler(self.widget, "liveries")
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
        self.main = MainWindow()
        self.widget.close()

    def error_livery_first(self):
        self.msg = QMessageBox()
        self.msg.setWindowTitle("Upload Livery Files First!")
        self.msg.setIcon(QMessageBox.Critical)
        self.msg.setText("Upload Livery Files First!")
        self.msg.resize(200, 200)
        self.msg.exec_()
        

class DownloadWindow(MainWindow):
    def __init__(self):
        super().__init__()
        self.widget = QWidget()
        self.label = QLabel(self.widget)
        
        # image and icon paths
        self.bg_img = QPixmap("./images/download.png")
        
        # set background image and stylesheet
        self.label.setPixmap(self.bg_img)
        self.widget.setGeometry(self.x_pos, self.y_pos, self.width, self.height)
        self.widget.setStyleSheet("QWidget{border: 2px solid rgb(47, 196, 223);}")
        self.widget.setWindowTitle("Livery Exchange Tool")
        self.widget.setWindowIcon(self.icon)
        self.widget.setFixedSize(self.width, self.height)
        self.widget.resize(self.width, self.height)
                # banner
        self.banner = QPushButton("Download Liveries", self.widget)
        self.banner.setFont(self.font_big)
        self.banner.move(400, 75)
        self.banner.resize(600, 75)
        self.banner.setStyleSheet(
            "QPushButton{background-color: rgb(159, 47, 223);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}"
        )

        # save config button
        self.download_button = QPushButton("Download", self.widget)
        self.download_button.setFont(self.font_big)
        self.download_button.setStyleSheet(
            "QPushButton{background-color: rgb(159, 47, 223);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}"
        )
        self.download_button.move(900, 750)
        self.download_button.resize(300, 75)
        self.download_button.pressed.connect(self.download_clicked)

        # back button
        self.back_button = QPushButton("Back", self.widget)
        self.back_button.setFont(self.font_big)
        self.back_button.setStyleSheet(
            "QPushButton{background-color: rgb(159, 47, 223);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}"
        )
        self.back_button.move(150, 750)
        self.back_button.resize(250, 75)
        self.back_button.pressed.connect(self.go_back)

        self.widget.show()

    def download_clicked(self):
        self.download_button.setStyleSheet(
            "QPushButton{background-color: rgb(177, 105, 219);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}"
        )
        self.download_button.released.connect(self.download_button_reset)

    def download_button_reset(self):
        self.download_button.setStyleSheet(
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
        self.main = MainWindow()
        self.widget.close()
        
class ServerConfig(MainWindow):
    def __init__(self):
        super().__init__()
        self.widget = QWidget()
        self.label = QLabel(self.widget)

        # image and icon paths
        self.bg_img = QPixmap("./images/server.png")

        # set background image and stylesheet
        self.label.setPixmap(self.bg_img)
        self.widget.setGeometry(self.x_pos, self.y_pos, self.width, self.height)
        self.widget.setStyleSheet("QWidget{border: 2px solid rgb(47, 196, 223);}")
        self.widget.setWindowTitle("Livery Exchange Tool")
        self.widget.setWindowIcon(self.icon)
        self.widget.setFixedSize(self.width, self.height)
        self.widget.resize(self.width, self.height)

        # banner
        self.banner = QPushButton("Server Config", self.widget)
        self.banner.setFont(self.font_big)
        self.banner.move(400, 75)
        self.banner.resize(600, 75)
        self.banner.setStyleSheet(
            "QPushButton{background-color: rgb(159, 47, 223);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}"
        )

        # save config button
        self.save_config_button = QPushButton("Save", self.widget)
        self.save_config_button.setFont(self.font_big)
        self.save_config_button.setStyleSheet(
            "QPushButton{background-color: rgb(159, 47, 223);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}"
        )
        self.save_config_button.move(1000, 750)
        self.save_config_button.resize(250, 75)
        self.save_config_button.pressed.connect(self.save_config_clicked)

        # back button
        self.back_button = QPushButton("Back", self.widget)
        self.back_button.setFont(self.font_big)
        self.back_button.setStyleSheet(
            "QPushButton{background-color: rgb(159, 47, 223);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}"
        )
        self.back_button.move(150, 750)
        self.back_button.resize(250, 75)
        self.back_button.pressed.connect(self.go_back)

        self.widget.show()

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
        self.main = MainWindow()
        self.widget.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = MainWindow()
    sys.exit(app.exec_())
