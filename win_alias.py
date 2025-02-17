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
def create_alias(alias_name):
    """Create a batch alias that supports multiline commands."""

    print("Enter the command (press Enter for a new line, type 'EOF' on a new line to finish):")

    # Read multiline input until the user types "EOF"
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "EOF":
            break
        lines.append(line)

    os.makedirs(alias_dir, exist_ok=True)

    # Save to a batch file
    alias_path = os.path.join(alias_dir, f"{alias_name}.bat")
    with open(alias_path, "w") as f:
        f.write("@echo off\n")
        f.write("\n".join(lines))  # Write multiline command

    print(f'{Fore.GREEN}Alias "{alias_name}" created successfully!{Style.RESET_ALL}')
    print(
        Fore.YELLOW + "If this is your first time creating an alias, add the folder to your PATH environment variable.")


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
