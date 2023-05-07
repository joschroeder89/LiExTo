import os
import sys
from PyQt5.QtWidgets import  QFileDialog, QMessageBox, QWidget

class FileHandler():
    def __init__(self, widget: QWidget, file_type: str) -> None:
        self.file_handler = QFileDialog()
        self.widget = widget
        self.msg = QMessageBox()
        self.file_ext = [".png", ".json", ".dds"]
        self.root_dir = os.path.expanduser("~")
        self.acc_livery_dir = os.path.join(
            self.root_dir, 
            "Documents",
            "Assetto Corsa Competizione",
            "Customs\Liveries"
            )
        self.acc_cars_dir = os.path.join(
            self.root_dir, 
            "Documents",
            "Assetto Corsa Competizione",
            "Customs\Cars"
            )
        if file_type == "liveries":
            self.files, _ = QFileDialog.getOpenFileNames(
                parent=widget,
                caption="Upload livery files",
                directory=self.acc_livery_dir,
                filter="Livery .png, .dds and .json(*)",
            )
            self.files = [file for file in self.files
                        if file.endswith(tuple(self.file_ext))]
            self.check_files(self.files)
        
        if file_type == "cars":
            self.file, _ = QFileDialog.getOpenFileName(
                parent=widget,
                caption="Upload car json file",
                directory=self.acc_cars_dir,
                filter=".json(*)",
            )
        self.check_file(self.file)
        
    def check_file(self, file):
        if not file.endswith('json') and bool(file):
            self.msg.setWindowTitle("Wrong file type!")
            self.msg.setIcon(QMessageBox.Critical)
            self.msg.setText("Not a .json file!")
            self.msg.exec_()
            FileHandler(self.widget)
        else:
            return file
    
    def check_files(self, files):
        png_cnt, dds_cnt = 0, 0
        for file in files:
            print(file)
            if file.endswith(".png"):
                png_cnt += 1
            if file.endswith(".dds"):
                 dds_cnt += 1
        print(png_cnt, dds_cnt)
        if png_cnt*2 != dds_cnt and png_cnt == 2:
            self.msg.setWindowTitle("Missing .dds files!")
            self.msg.setIcon(QMessageBox.Critical)
            self.msg.setText("Missing .dds files!")
            self.msg.exec_()
            FileHandler(self.widget)
        else:
            return files