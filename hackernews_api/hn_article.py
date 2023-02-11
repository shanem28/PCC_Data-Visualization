import requests
import json

# Make an API call
url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
r = requests.get(url)
print(f'status code:{r.status_code}')

# Explore the data structure
response_dict = r.json()
response_string = json.dumps(response_dict, indent=4)
print(response_string)

# Output the JSON in and indented format
readable_file = 'data/readable_hn_data.json'
with open(readable_file, 'w') as fn:
    json.dump(response_dict, fn, indent=4)
