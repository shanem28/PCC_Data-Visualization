'''
Hacker News API Calls 
From Chaper 17 of Python Crash Course 2nd Edition by Eric Matthes
'''
from operator import itemgetter
import requests

# Make an API call
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f'status code {r.status_code}')

# Process information about each submission
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    url = f'https://hacker-news.firebaseio.com/v0/item/{submission_id}.json'
    r = requests.get(url)
    print(f'id: {submission_id}\tstatus: {r.status_code}')
    response_dict = r.json()

    # Build a dictionary for each article
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f'http://news.ycombinator.com/item?id={submission_id}',
        'comments': response_dict['descendants'],
    }
    submission_dicts.append(submission_dict)
submission_dicts = sorted(
    submission_dicts, key=itemgetter('comments'), reverse=True)

for submission in submission_dicts:
    print(f"Title: {submission['title']}")
    print(f"Discussion Link: {submission['hn_link']}")
    print(f"Comments: {submission['comments']}\n")
