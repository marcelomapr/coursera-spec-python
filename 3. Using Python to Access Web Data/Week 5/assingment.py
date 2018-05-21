import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

while True:
    url = input('Enter URL: ')

    if len(url) < 1: break

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read()

    print('Retrieved', len(data), 'characters')
    print(data.decode())

    tree = ET.fromstring(data)

    counts = tree.findall('.//count')

    print(len(counts))

    total = 0

    for c in counts:
        total = total + int(c.text)

    print(total)
