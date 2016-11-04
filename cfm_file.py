import json
import os.path
import utils


class CFMFile():
    def __init__(self, file_path='~/.cfm'):
        self.file_path = os.path.expanduser(file_path)
        if not utils.does_file_exist(self.file_path):
            raise OSError(".rce file doesn't exist at " + file_path +
                          "; exiting")

    def load_file_contents(self):
        with open(self.file_path) as rce_file:
            file_contents = rce_file.read()
        return file_contents

    def save_to_file(self, save_data):
        with open(self.file_path, 'w', encoding='utf-8') as rce_file:
            json.dump(save_data, rce_file, sort_keys=True,
                      indent=4, ensure_ascii=False)
