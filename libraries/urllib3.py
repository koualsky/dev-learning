import urllib3

http = urllib3.PoolManager()
r = http.request('GET', 'https://www.onet.pl')
print(r.status)
print(r.data)