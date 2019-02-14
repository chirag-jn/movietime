import requests

API_KEY = "8d3f0fb4"

OMDB_URL = "http://www.omdbapi.com/"

PARAMS = {'apikey':API_KEY}

def getData(imdbID):
	movieURL = OMDB_URL
	PARAMS["i"] = "tt" + imdbID
	jsonResponse = requests.get(url = movieURL, params = PARAMS)
	return jsonResponse.json()
