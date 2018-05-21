import urllib.request, urllib.parse, urllib.error
import json

while True:
    url = input('Enter URL: ')

    if len(url) < 1: break

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read()

    info = json.loads(data)['comments']

    print('Entradas: ' + str(len(info)))

    total = 0

    for i in info:
      total = total + int(i['count'])

    print("Total: " + str(total))
