#!/usr/bin/env python3.5

import parser


def main():

    # Parse the commandline args

    rceParser = parser.new_parser()
    args = rceParser.parse_args()

    subcommand = args.subcommand

    if subcommand == "list":
        print('list')
    elif subcommand == "search":
        print('search ' + args.alias)
    elif subcommand == "help":
        rceParser.print_help()

if __name__ == "__main__":
    main()
