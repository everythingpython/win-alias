# Win-Alias

Win-Alias is a simple CLI tool to create and manage Windows command aliases.

## Features

- Create custom command aliases
- List all created aliases
- Display usage instructions

## Requirements

- Python 3.11 or higher
- `click` library
- `colorama` library

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/win-alias.git
    cd win-alias
    ```

2. Install dependencies:
    ```sh
    pip install flit
    flit install --deps=all
    ```

## Usage

### Create an Alias

To create a new alias, run:
```sh
python -m win_alias create-alias