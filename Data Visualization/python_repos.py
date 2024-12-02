import requests

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

# Explore information about the repositories

repo_dicts = response_dict['items'] # This is a list containing a number of repository dictionaries
print(f"Repositories returned: {len(repo_dicts)}")

print("\nSelected info about each repository:")
for repo_test in repo_dicts:

    print(f"Name: {repo_test['name']}")
    print(f"Owner: {repo_test['owner']['login']}")
    print(f"Stars: {repo_test['stargazers_count']}")
    print(f"Repository: {repo_test['html_url']}")
    print(f"Created: {repo_test['created_at']}")
    print(f"Updated: {repo_test['updated_at']}")
    print(f"Description: {repo_test['description']}\n")


