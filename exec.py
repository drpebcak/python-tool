#!/usr/bin/env python
import os
import subprocess


def main():
    command = os.environ["COMMAND"]
    print(f"Command to run: `{command}`")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print("Error running command:", result.stderr)
    else:
        print(result.stdout)


if __name__ == "__main__":
    main()
