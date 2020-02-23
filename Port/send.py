import sys
from urllib import request, parse
import random

def get_as_output(server, port):
    url = f'http://{server}:{port}/calc'
    wload = {'inputs': '''{"a":'''+str(random.randint(1,60))+''',"b":'''+str(random.randint(1,60))+'''}'''}
    data = parse.urlencode(wload)
    data = data.encode()
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        resp = response.read()
        return resp.decode() #Converting bytes to str

if __name__ == '__main__':
    server = 'localhost'
    if len(sys.argv) != 2:
        print()
        print('Usage : \tpython test/get_auto_sizing.py port')
        print()
        sys.exit()
    port = sys.argv[1]
    for i in range(2000):
        result = get_as_output(server, port)
        print(result)
