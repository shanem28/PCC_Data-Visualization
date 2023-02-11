'''
Exercise 17-2
From Chaper 17 of Python Crash Course 2nd Edition by Eric Matthes
'''

import requests
import plotly.express as px

# Make an API call and check the response.
url = "https://api.github.com/search/repositories"
url += "?q=language:c+sort:stars+stars:>10000"

headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f'Status code: {r.status_code}')

# Process overall results
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")
print(f"Complete results: {not response_dict['incomplete_results']}")

# Process respository information
repo_dicts = response_dict['items']
repo_links, stars, hover_texts = [], [], []
for repo_dict in repo_dicts:
    # Turn repo names into active links.
    repo_name = repo_dict['name']
    repo_link = repo_dict['html_url']
    repo_links.append(f"<a href='{repo_link}'>{repo_name}</a>")

    stars.append(repo_dict['stargazers_count'])

    # Build hover text
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f'{owner}\n{description}'
    hover_texts.append(hover_text)

title = 'Most-Starred C Projects on GitHub'
labels = {'x': 'Repository', 'y': 'Stars'}
fig = px.bar(x=repo_links, y=stars, title=title,
             labels=labels, hover_name=hover_texts)

fig.update_layout(title_font_size=28, xaxis_title_font_size=20,
                  yaxis_title_font_size=20)

fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)

fig.show()
