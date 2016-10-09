import collections


def print_alias(alias, file_path):
    print(alias + ' -> ' + file_path)


def print_does_not_exist(alias):
    print('Alias ' + alias + ' does not exist')


def make_sorted_dict(unordered):
    # Create an OrderedDict from a regular dict
    # It will be sorted by the key's values

    return collections.OrderedDict(
        sorted(unordered.items(), key=lambda t: t[0])
    )
