import requests

api_key = "DafMSc1I0gqVGMuZaa1V9Nl0FFTgzPXVgy42Ee4%2BF9G0X8EP6gpzRv2zoIxj72aTkl%2BUFHZIaO%2F0%2Fn9cVWxwVQ%3D%3D"

api_key_decode = requests.utils.unquote(api_key)

parameters = {"ServiceKey":api_key_decode, "numOfROws":10, "pageNo":1}

req = requests.get(url, params = parameters)