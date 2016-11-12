import collections


def does_file_exist(file_path):
    try:
        with open(file_path):
            pass
        return True
    except OSError:
        pass
    return False


def print_alias(alias, file_path):
    print('{0} -> {1}'.format(alias, file_path))


def print_does_not_exist(alias):
    print('Alias {0} does not exist'.format(alias))


def prompt_user(prompt):
    resp = input('{0} [y/n]: '.format(prompt)).lower()
    while resp not in ['y', 'n']:
        resp = input("Please answer [y/n]: ")
    return resp == 'y'


def offer_to_add(alias):
    if prompt_user('Do you want to add {0}?'.format(alias)):
        file_path = input("Enter the path to the "
                          "file that {0} points to: ".format(alias))
        return file_path


def create_cfm():
    return prompt_user('Create a default .cfm file at ~/.cfm?')


def confirm_rm(alias):
    return prompt_user('Remove {0}?'.format(alias))


def make_sorted_dict(unordered):
    # Create an OrderedDict from a regular dict
    # It will be sorted by the key's values
    return collections.OrderedDict(
        sorted(unordered.items(), key=lambda t: t[0])
    )
