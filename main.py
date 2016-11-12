#!/usr/bin/env python3

import conf
import cfm_file
import parser
import utils

import sys


def main(user_args):

    # Parse the commandline args

    cfm_arg_parser = parser.new_parser()
    args = cfm_arg_parser.parse_args(user_args)

    subcommand = args.subcommand

    if subcommand == 'help' or not subcommand:
        # Help message will be printed if 'help' is inputted or
        # if there was no subcommand inputted
        cfm_arg_parser.print_help()

    else:
        # The subcommands below require data from the .cfm file.
        # Extract the contents of it

        # TODO: load .cfm file from different locations
        try:
            cfm_file_handler = cfm_file.CFMFile()
            cfm_file_handler.check_cfm_file()
            cfm_conf_man = conf.Conf(cfm_file_handler)
        except OSError as err:
            print(err)
            if utils.create_cfm():
                cfm_file_handler.make_default_cfm()
            quit()
        except ValueError as err:
            print(err)
            quit()

        if subcommand == "list":
            cfm_conf_man.list(args.aliases)
        elif subcommand == "search":
            cfm_conf_man.search(args.alias)
        elif subcommand == "mv":
            cfm_conf_man.mv(args.old_alias, args.new_alias)
        elif subcommand == "add":
            cfm_conf_man.add(args.alias, args.file_path)
        elif subcommand == "rm":
            cfm_conf_man.rm(args.alias, args.force)
        elif subcommand == "edit":
            cfm_conf_man.edit(args.alias, args.editor)
        elif subcommand == "check":
            cfm_conf_man.check(args.alias)
        elif subcommand == "remap":
            cfm_conf_man.remap(args.alias, args.new_file_path)


if __name__ == "__main__":
    main(sys.argv[1:])
