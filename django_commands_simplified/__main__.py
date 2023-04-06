import argparse
from .commands import startproject, startapp, runserver, makemigrations, migrate, createsuperuser, collectstatic, shell, test

parser = argparse.ArgumentParser(description='Django Commands Simplified')

parser.add_argument('command', choices=[
                    'startproject', 'startapp', 'runserver', 'makemigrations', 'migrate', 'createsuperuser', 'collectstatic', 'shell', 'test'], help='The command to run')

args = parser.parse_args()

if args.command == 'startproject':
    startproject()
elif args.command == 'startapp':
    startapp()
elif args.command == 'runserver':
    runserver()
elif args.command == 'makemigrations':
    makemigrations()
elif args.command == 'migrate':
    migrate()
elif args.command == 'createsuperuser':
    createsuperuser()
elif args.command == 'collectstatic':
    collectstatic()
elif args.command == 'shell':
    shell()
elif args.command == 'test':
    test()
