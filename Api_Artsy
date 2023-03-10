"""
В этой задаче вам необходимо воспользоваться API сайта artsy.net

API проекта Artsy предоставляет информацию о некоторых деятелях искусства, их работах, выставках.

В рамках данной задачи вам понадобятся сведения о деятелях искусства (назовем их, условно, художники).

Вам даны идентификаторы художников в базе Artsy.
Для каждого идентификатора получите информацию о имени художника и годе рождения.
Выведите имена художников в порядке неубывания года рождения. В случае если у художников одинаковый год рождения, выведите их имена в лексикографическом порядке.
"""




import requests
import json

artists_dict = {}

#нужно ввести клиент id и секрет

client_id = '____'
client_secret = '_____'

r = requests.post('https://api.artsy.net/api/tokens/xapp_token',
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret,
                  })

j = json.loads(r.text)

token = j['token']
headers = {"X-Xapp-Token": token}

# В строку ******** нужно ввести имя файла с которого будут считаны идентификаторы авторов

with open('********', 'r') as r:
    for artist in r:
        res = requests.get(f"https://api.artsy.net/api/artists/{artist.strip()}", headers=headers)
        res.encoding = 'utf-8'
        jes = json.loads(res.text)
        artists_dict[jes['sortable_name']] = jes['birthday']


artists_dict = sorted(artists_dict.items(), key=lambda x: (x[1], x[0]))
for artist in artists_dict:
    print(str(artist)[2: -10])
