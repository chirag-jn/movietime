from flask import Flask, render_template, request
import pymongo as pym
from scripts.recommender import user_user
from scripts.recommender import item_item
from scripts.recommender import lengthMovies

app = Flask(__name__)

length = 0
movies = []
myMovies = []

class node:
	def __init__(self, key1, key2, key3, key4, key5):
		self.movie = key1
		self.year = key2
		self.genre = key3
		self.imdbId = key4
		self.plot = key5

@app.route("/results", methods=['POST'])
def results():
	global movies
	global length
	# print(lengthMovies)
	answer1 = {}
	for i in range(lengthMovies):
		answer1[movies[i].imdbId] = request.form['rating_'+str(i+1)]
	user_user(answer1)
	return(request.form['rating_9'])

@app.route("/")
def home():
	global movies
	global length
	global myMovies

	movies = []
	for x in myMovies.find():
		temp = dict(x)
		p1 = node(temp['Title'], temp['Year'], temp['Genre'], temp['imdbId'], temp['Plot'])
		movies.append(p1)
	length = len(movies)
	# print(lengthMovies)
	return render_template('movies.html', data=movies)

if __name__ == "__main__":
	myClient = pym.MongoClient("mongodb://admin:Div%401234@movietimebot-shard-00-00-jttos.mongodb.net:27017,movietimebot-shard-00-01-jttos.mongodb.net:27017,movietimebot-shard-00-02-jttos.mongodb.net:27017/test?ssl=true&replicaSet=movietimebot-shard-0&authSource=admin&retryWrites=true")
	moviesDB = myClient["movietime"]
	myMovies = moviesDB["movies"]
	print(myMovies)
	app.run(debug=True)