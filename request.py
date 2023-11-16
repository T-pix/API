import requests

link = 'https://primeira-api--tiagosoares6.repl.co/valortotal'

r = requests.get(link)
print(r)
print(r.json())