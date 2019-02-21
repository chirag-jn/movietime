import pymongo as pym
import csv

users =[]
movies = []

def setMovies():
	global movies
	with open('data/movieRatings/movieData.csv') as movies_file:
		movies_reader = csv.reader(movies_file, delimiter=',')
		line_count = 0
		tag1=''
		tag2=''
		tag3=''
		tag4=''
		tag5=''
		tag6=''
		tag7=''
		for row in movies_reader:
			if line_count == 0:
				tag1 = row[0]
				tag2 = row[1]
				tag3 = row[2]
				tag4 = row[3]
				tag5 = row[4]
				tag6 = row[5]
				tag7 = row[6]				
				line_count += 1
			else:
				tempDict = {tag1:row[0], tag2:row[1], tag3:row[2], tag4:row[3], tag5:row[4], tag6:row[5], tag7:row[6]}
				movies.append(tempDict)
				line_count += 1

def setDummyUsers():
	global users
	with open('data/movieRatings/ratings.csv') as movies_file:
		movies_reader = csv.reader(movies_file, delimiter=',')
		line_count = 0
		tag1=''
		tag2=''
		tag3=''
		for row in movies_reader:
			if line_count == 0:
				tag1 = row[0]
				tag2 = row[1]
				tag3 = row[2]
				line_count += 1
			else:
				tempDict = {tag1:row[0], tag2:row[1], tag3:row[2]}
				users.append(tempDict)
				line_count += 1

def setupDatabase():
	global users
	global movies
	myClient = pym.MongoClient("mongodb://localhost:27017")
	moviesDB = myClient["movietime"]
	myUsers = moviesDB["users"]
	myMovies = moviesDB["movies"]

	for i in range(len(users)):
		myUsers.insert_one(users[i])

	for i in range(len(movies)):
		myMovies.insert_one(movies[i])

setMovies()
setDummyUsers()
setupDatabase()
