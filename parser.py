import argparse


def new_parser():
    parser = argparse.ArgumentParser(
        description="Config file manager",
    )

    subparsers = parser.add_subparsers(
        dest='subcommand',
        help='Available rce subcommands'
    )

    # List subcommand
    list_parser = subparsers.add_parser(
        'list',
        help='list aliases'
    )

    list_parser.add_argument(
        'ALIAS',
        nargs='?',
        default=None,
        help=("list the ALIAS' mappings to " +
              "their config file path")
    )

    # Search subcommand
    search_parser = subparsers.add_parser(
        'search',
        help='search aliases'
    )
    search_parser.add_argument(
        'ALIAS',
        help='alias to search for'
    )

    add_parser = subparsers.add_parser(
        'add',
        help='add an alias'
    )

    add_parser.add_argument(
        'ALIAS',
        help="config file's alias"
    )

    add_parser.add_argument(
        'file_path',
        help='file path to the config file'
    )

    rm_parser = subparsers.add_parser(
        'rm',
        help='remove an alias'
    )

    rm_parser.add_argument(
        'ALIAS',
        help='config file alias to remove'
    )

    rm_parser.add_argument(
        '-f', '--force',
        action='store_true',
        help='do not prompt for removal'
    )

    # TODO: Implement 'remap' subcommand

    edit_parser = subparsers.add_parser(
        'edit',
        help='edit a config file'
    )

    edit_parser.add_argument(
        'ALIAS',
        help="alias of the config file to edit"
    )

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

    check_parser = subparsers.add_parser(
        'check',
        help='check that the file associated with an alias exists'
    )

    check_parser.add_argument(
        'ALIAS',
        help='alias to check'
    )

    # Help subcommand
    subparsers.add_parser(
        'help',
        help='show this help message',
    )

    return parser
