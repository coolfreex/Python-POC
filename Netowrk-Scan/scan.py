#only work on Linux like system, tested on kali
#usage sudo python3 scan.py ip xxx.txt
#example : sudo python3 scan.py 192.168.10.11 myscan.txt
#By mushroom

import os
import sys

target = sys.argv[1]
name = sys.argv[2]

def scan(ip, name):

    nmap_scan = f'nmap -Pn -sS --stats-every 3m --max-retries 1 --max-scan-delay 20 --defeat-rst-ratelimit -T4 -p1-65535 {ip} -oN {name}'
    print(f'Running command -----> {nmap_scan}')
    print('===================================')
    os.system(nmap_scan)
    command = "cat "+name+" | grep open | cut -f 1 -d ' ' | cut -f 1 -d '/' | awk '{printf(\"%s,\",$1)}'|sed 's/.$//'" + f">tmp_{name}"
    os.system(command)
    tmp_name=f'tmp_{name}'
    with open(tmp_name,mode='r') as f:
        data = f.read()
        print('\n')
        print(f'######open ports are ------> {data}#####'+ '\n')
    os.system(f'rm -rf {tmp_name}')
    os.system(f'rm -rf {name}')
    detail_scan = 'nmap -nvv -Pn -sSV -p '+ data+f' --version-intensity 9 -A -oN detail_{name} {ip}'
    print(f'Running command -----> {detail_scan}')
    print('===================================')
    os.system(detail_scan)
    print('\n')
    print('===================================')
    print(f'######ALL DONE, Please check detail_{name} with ip {ip}#####' + '\n')

def import_service(filename):
    checker = ["'open  http'", "'open  ftp'", "'net'"]
    print("checking important server.........." + '\n')
    print("checking if http,ftp,smb exists....." + '\n')
    for i in checker:
        #print(i)
        os.system(f'cat detail_{filename} | grep {i}')
    print('==============================')
    print(f'----------------Short Result:{target}-----------------')
    
    short = 'open  '
    os.system(f'cat detail_{filename} | grep {short} | grep -v Warning')


if __name__ == '__main__':
    scan(target, name)
    import_service(name)
