import json


class Conf():
    def __init__(self, rce_handler):
        # Extract the contents of the .rce file
        file_contents = rce_handler.load_file_contents()

        try:
            self.configs = json.loads(file_contents)
        except ValueError as err:
            print(err)
            raise ValueError('Invalid JSON format; exiting')

    def ListAliases(self):
        for alias, file_path in self.configs['aliases'].items():
            print(alias + ' -> ' + file_path)
