import sys
import run
from run import FIA
import add_ons
from add_ons import *
import platform
import os
from add_ons import launcher

# mandatory do not remove, and limit to only essential, no install

imports = ('os', 'platform', 'sys', 'numpy', 'time', 'smtplib', 'socket', 'random')

ß = run.FIA
# global for run/mac/ .mod

mod_names = []

try:
    os.chdir('add_ons/')
    add_ons.launcher.Mod(mod_names)
    mod_names = None
except AttributeError:
    print('Package add_ons is depricated or damaged- install / download from github')


A = os.name
B = platform.system()
C = platform.release()

ß.import_test(imports)
ß._ø_(A, B, C)
