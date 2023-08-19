import dropbox

from PyQt5.QtWidgets import  QFileDialog, QMessageBox, QWidget

class DropboxConfig:
    def __init__(self, api_token):
        self.drpbx_api_token = api_token
        print(self.drpbx_api_token)
        