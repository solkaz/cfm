# `cfm`

`cfm` is a config file manager written in Python 3. 

## Installation

* Clone this repo 

* Add the `cfm` file to your `$PATH`.

## Usage

`cfm` utilizes aliases that are mapped to your config files' file paths. The alias `foo`, for example, can be mapped to `~/.foorc`.
You can then call `cfm edit foo` to edit the file that `foo` points to.

The `~.cfm` file that `cfm` uses is in JSON format, and should be placed in your `$HOME` directory. 

### Available commands

`cfm add`

Add an alias to your `.cfm` file

`cfm list`

List all of your saved aliases and the files they point to. Can specify an arbitrary number of aliases to list

`cfm search`

Search through your saved aliases.

`cfm rm`

Remove an alias from your saved aliases

`cfm mv`

Rename an alias

`cfm edit`

Open the alias' config file with your editor of choice

`cfm remap`

Change the file path that an alias refers to.

`cfm check`

Check that the file an alias points to exists. Can specify an arbitrary number of aliases to check

## Roadmap
1. More support for different versions of Python; currently only tested on Python 3.5.2
2. Cross-platform support. Built on Xubuntu 16.04; probably will not work with Windows
3. Look for config files in default locations
4. VCS integration