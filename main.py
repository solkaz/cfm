#!/usr/bin/env python3.5

import conf
import json_handler
import parser

import sys


def main(user_args):

    # Parse the commandline args

    rceParser = parser.new_parser()
    args = rceParser.parse_args(user_args)

    subcommand = args.subcommand

    if subcommand == 'help' or not subcommand:
        # Help message will be printed if 'help' is inputted OR
        # if there was no subcommand inputted
        rceParser.print_help()

    else:
        # The subcommands below require data from the .rce file.
        # Extract the contents of it

        # TODO: load .rce file from different locations
        try:
            rce_file_handler = json_handler.JSONHandler()
        except OSError as err:
            print(err)
            quit()

        try:
            rce_config_man = conf.Conf(rce_file_handler)
        except ValueError as err:
            print(err)
            quit()

        if subcommand == "list":
            rce_config_man.ListAliases()
        elif subcommand == "search":
            print('search ' + args.alias)

if __name__ == "__main__":
    main(sys.argv[1:])
