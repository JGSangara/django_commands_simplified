from setuptools import setup, find_packages

setup(
    name="django commands simplified",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "startproject=commands:startproject",
            "startapp=commands:startapp",
            "runserver=commands:runserver",
            "makemigrations=commands:makemigrations",
            "migrate=commands:migrate",
            "createsuperuser=commands:createsuperuser",
            "collectstatic=commands:collectstatic",
            "shell=commands:shell",
            "test=commands:test",
        ],
    },
    install_requires=[
        "argparse",
    ],
    author="Josphat Gitogo Sangara",
    author_email="josphat.gitogo@gmail.com",
    description="""Django Commands Simplified is a Python package that provides
        simplified versions of common Django commands for managing your Django
        projects. With this tool, you can easily start the development server
        and run migrations without having to remember the full commands""",
    url="https://github.com/your-username/my-command-line-tool",
)
