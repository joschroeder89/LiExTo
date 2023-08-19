from PyQt5.QtWidgets import (
    QFileDialog,
    QMessageBox,
    QMainWindow
)
import json
import os

class FileHandler():
    def __init__(self, widget: QMainWindow, file_type: str) -> None:
        self.file_handler = QFileDialog()

        # self.file_handler.setFileMode(QFileDialog.AnyFile)
        self.file = ""
        self.files = []
        self.folder = ""

        # self.widget = widget
        self.msg = QMessageBox()
        self.file_ext = [".png", ".json", ".dds"]
        self.root_dir = os.path.expanduser("~")
        self.acc_livery_dir = os.path.join(
            self.root_dir,
            "Documents",
            "Assetto Corsa Competizione",
            r"Customs\Liveries")

        self.acc_cars_dir = os.path.join(
            self.root_dir,
            "Documents",
            "Assetto Corsa Competizione",
            r"Customs\Cars")

        if file_type == "liveries":
            print(file_type)
            self.files, _ = self.file_handler.getOpenFileNames(
                parent=widget,
                caption="Upload livery files",
                directory=self.acc_livery_dir,
                filter="Livery .png, .dds and .json(*)",
            )
            self.files = [file for file in self.files if file.endswith(tuple(self.file_ext))]

        if file_type == "cars":
            print(file_type)
            self.file, _ = self.file_handler.getOpenFileName(
                parent=widget,
                caption="Upload car json file",
                directory=self.acc_cars_dir,
                filter=".json(*)",
            )
            # self.check_file(self.file)

    def check_file(self, files):
        print(files, self.file)
        if not self.file.endswith('json') and len(self.file):
            self.msg.setWindowTitle("Wrong file type!")
            self.msg.setIcon(QMessageBox.Critical)
            self.msg.setText("Not a .json file!")
            self.msg.resize(200, 200)
            self.msg.exec_()

        if self.file != "":
            with open(self.file, 'r') as f:
                data = f.read()
            json_data = json.loads(data.encode("utf-8"))
            skin_name = json_data["customSkinName"]
            folder = files[0].split('/')[-2]
            if folder != skin_name:
                self.msg.setWindowTitle("Car.json mismatch!")
                self.msg.setIcon(QMessageBox.Critical)
                self.msg.setText("Car.json file does not match livery folder!")
                self.msg.resize(200, 200)
                self.msg.exec_()
            print(self.file)
            return self.file

    def check_files(self):
        png_cnt, dds_cnt = 0, 0
        for file in self.files:
            print(file)
            if file.endswith(".png"):
                png_cnt += 1
            if file.endswith(".dds"):
                dds_cnt += 1
        if png_cnt * 2 != dds_cnt and png_cnt == 2:
            self.msg.setWindowTitle("Missing .dds files!")
            self.msg.setIcon(QMessageBox.Critical)
            self.msg.setText("Missing .dds files!")
            self.msg.resize(500, 500)
            self.msg.exec_()
            return []
            # FileHandler(self.widget, "liveries")
        else:
            return self.files
