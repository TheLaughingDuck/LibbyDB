'''
Script that allows the package to be run with 'python -m libbydb'
'''

from . import cli
import argparse

def main():
    parser = argparse.ArgumentParser(description="Database Manager Entry Point")
    parser.add_argument('--mode', choices=['cli', 'gui'], default='cli',
                        help="Choose interface mode: 'cli' or 'gui' (default: cli)")
    args = parser.parse_args()

    if args.mode == "cli":
        print("Opening CLI...")
        cli.main()
    elif args.mode == "gui":
        from . import gui
        print("Opening GUI...")
        gui.main()
    else:
        print("Unknown selection")

if __name__ == "__main__":
    main()