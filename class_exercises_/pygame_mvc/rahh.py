import requests
response = requests.get('https://api.themoviedb.org/3/search/movie',
                        params={'query': 'Inception', 'api_key': 'YOUR_KEY'})
print(response.json())