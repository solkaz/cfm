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
            raise ValueError('invalid JSON format; exiting')

    def DoesAliasExist(self, alias_phrase):
        return alias_phrase in self.aliases

    def ListAliases(self, alias_phrase):
        if alias_phrase is None:
            sorted_aliases = utils.make_sorted_dict(self.aliases)
            for alias, file_path in sorted_aliases.items():
                utils.print_alias(alias, file_path)
        elif self.DoesAliasExist(alias_phrase):
            utils.print_alias(alias_phrase, self.aliases[alias_phrase])
        else:
            utils.print_does_not_exist(alias_phrase)
            # TODO: offer to add alias

    def Search(self, search_phrase):
        matched_keys = []
        for alias in self.aliases:
            if search_phrase in alias:
                matched_keys.append(alias)

        if matched_keys:
            for key in matched_keys:
                utils.print_alias(key, self.aliases[key])

        else:
            print('no aliases matched')

    def Rename(self, old_alias, new_alias):
        if not self.DoesAliasExist(old_alias):
            utils.print_does_not_exist(old_alias)
            # TODO: offer to add alias
        else:
            if not old_alias == new_alias:
                self.aliases[new_alias] = self.aliases.pop(old_alias)
                print('renaming ' + old_alias + ' to ' + new_alias)
                # Save to .rce file
                self.rce_handler.save_to_file(self.PrepForSave())
            else:
                print('aliases are the same')

    def PrepForSave(self):
        return dict(
            default_editor=self.default_editor,
            aliases=self.aliases
        )
