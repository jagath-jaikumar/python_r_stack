import requests

## CALLING R
print ("CALLING R FUNCTIONS: ~~~")
#################################
#### Example GET

endpoint_get ="http://localhost:8000/echo"

payload = {'msg':'hello'}

r = requests.get(endpoint_get, params=payload)

print(r.text)

#expect "hello"

#################################
#### Example POST


endpoint_post="http://localhost:8000/sum"

data = {"a":"2","b":"3"}

r = requests.post(endpoint_post, json=data)

print(r.text)

# expect "5"



## CALLING PYTHON
print()
print ("CALLING PYTHON FUNCTIONS: ~~~")
#################################
#### Example GET

endpoint_get ="http://localhost:5000/echo"

payload = {'msg':'hello'}

r = requests.get(endpoint_get, params=payload)

print(r.text)

#expect "hello"

#################################
#### Example POST


endpoint_post="http://localhost:5000/sum"

data = {"a":"2","b":"3"}

r = requests.post(endpoint_post, json=data)

print(r.text)

# expect "5"
