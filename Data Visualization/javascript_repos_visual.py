import requests
import plotly.express as px

# Make an API call and check the response

url = 'https://api.github.com/search/repositories'
url += '?q=language:javascript+sort:stars+stars:>10000'

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

repo_names, stars = [], []

for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# Make visualization

fig = px.bar(x=repo_names, y=stars)
fig.show()
