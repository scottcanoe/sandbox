import os
from pathlib import Path
import sys

class Installer:

    def __init__(self):
        self.to_install = []
        self.userdir = None
        self.filesystems = []

executable = Path(sys.executable)
envdir = executable.parent.parent
mambadir = envdir.parent.parent


