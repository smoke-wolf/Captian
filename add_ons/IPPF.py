import time, run, requests, json, hashlib
from run import FIA

publishdate = ('5/29/2022')
author = ('SHADOW')


## definitions
name = 'IPPF'
choices = '1P 2P'

def men():
    print(
        f'''     
    |-------------------------------|
    | IP add-on for project Fia     |
    | ------------------------------|
    | 1P:: Whois                    |
    |-------------------------------|
    | 2P:: geoIP       				|
    |-------------------------------|  
    ''')
def can(choice):
    if choice in choices:
        pass
    else:
        raise ValueError('CC')


def assl(arg):
    if '1' in arg:
        modules.Whois(arg)
    elif '2' in arg:
        modules.geoIP(arg)

def VV():
    print("module is functional")

class modules:

    def Whois(arg):
        ipaddd = None
        print('if no input is given, process will use your own address for operation')
        ipaddd = input('target IP address: ')


        if ipaddd is not None:
            ipadd = (f'/json/{ipaddd}')
            response = requests.get(f"http://ip-api.com{ipadd}")
            json_response = json.loads(response.text)
            for key, value in json_response.items():
                if value:
                    print(f"{key.title()}: {str(value).strip()}")
                    time.sleep(1)
            time.sleep(2)
        else:
            print('No input detected')

    def geoIP(arg):
        ipadd = input('target IP address: ')
        response = requests.get(f"http://ipwhois.app/json/{ipadd}")
        json_response = json.loads(response.text)
        for key, value in json_response.items():
            if value:
                print(f"{key.title()}: {str(value).strip()}")