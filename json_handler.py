import json
import os.path


class JSONHandler():
    def __init__(self, file_path='~/.rce'):
        self.file_path = os.path.expanduser(file_path)
        if not self.does_file_exist():
            raise OSError(".rce file doesn't exist at " + file_path +
                          "; exiting")

    def does_file_exist(self):
        try:
            with open(self.file_path):
                pass
            return True
        except OSError:
            pass
        return False

    def load_file_contents(self):
        with open(self.file_path) as rce_file:
            file_contents = rce_file.read()
        return file_contents

    def save_to_file(self, save_data):
        with open(self.file_path, 'w', encoding='utf-8') as rce_file:
            json.dump(save_data, rce_file, ensure_ascii=False)
