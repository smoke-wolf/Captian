import os.path, time, run.FIA

import add_ons.key_verification
from run.FIA import *
import subprocess
from subprocess import Popen, PIPE


def Mod(mod_names):
    print('checking for all available add-ons: ')
    files = filter(os.path.isfile, os.listdir(os.curdir))
    time.sleep(0.5)
    print(f'searching files in add-ons for compatibility (is properly configured): ')
    time.sleep(0.5)
    print(f'files in add_ons: {files}')
    time.sleep(2)
    print(f'\n'*30)
    for file in files:
        if 'PF' in file:
            print(f'{file}, is most likely compatible. running final tests')
            MEN = False
            word = (f'add_ons.{file}')
            post_word = word[:-3]
            post_post = file[:-3]
            try:
                try:
                    add_ons.key_verification.Creation(post_post)
                    KILO = True
                except:
                    KILO = False
                    pass
                try:
                    __import__(post_word)
                    car = (f'add_ons.{post_post}.VV()')
                    exec(car)
                    MEN = True
                except ImportError:
                    print('Module unable to import')

                print(f'{post_post} :: IS complete == query({MEN})')

                if MEN == True:
                    if KILO is True:
                        print(f'{post_post} is complete, would you like to import it? [1=yes]')
                        PL = int(input('>>> '))
                        if PL == 1:
                            try:
                                f = (f'from add_ons.{post_post} import *')
                                exec(f)
                                modules = post_post
                                run.FIA.val_check(modules)

                                print(f'successfully imported {post_post}')
                                print(f'\n'*30)

                            except ImportError:
                                pass
                        else:
                            pass
                    else:
                        print('module could not be trusted and was canceled')
                else:
                    pass
            except:
                print(f"An error occured during {post_post} check (modules were not installed, but cancled). -- re-trying with other file.")
                time.sleep(2)
                print(f'\n'*30)
        else:
            pass

def choice_check(choice):
    if run.FIA.TAN is not None:
        print(run.FIA.TAN)
        for word in run.FIA.TAN:
            try:
                str(choice)
                charlie = (f'add_ons.{word}.can(choice)')
                exec(charlie)

                arg = choice
                j = (f'add_ons.{word}.assl(arg)')
                exec(j)
                choice = None
                run.FIA.go_mod()

            except ValueError:
                pass
    else:
        pass



