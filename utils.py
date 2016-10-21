import collections


def print_alias(alias, file_path):
    print(alias + ' -> ' + file_path)


def print_does_not_exist(alias):
    print('Alias ' + alias + ' does not exist')


def prompt_user(prompt):
    resp = input(prompt + ' [y/n]: ').lower()
    while resp not in ['y', 'n']:
        resp = input("Please answer [y/n]: ")
    return resp == 'y'


def offer_to_add(alias):
    if prompt_user('Do you want to add ' + alias + '?'):
        file_path = input("Enter the path to the file that " + alias
                          + ' points to: ')
        return file_path


def confirm_rm(alias):
    return prompt_user('Remove ' + alias + '?')


def make_sorted_dict(unordered):
    # Create an OrderedDict from a regular dict
    # It will be sorted by the key's values
    return collections.OrderedDict(
        sorted(unordered.items(), key=lambda t: t[0])
    )
