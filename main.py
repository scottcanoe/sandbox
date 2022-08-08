import os
from pathlib import Path
import sys

import click

PACKAGES = (
    "filesystem",
    "motion_correction",
    "segmentation",
    "gui",
)


class Installer:
    def __init__(self):
        self.to_install = []
        self.userdir = None
        self.filesystems = []


@click.command()
@click.argument("args", nargs=-1)
# @click.option('--all', '-a', default=None, help='Install all packages.')
# @click.option("--packages", multiple=True, default=["filesystem", "motion_correction", "segmentation"])
def install(args, **kw):
    """Simple program that greets NAME for a total of COUNT times."""
    print('install')
    s = "args: " + repr(args)
    click.echo(s)
    s = "kw: " + ", ".join([f"{key}={val}" for key, val in kw.items()])
    click.echo(s)




@click.group()
def cli():
    pass

@click.command()
def initdb():
    click.echo('Initialized the database')

@click.command()
def dropdb():
    click.echo('Dropped the database')

cli.add_command(initdb)
cli.add_command(dropdb)


if __name__ == '__main__':
    installer = Installer()
    install()
