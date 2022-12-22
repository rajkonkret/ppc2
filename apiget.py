# get, post, put, delete
# http://api.nbp.pl/api/exchangerates/rates/{table}/{code}/
import requests as re

# pip install requests

response = re.get("http://api.nbp.pl/api/exchangerates/rates/A/USD/")
print(response)
# 200 - ok
# 4.. - błedy
# 5.. - wewewnetrzne błedy servera

table = response.json()
print(table)
print(table['table'])
print(table['rates'][0]['mid'])
