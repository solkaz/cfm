import json
import os.path
import utils


class CFMFile():
    def __init__(self, file_path='~/.cfm'):
        self.file_path = os.path.expanduser(file_path)

    def check_cfm_file(self):
        if not utils.does_file_exist(self.file_path):
            raise OSError(".cfm file doesn't exist at " + self.file_path)

    def load_file_contents(self):
        with open(self.file_path) as cfm_file:
            file_contents = cfm_file.read()
        return file_contents

    def save_to_file(self, save_data):
        with open(self.file_path, 'w', encoding='utf-8') as cfm_file:
            json.dump(save_data, cfm_file, sort_keys=True,
                      indent=4, ensure_ascii=False)

    def make_default_cfm(self):
        default_data = {
            "aliases": {
                "cfm": "~/.cfm"
            },
            "editor": {
                "command": "vi",
                "flags": []
            }
        }
        self.save_to_file(default_data)
