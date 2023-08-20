import dropbox
import dropbox.sharing
import os

class DropboxHandler:
    def __init__(self, api_token):
        self.dropbox_api_token = api_token
        self.dbx = dropbox.Dropbox(self.dropbox_api_token)
        self.link_settings = dropbox.sharing.SharedLinkSettings(
            allow_download=True
        )

    def get_sharelink(self, path):
        return self.dbx.sharing_create_shared_link_with_settings(f"/{path}", self.link_settings)

    def init_sharefolder(self, path):
        self.dbx.files_create_folder(f"/{path}")
        self.dbx.files_create_folder(f"/{path}/Liveries")
        self.dbx.files_create_folder(f"/{path}/Cars")

    def get_sharefolder(self):
        return
