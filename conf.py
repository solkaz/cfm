import utils

import json
import os.path
import subprocess


class Conf():
    def __init__(self, rce_handler):
        # Set the .rce file handler used for I/O
        self.rce_handler = rce_handler
        # Extract the contents of the .rce file
        file_contents = self.rce_handler.load_file_contents()

        try:
            configs = json.loads(file_contents)
            self.aliases = configs['aliases']
            self.editor = configs['editor']
        except ValueError as err:
            print(err)
            raise ValueError('invalid JSON format; exiting')

    def save(self):
        save_data = dict(
            editor=self.editor,
            aliases=self.aliases
        )
        self.rce_handler.save_to_file(save_data)

    def does_alias_exist(self, alias_phrase):
        return alias_phrase in self.aliases

    def handle_does_not_exist(self, alias_phrase):
        utils.print_does_not_exist(alias_phrase)
        self.offer_add(alias_phrase)

    def offer_add(self, alias):
        alias_file_path = utils.offer_to_add(alias)

        # User chose to add the alias and entered a file_path
        if alias_file_path is not None:
            self.add_alias(alias, alias_file_path)

    def add(self, alias_to_add, file_path):
        # Check that the alias already exists
        if self.does_alias_exist(alias_to_add):
            print("alias {0} already exists at {1}".format(
                alias_to_add, self.get_file_path(alias_to_add)
            ))
            # TODO: offer to remap file or to specify a new alias
        else:
            print('adding {0} at {1}'.format(
                alias_to_add, file_path
            ))
            self.aliases[alias_to_add] = file_path
            self.save()

    def rm(self, alias_to_remove, force=False):
        # Check that the alias does exist
        if self.does_alias_exist(alias_to_remove):
            if not force and not utils.confirm_rm(alias_to_remove):
                return
            del self.aliases[alias_to_remove]
            self.save()
            if not force:
                print("{0} removed".format(alias_to_remove))
        elif not force:
            print('{0} does not exist'.format(alias_to_remove))

    def list(self, alias_phrase):
        if alias_phrase is None:
            sorted_aliases = utils.make_sorted_dict(self.aliases)
            for alias, file_path in sorted_aliases.items():
                utils.print_alias(alias, file_path)
        elif self.does_alias_exist(alias_phrase):
            utils.print_alias(alias_phrase, self.aliases[alias_phrase])
        else:
            self.handle_does_not_exist(alias_phrase)

    def search(self, search_phrase):
        matched_keys = []
        for alias in self.aliases:
            if search_phrase in alias:
                matched_keys.append(alias)

        if matched_keys:
            for key in matched_keys:
                utils.print_alias(key, self.aliases[key])
        else:
            print('no aliases matched for {0}'.format(search_phrase))
            self.offer_add(search_phrase)

    def mv(self, old_alias, new_alias):
        if not self.does_alias_exist(old_alias):
            self.handle_does_not_exist(old_alias)
        else:
            if not old_alias == new_alias:
                self.aliases[new_alias] = self.aliases.pop(old_alias)
                print('renaming {0} to {1}'.format(old_alias, new_alias))
                self.save()
            else:
                print('aliases are the same')

    def edit(self, alias):
        if self.does_alias_exist(alias):
            file_path = self.get_file_path(alias)
        else:
            self.handle_does_not_exist(alias)
            return

        exec_cmd = [
            self.editor['command'],
            *self.editor['flags'],
            file_path
        ]
        try:
            subprocess.run(exec_cmd)
        except Exception as err:
            print(err)

    def get_file_path(self, alias):
        return os.path.expanduser(self.aliases[alias])
