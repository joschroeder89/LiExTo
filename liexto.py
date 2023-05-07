from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap, QFont
import os
import sys

class UploadWindow():
    def __init__(self):
        super().__init__()
        self.widget = QWidget()
        
        # image and icon paths 
        self.icon_path = "./images/amg.png"
        self.bg_img = "./images/upload.png"
        
        # set app resolution and position
        self.width = 1348
        self.height = 900
        screen = QApplication.primaryScreen() 
        self.x_pos = (screen.size().width() // 2) - (self.width//2)
        self.y_pos = (screen.size().height() // 2) - (self.height//2)
        
        self.widget.setGeometry(self.x_pos, self.y_pos, self.width, self.height)
        self.widget.setStyleSheet("QWidget{border: 2px solid rgb(47, 196, 223);}")
        self.widget.setWindowTitle("Livery Exchange Tool")
        self.widget.setWindowIcon(QIcon(self.icon_path))
        self.widget.setFixedSize(self.width, self.height)
        
        self.label = QLabel(self.widget)
        bg_img = QPixmap(self.bg_img)
        self.label.setPixmap(bg_img)
        self.widget.resize(self.width, self.height)
        
        banner = QPushButton("Livery Upload", self.widget)
        banner.setFont(QFont("Airstrike", 30))
        banner.move(400, 75)
        banner.resize(600, 75)
        banner.setStyleSheet("QPushButton{background-color: rgb(159, 47, 223);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}")
        
        # button for choosing livery images 
                
        self.upload_livery_files = QPushButton("Select Livery Images", self.widget)
        self.upload_livery_files.setFont(QFont("Airstrike", 16))
        self.upload_livery_files.setToolTip("Upload your livery files.")
        self.upload_livery_files.setStyleSheet("QPushButton{background-color: rgb(159, 47, 223);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}")
        self.upload_livery_files.move(50, 300)
        self.upload_livery_files.resize(300, 50)
        self.upload_livery_files.pressed.connect(self.livery_files_clicked)
        
        self.upload_livery_json = QPushButton("Select Car.json File", self.widget)
        self.upload_livery_json.setFont(QFont("Airstrike", 16))
        self.upload_livery_json.setToolTip("Upload your livery files.")
        self.upload_livery_json.setStyleSheet("QPushButton{background-color: rgb(159, 47, 223);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}")
        self.upload_livery_json.move(50, 375)
        self.upload_livery_json.resize(300, 50)
        self.upload_livery_json.pressed.connect(self.livery_json_clicked)
        
        self.server_textbox = QLineEdit(self.widget)
        self.server_textbox.move(50, 225)
        self.server_textbox.resize(525, 50)
        self.server_textbox.setFont(QFont("Airstrike", 16))
        self.server_textbox.setStyleSheet("QLineEdit{background-color: rgb(159, 47, 223);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}")
        self.server_textbox.setPlaceholderText("Enter Servername here...")
        
        self.upload_button = QPushButton("Start Upload", self.widget)
        self.upload_button.setFont(QFont("Airstrike", 20))
        self.upload_button.setStyleSheet("QPushButton{background-color: rgb(159, 47, 223);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}")
        self.upload_button.move(1000, 750)
        self.upload_button.resize(250, 75)
        self.upload_button.pressed.connect(self.start_upload)
        
        self.widget.show()
    
    def start_upload(self):
        self.upload_button.setStyleSheet("QPushButton{background-color: rgb(177, 105, 219);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}")
        self.upload_button.released.connect(self.upload_check)
        self.server_name_input = self.server_textbox.text()
    
    def upload_check(self):
        self.upload_button.setStyleSheet("QPushButton{background-color: rgb(159, 47, 223);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}")
        
    def livery_files_clicked(self):
        self.upload_livery_files.setStyleSheet("QPushButton{background-color: rgb(177, 105, 219);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}")
        self.upload_livery_files.released.connect(self.livery_files_reset)
        
    def livery_files_reset(self):
        self.upload_livery_files.setStyleSheet("QPushButton{background-color: rgb(159, 47, 223);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}")

    def livery_json_clicked(self):
        self.upload_livery_json.setStyleSheet("QPushButton{background-color: rgb(177, 105, 219);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}")
        self.upload_livery_json.released.connect(self.livery_json_reset)
        
    def livery_json_reset(self):
        self.upload_livery_json.setStyleSheet("QPushButton{background-color: rgb(159, 47, 223);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}")

class MainWindow():
    def __init__(self):        
        self.widget = QWidget()
        
        # image and icon paths 
        self.icon_path = "./images/amg.png"
        self.bg_img = "./images/cars.png"
        
        # set app resolution and position
        self.width = 1348
        self.height = 900
        screen = QApplication.primaryScreen() 
        self.x_pos = (screen.size().width() // 2) - (self.width//2)
        self.y_pos = (screen.size().height() // 2) - (self.height//2)
        
        self.widget.setGeometry(self.x_pos, self.y_pos, self.width, self.height)
        self.widget.setStyleSheet("QWidget{border: 2px solid rgb(47, 196, 223);}")
        self.widget.setWindowTitle("Livery Exchange Tool")
        self.widget.setWindowIcon(QIcon(self.icon_path))
        self.widget.setFixedSize(self.width, self.height)
        
        self.label = QLabel(self.widget)
        bg_img = QPixmap(self.bg_img)
        self.label.setPixmap(bg_img)
        self.widget.resize(self.width, self.height)
        
        # buttons
        
        banner = QPushButton("Livery Exchange Tool", self.widget)
        banner.setFont(QFont("Airstrike", 30))
        banner.move(400, 75)
        banner.resize(600, 75)
        banner.setStyleSheet("QPushButton{background-color: rgb(197, 25, 102);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}")
        
        self.upload_button = QPushButton("Upload Livery", self.widget)
        self.upload_button.setFont(QFont("Airstrike", 20))
        self.upload_button.setToolTip("Upload your livery files.")
        self.upload_button.setStyleSheet("QPushButton{background-color: rgb(197, 25, 102);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}")
        self.upload_button.move(250, 750)
        self.upload_button.resize(250, 75)
        self.upload_button.pressed.connect(self.upload_clicked)
        
        self.server_button = QPushButton("Server Config", self.widget)
        self.server_button.setFont(QFont("Airstrike", 20))
        self.server_button.setToolTip("Configure Exchange Server.")
        self.server_button.setStyleSheet("QPushButton{background-color: rgb(197, 25, 102);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}")
        self.server_button.move(900, 750)
        self.server_button.resize(250, 75)
        self.server_button.pressed.connect(self.server_conf)
        
        self.widget.show()
    
    def upload_button_color_reset(self):
        self.upload_button.setStyleSheet("QPushButton{background-color: rgb(197, 25, 102);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}")  
          
    def server_button_color_reset(self):
        self.server_button.setStyleSheet("QPushButton{background-color: rgb(197, 25, 102);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}")
        
    def upload_clicked(self):
        self.upload_button.setStyleSheet("QPushButton{background-color: rgb(218, 65, 133);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}")
        self.upload_button.released.connect(self.upload_button_color_reset)
        self.upload = UploadWindow()
        self.widget.hide()
    
    def server_conf(self):
        self.server_button.setStyleSheet("QPushButton{background-color: rgb(218, 65, 133);color: rgb(47, 196, 223);border: 2px solid rgb(47, 196, 223);}")
        self.server_button.released.connect(self.server_button_color_reset)
        print("SERVER CONFIG")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = MainWindow()
    sys.exit(app.exec_())