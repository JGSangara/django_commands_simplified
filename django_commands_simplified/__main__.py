import argparse
from .commands import runserver, migrate

parser = argparse.ArgumentParser(description='My Command-Line Tool')

parser.add_argument('command', choices=[
                    'runserver', 'migrate'], help='The command to run')

args = parser.parse_args()

if args.command == 'runserver':
    runserver()
elif args.command == 'migrate':
    migrate()
