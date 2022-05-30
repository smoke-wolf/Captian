from __future__ import print_function
import pathlib
from pathlib import Path
import time
# key assembly
import hashlib, ast
import add_ons.IPPF


format =  '{publishdate}{author}{totalfilelines}{totalwordcount}{totalcharactercount}{totalfunctionsinfile}'


def addkey(gen_key):
    keylist = 'keylist.txt'
    with open(keylist, 'a') as f:
        f.write((f'\n'))
        f.write(str(gen_key))
        print('key has been successfully added to file')
def Creation(post_post):
    DESSPEC = (f'add_ons.{post_post}')
    __import__(DESSPEC)

    d = 'publishdate'
    publishdate = getattr(__import__(DESSPEC, fromlist=[d]), d)
    c = 'author'
    author = getattr(__import__(DESSPEC, fromlist=[c]), c)

    carl = (f'{post_post}.py')

    with open(carl) as infile:
        words = 0
        characters = 0
        for lineno, line in enumerate(infile, 1):
            wordslist = line.split()
            words += len(wordslist)
            characters += sum(len(word) for word in wordslist)

    totalwordcount = words
    totalcharactercount = characters
    totalfilelines = lineno
    class FunctionCounter(ast.NodeVisitor):
        def __init__(self, filename):
            self.function_count = 0
            with open(filename) as f:
                module = ast.parse(f.read())
                self.visit(module)

        def visit_FunctionDef(self, node):
            self.function_count += 1

    counter = FunctionCounter(f'{post_post}.py')
    totalfunctionsinfile = counter.function_count

    key = (f'{publishdate}{author}{totalfilelines}{totalwordcount}{totalcharactercount}{totalfunctionsinfile}')
    gen_key = int(hashlib.sha256(key.encode('utf-8')).hexdigest(), 16) % 10 ** 50

    print(f'{gen_key} is bonded to {post_post}')
    add_ons.key_verification.ver(gen_key, post_post)

def ver(gen_key, post_post):

    key_list = Path('keylist.txt').read_text()

    if str(gen_key) in key_list:
        print(f'{post_post} is verified, and has a key of: {gen_key}')
        print('Thus module is trusted and will undergo completion tests')
        time.sleep(2)
        print(f'\n'*30)
    else:
        print(f"{post_post} has not yet had it's key verified: would you like to add the key to trusted modules, "
              f"this may open your laptop to security vulnerabilities? [1=yes]")
        c = input('>>> ')

        if c == '1':
            add_ons.key_verification.addkey(gen_key)
