import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    #print('Retrieving', url)
    uh = urllib.request.urlopen(address, context=ctx)

    data = uh.read()
    #print('Retrieved', len(data), 'characters')
    #print(data.decode())
    data = data.decode()
    tree = ET.fromstring(data)
    sum = 0
    results = tree.findall('.//count')
    for x in results:
        sum += int(x.text)
    print(sum)
