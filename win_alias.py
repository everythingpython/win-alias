import os
from colorama import Fore, Back, Style
import click

home_dir = os.path.expanduser('~')
alias_dir = os.path.join(home_dir, 'aliases')
os.makedirs(alias_dir, exist_ok=True)


@click.group()
def cli():
    """CLI tool for managing Windows command aliases."""


# Command to create alias
@cli.command()
@click.option('--alias_name', prompt='Enter the alias name')
@click.option('--command', prompt='Enter the command')
def create_alias(_alias_name, _command):
    with open(f'{os.path.join(alias_dir, _alias_name)}.bat', 'w') as f:
        f.write(f'@echo off\n{_command}')
    print(f'{Fore.GREEN}Alias created successfully{Style.RESET_ALL}')
    print(Fore.GREEN + "If this is your first time creating an alias,"
                       " add the folder to your PATH environment variable.")


# Command to get all aliases
@cli.command()
def get_aliases():
    """List all created aliases."""
    aliases = os.listdir(alias_dir)
    if not aliases:
        print(f"{Fore.RED}No aliases found.{Style.RESET_ALL}")
    else:
        print(f"{Fore.BLUE}Existing aliases:{Style.RESET_ALL}")
        for alias in aliases:
            print(f" - {alias}")


# Show help message explicitly
@cli.command()
def guide():
    """Display usage instructions."""
    print(Fore.GREEN + "Usage Guide:")
    print(f" - {Fore.YELLOW}To create an alias:{Style.RESET_ALL} `python script.py create-alias`")
    print(f" - {Fore.YELLOW}To list all aliases:{Style.RESET_ALL} `python script.py get-aliases`")


if __name__ == '__main__':
    cli()
