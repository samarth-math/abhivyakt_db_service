import requests

r = requests.get('http://127.0.0.1:5000/kavita?title=क')
print(r.status_code)
print(r.headers['content-type'])
print(r.json())
js = r.json()
data = js.get('data')
print(type(data))
print(len(data))

#r = requests.get('http://127.0.0.1:5000/kavita?title=क&nextItem=5a53082474ad350ba00ae83a')
#print(r.status_code)
#print(r.headers['content-type'])
#print(r.json())
#js = r.json()
#data = js.get('data')
#print(type(data))
