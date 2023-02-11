'''
Exercise 17-2
From Chaper 17 of Python Crash Course 2nd Edition by Eric Matthes
'''
from operator import itemgetter
import requests
import plotly.express as px

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

    short_title = response_dict['title'].split()
    short_title = " ".join(short_title[:5])
    short_title += '...'
    # Build a dictionary for each article
    submission_dict = {
        'full_title': response_dict['title'],
        'short_title': short_title,
        'link': f'http://news.ycombinator.com/item?id={submission_id}',
        'comments': response_dict['descendants'],
    }

    submission_dicts.append(submission_dict)

submission_dicts = sorted(
    submission_dicts, key=itemgetter('comments'), reverse=True)

links, comments, hover_texts = [], [], []
for submission in submission_dicts:
    hover_texts.append(
        f"{submission['full_title']}")
    links.append(
        f"<a href='{submission['link']}'>{submission['short_title']}</a>")
    comments.append(submission['comments'])

title = 'Most Commented Article on Hacker News Top Stories'
labels = {'x': 'Article', 'y': 'Comments'}
fig = px.bar(x=links, y=comments, title=title,
             labels=labels, hover_name=hover_texts)

fig.update_layout(title_font_size=28, xaxis_title_font_size=20,
                  yaxis_title_font_size=20)

fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)

fig.show()
