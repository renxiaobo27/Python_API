import requests
import json

url='http://127.0.0.1:5000/'

###post json  for text_search
data = {"query":"car wa","uid":"12345","time":"1491953263630","latitued":"40.741895","longitude":"-73.989308","service":"service1"}
res = requests.post(url+"api/text_search",json= data)
print res
print json.loads(res.content)

data = {"uid":"12345","time":"1491953263630","latitued":"40.741895","longitude":"-73.989308","service":"service1"}
res = requests.post(url+"api/service_predict",json= data)