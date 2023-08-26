import dropbox
import dropbox.sharing
from datetime import datetime
import os

class DropboxHandler:
    def __init__(self, api_token):
        self.dropbox_api_token = api_token
        self.dbx = dropbox.Dropbox(self.dropbox_api_token)
        self.link_metadata = dropbox.sharing

    def get_sharelink(self, path):
        self.link_settings = dropbox.sharing.SharedLinkSettings(
            allow_download=True
        )
        return self.dbx.sharing_create_shared_link_with_settings(f"/{path}", self.link_settings)

    def init_sharefolder(self, path):
        self.dbx.files_create_folder(f"/{path}")
        self.dbx.files_create_folder(f"/{path}/Liveries")
        self.dbx.files_create_folder(f"/{path}/Cars")

    def download_content(self, path):
        pass

    def upload_content(self, path):
        pass

    def check_folder_status(self, path):
        results = self.dbx.sharing_get_shared_links()
        folder_path = results.links[0]
        folders = self.dbx.files_list_folder(folder_path.path)
        dropbox_files = []
        for folder in folders.entries:
            files = self.dbx.files_list_folder(folder.path_lower)
            for file in files.entries:
                if type(file) == dropbox.files.FolderMetadata:
                    subfolder = self.dbx.files_list_folder(file.path_lower)
                    for subfiles in subfolder.entries:
                        dropbox_files.append(subfiles.path_lower)
                    continue
                dropbox_files.append(file.path_lower)
        print(dropbox_files)
