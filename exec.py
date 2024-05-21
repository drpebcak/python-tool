#!/usr/bin/env python
import os
import subprocess


def main():
    # Create the parser
    command = os.environ["COMMAND"]
    command = command.split(" ")

    # Access the list of arguments
    print(f"Command to run: `{command}`")
    result = subprocess.run(command, capture_output=True, text=True)
    print(result.stdout)


if __name__ == "__main__":
    main()
