from PyQt5.QtWidgets import (
    QFileDialog,
    QMessageBox,
    QMainWindow
)
from dataclasses import dataclass
import json
import os

@dataclass
class FilesStorage():
    pass

class FileHandler():
    def __init__(self, widget: QMainWindow, livery_files: list, car_file: str) -> None:
        self.file_handler = QFileDialog()

        # variables
        self.car_file = car_file
        self.livery_files = livery_files

        # strings
        self.acc_str = "Assetto Corsa Competizione"
        self.documents_str = "Documents"
        self.livery_str = r"Customs\Liveries"
        self.car_str = r"Customs\Cars"

        self.msg = QMessageBox()
        self.window = widget
        self.file_ext = [".png", ".json", ".dds"]
        self.root_dir = os.path.expanduser("~")
        self.acc_livery_dir = os.path.join(self.root_dir, self.documents_str, self.acc_str, self.livery_str)
        self.acc_car_dir = os.path.join(self.root_dir, self.documents_str, self.acc_str, self.car_str)

        if not os.path.isdir(self.acc_car_dir):
            self.acc_cars_dir = os.path.join(self.root_dir, self.documents_str)
        if not os.path.isdir(self.acc_livery_dir):
            self.acc_livery_dir = os.path.join(self.root_dir, self.documents_str)

    def add_livery_files(self):
        self.livery_files, _ = self.file_handler.getOpenFileNames(
            parent=self.window,
            caption="Upload livery files",
            directory=self.acc_livery_dir,
            filter="Livery .png, .dds and .json(*)")
        self.livery_files = [file for file in self.livery_files if file.endswith(tuple(self.file_ext))]
        self.livery_files = list(set(self.livery_files))

        png_count, dds_count = 0, 0
        for file in self.livery_files:
            if file.endswith(".png"):
                png_count += 1
            if file.endswith(".dds"):
                dds_count += 1
        if png_count * 2 != dds_count and png_count == 2:
            self.msg.setWindowTitle("Missing .dds files!")
            self.msg.setIcon(QMessageBox.Critical)
            self.msg.setText("Missing .dds files!")
            self.msg.resize(500, 500)
            self.msg.exec_()
            return []
        else:
            return self.livery_files

    def add_car_file(self):
        self.car_file, _ = self.file_handler.getOpenFileName(
            parent=self.window,
            caption="Upload car json file",
            directory=self.acc_cars_dir,
            filter=".json(*)")

        if not self.car_file.endswith('json') and self.car:
            self.msg.setWindowTitle("Wrong file type!")
            self.msg.setIcon(QMessageBox.Critical)
            self.msg.setText("Not a .json file!")
            self.msg.resize(200, 200)
            self.msg.exec_()
            return False

        if self.car_file != "":
            with open(self.car_file, 'r') as f:
                data = f.read()
            json_data = json.loads(data.encode("utf-8"))
            skin_name = json_data["customSkinName"]
            folder = self.livery_files[0].split('/')[-2]

            if folder != skin_name:
                self.msg.setWindowTitle("Car.json mismatch!")
                self.msg.setIcon(QMessageBox.Critical)
                self.msg.setText("Car.json file does not match livery folder!")
                self.msg.resize(200, 200)
                self.msg.exec_()
            return self.car_file
