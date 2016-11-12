import argparse


def new_parser():
    parser = argparse.ArgumentParser(
        description="config file manager",
    )

    subparsers = parser.add_subparsers(
        dest='subcommand',
        help='available subcommands'
    )

    # list subcommand
    list_parser = subparsers.add_parser(
        'list',
        help="list the alias' mappings in the .cfm file or a specific one"
    )

    list_parser.add_argument(
        'aliases',
        nargs='*',
        default=[],
        help="alias of the config file to show"
    )

    # search subcommand
    search_parser = subparsers.add_parser(
        'search',
        help='search the aliases stored in the .cfm file'
    )
    search_parser.add_argument(
        'alias',
        help='phrase to search against'
    )

    # add subcommand
    add_parser = subparsers.add_parser(
        'add',
        help='add an alias to the .cfm file'
    )

    add_parser.add_argument(
        'alias',
        help="alias of the config file to add "
    )

    add_parser.add_argument(
        'file_path',
        help='file path to the config file'
    )

    # rm subcommand
    rm_parser = subparsers.add_parser(
        'rm',
        help='remove an alias'
    )

    rm_parser.add_argument(
        'alias',
        help='config file alias to remove'
    )

    rm_parser.add_argument(
        '-f', '--force',
        action='store_true',
        help='do not prompt for removal'
    )

    # remap subcommand
    remap_parser = subparsers.add_parser(
        'remap',
        help='remap an alias to another config file location'
    )
    remap_parser.add_argument(
        'alias',
        help='alias to remap'
    )
    remap_parser.add_argument(
        'new_file_path',
        help='new file path that ali'
    )

    # edit subcommand
    edit_parser = subparsers.add_parser(
        'edit',
        help='edit a config file'
    )

    edit_parser.add_argument(
        'alias',
        help="alias of the config file to edit"
    )

    edit_parser.add_argument(
        '-e', '--editor',
        nargs='*',
        dest="editor",
        help="specifies which editor command to use"
    )

    # mv subcommand
    mv_parser = subparsers.add_parser(
        'mv',
        help='rename an alias'
    )

    mv_parser.add_argument(
        'old_alias',
        help="alias' old name"
    )

    mv_parser.add_argument(
        'new_alias',
        help="alias' new name"
    )

    # check subcommand
    check_parser = subparsers.add_parser(
        'check',
        help='check that the file associated with a specified alias exists'
    )

    check_parser.add_argument(
        'alias',
        help='alias of the file to check'
    )

    # Help subcommand
    subparsers.add_parser(
        'help',
        help='show this help message',
    )

    return parser
