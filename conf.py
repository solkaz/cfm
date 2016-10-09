import utils

import json


class Conf():
    def __init__(self, rce_handler):
        # Set the .rce file handler used for I/O
        self.rce_handler = rce_handler
        # Extract the contents of the .rce file
        file_contents = self.rce_handler.load_file_contents()

        try:
            configs = json.loads(file_contents)
            self.aliases = configs['aliases']
            self.default_editor = configs['default_editor']
        except ValueError as err:
            print(err)
            raise ValueError('Invalid JSON format; exiting')

    def ListAliases(self):
        for alias, file_path in self.aliases.items():
            print(alias + ' -> ' + file_path)

    def Search(self, search_phrase):
        matched_keys = []
        for alias in self.aliases:
            if search_phrase in alias:
                matched_keys.append(alias)

        if matched_keys:
            for key in matched_keys:
                utils.print_alias(key, self.aliases[key])

        else:
            print('No aliases matched')
