'''
This script functions as one of the interaction points for LibbyDB.
'''

import argparse

def main():
    parser = argparse.ArgumentParser(description="Database Manager Entry Point")
    parser.add_argument('--mode', choices=['cli', 'gui'], default='cli',
                        help="Choose interface mode: 'cli' or 'gui' (default: cli)")
    args = parser.parse_args()

    if args.mode == "cli":
        import libbydb.cli as cli
        cli.main()
    elif args.mode == "gui":
        import libbydb.gui as gui
        gui.main()
    else:
        print("Unknown selection")

if __name__ == "__main__":
    main()
