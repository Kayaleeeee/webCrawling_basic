import requests
import webbrowser

search = 'Corona Virus'
queryString = {'q': search}
searchEngine = 'http://google.com/search'

res = requests.get(searchEngine, params=queryString)
webbrowser.open(res.url)
