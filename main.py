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
    else:
        # Help message will be printed if 'help' is inputted OR
        # if there was no subcommand inputted
        rceParser.print_help()

if __name__ == "__main__":
    main()
