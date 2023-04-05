import subprocess


def startproject():
    subprocess.call('python manage.py startproject', shell=True)


def startapp():
    subprocess.call('python manage.py startapp', shell=True)


def runserver():
    subprocess.call('python manage.py runserver', shell=True)


def makemigrations():
    subprocess.call('python manage.py makemigrations', shell=True)


def migrate():
    subprocess.call('python manage.py migrate', shell=True)


def createsuperuser():
    subprocess.call('python manage.py createsuperuser', shell=True)


def collectstatic():
    subprocess.call('python manage.py collectstatic', shell=True)


def shell():
    subprocess.call('python manage.py shell', shell=True)


def test():
    subprocess.call('python manage.py test', shell=True)
