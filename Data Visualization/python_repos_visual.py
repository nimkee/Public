import requests
import plotly.express as px

# Make an API call and check the response

url = 'https://api.github.com/search/repositories'
url += '?q=language:python+sort:stars+stars:>10000'

headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f'Status code: {r.status_code}')

# Convert the response object to a dictionary
response_dict = r.json() # json() is a method being used on the request object r

# Process results
print(response_dict.keys())
# print(response_dict.values())

print(f'Total repositories: {response_dict['total_count']}')
print(f'Complete results: {not response_dict['incomplete_results']}')

# Process repository information
repo_dicts = response_dict['items'] # Create a list of the repo dictionaries

repo_links, stars, hover_texts = [], [], []

for repo_dict in repo_dicts:
    # Turn repo names into active links
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name},</a>"
    repo_links.append(repo_link)

    stars.append(repo_dict['stargazers_count'])

    # Build hover texts
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)

# Make visualization
title = "Most-Starred Python Projects on GitHub"
labels = {'x': 'Repository', 'y': 'Stars'}


fig = px.bar(x=repo_links, y=stars, title=title, labels=labels, hover_name=hover_texts)
fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)
fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6,
                  hovertemplate="<b>Value:</b> %{y}<br><b>URL:</b> <font color='black'><a href='%{x}'>%{x}</a></font>")
                    # The hovertemplate code above does not seem to work
fig.show()
