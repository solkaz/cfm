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

    def HandleDoesNotExist(self, alias_phrase):
        utils.print_does_not_exist(alias_phrase)
        self.OfferToAdd(alias_phrase)

    def OfferToAdd(self, alias):
        alias_file_path = utils.offer_to_add(alias)

        # User chose to add the alias and entered a file_path
        if alias_file_path is not None:
            self.AddAlias(alias, alias_file_path)

    def AddAlias(self, alias_to_add, file_path):
        # Check that the alias already exists
        if self.DoesAliasExist(alias_to_add):
            print('alias ' + alias_to_add + " already exists at "
                  + self.aliases[alias_to_add])
            # TODO: offer to remap file or to specify a new alias
        else:
            self.aliases[alias_to_add] = file_path
            print('adding ' + alias_to_add + ' at ' + file_path)
            # Save to .rce file
            self.rce_handler.save_to_file(self.PrepForSave())

    def RemoveAlias(self, alias_to_remove, force=False):
        # Check that the alias does exist
        if self.DoesAliasExist(alias_to_remove):
            if not force and not utils.confirm_rm(alias_to_remove):
                return
            del self.aliases[alias_to_remove]
            self.rce_handler.save_to_file(self.PrepForSave())
            if not force:
                print(alias_to_remove + " removed")
        elif not force:
            print(alias_to_remove + ' does not exist')

    def ListAliases(self, alias_phrase):
        if alias_phrase is None:
            sorted_aliases = utils.make_sorted_dict(self.aliases)
            for alias, file_path in sorted_aliases.items():
                utils.print_alias(alias, file_path)
        elif self.DoesAliasExist(alias_phrase):
            utils.print_alias(alias_phrase, self.aliases[alias_phrase])
        else:
            self.HandleDoesNotExist(alias_phrase)

    def Search(self, search_phrase):
        matched_keys = []
        for alias in self.aliases:
            if search_phrase in alias:
                matched_keys.append(alias)

        if matched_keys:
            for key in matched_keys:
                utils.print_alias(key, self.aliases[key])

        else:
            print('no aliases matched for ' + search_phrase)
            self.OfferToAdd(search_phrase)

    def Rename(self, old_alias, new_alias):
        if not self.DoesAliasExist(old_alias):
            self.HandleDoesNotExist(old_alias)
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
