# Win-Alias

Win-Alias is a simple CLI tool to create and manage Windows command aliases.

If you are tired of typing long commands or if you want to create custom command shortcuts, Win-Alias is for you.
If you've used Linux before, you might be familiar with the `alias` command. Win-Alias brings this functionality to Windows.

## Features

- Create custom command aliases
- List all created aliases
- Display usage instructions

## Installation

1. Install from pip
    ```sh
    pip install win-alias
    ```

## Usage

### Create an Alias

To create a new alias, run:
```sh
win_alias create-alias
```
```
>> Enter the alias name: ld 
>> Enter the command:
dir
EOF
```

- We can now use the alias `ld` to run the command `dir`.
- EOF is used to indicate the end of the command. It is not part of the command.


By default, the alias is saved in the user's home directory in a subdirectory called `aliases`. 
Each alias is saved in a separate batch file with the alias name as the filename.

**The very first time you create an alias, the `aliases` directory will need to be added to the system path. This is not needed for subsequent aliases.**

**The aliases will take effect after the system path is updated and the command prompt is restarted.**

### List All Aliases

To list all created aliases, run:
```sh
win_alias list-aliases
```

### Display Usage Instructions

To display usage instructions, run:
```sh
win_alias --help Or
win_alias guide
```