from PyQt5.QtWidgets import (
    QFileDialog,
    QMessageBox,
    QWidget
)
import dropbox

class DropboxConfig:
    def __init__(self, api_token):
        self.dropbox_api_token = api_token
