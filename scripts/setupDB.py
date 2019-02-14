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
		for row in movies_reader:
			if line_count == 0:
				tag1 = row[0]
				tag2 = row[1]
				tag3 = row[2]
				tag4 = row[3]
				tag5 = row[4]				
				line_count += 1
			else:
				tempDict = {tag1:row[0], tag2:row[1], tag3:row[2], tag4:row[3], tag5:row[4]}
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
				# movieIDs.append(row[1])
				line_count += 1

# setMovies()

def setupDatabase():
	global users
	global movies
	myClient = pym.MongoClient("mongodb://localhost:27017")
	moviesDB = myClient["movietime"]
	myUsers = moviesDB["users"]
	myMovies = moviesDB["movies"]
	# mydict = { "name": "John", "address": "Highway 37" }
	# something=['chirag']
	# print(users)
	for i in range(len(users)):
		myUsers.insert_one(users[i])

	for i in range(len(movies)):
		myMovies.insert_one(movies[i])

	# myUsers.insert_one(something)

setMovies()
setDummyUsers()
setupDatabase()

# myCol.insert_one(mydict)

# print(myClient.list_database_names())
# time.sleep(5)