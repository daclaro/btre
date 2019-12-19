import json
userJSON='{"first_name":"John","second_name":"Lamber"}'
#parse to dict
user=json.loads(userJSON)
print(user)