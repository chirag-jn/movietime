import pymongo as pym
import csv

lengthMovies = 0

class movieNode:
	def __init__(self, key, value):
		self.movieId = key
		self.movieRating = value

	def __lt__(self, other):
		if float(self.movieRating) < float(other.movieRating):
			return True

def user_user(arg_dict):

	myClient = pym.MongoClient("mongodb://admin:Div%401234@movietimebot-shard-00-00-jttos.mongodb.net:27017,movietimebot-shard-00-01-jttos.mongodb.net:27017,movietimebot-shard-00-02-jttos.mongodb.net:27017/test?ssl=true&replicaSet=movietimebot-shard-0&authSource=admin&retryWrites=true")
	moviesDB = myClient["movietime"]
	myUsers = moviesDB["users"]
	myMovies = moviesDB["movies"]

	userRatings = {}

	for x in myUsers.find():
		temp = dict(x)
		values = {temp['imdbId']:temp['rating']}
		if x['userId'] in userRatings.keys():
			userRatings[temp['userId']].append(values)
		else:
			userRatings[temp['userId']] = [values]
	
	newUserId = str(int(list(userRatings.keys())[-1])+1)

	# print(arg_dict)

	new_user = []
	for i in range(len(arg_dict)):
		temp = {'userId': newUserId, 'imdbId': list(arg_dict.keys())[i], 'rating': list(arg_dict.values())[i]}
		new_user.append(temp)
	# new_user = [{'userId': newUserId, 'imdbId': '3682448', 'rating': '5.0'}, {'userId': newUserId, 'imdbId': '2948356', 'rating': '3.5'}, {'userId': newUserId, 'imdbId': '369610', 'rating': '1.0'}, {'userId': newUserId, 'imdbId': '1392190', 'rating': '1.0'}, {'userId': newUserId, 'imdbId': '2395427', 'rating': '4.0'}, {'userId': newUserId, 'imdbId': '2637276', 'rating': '2.0'}]

	# exit()
	similarity = []

	foriegn_mag = []
	for j in range(len(userRatings)):
		temp = []
		ratings = userRatings[list(userRatings.keys())[j]]
		for k in range(len(ratings)):
			vv = float(list(ratings[k].values())[0])
			temp.append(vv*vv)	
		temp_val = sum(temp)
		temp_val = pow(temp_val, 0.5)
		foriegn_mag.append(temp_val)

	myMag = 0

	for i in range(len(new_user)):
		temp = new_user[i]
		cur_movie = temp['imdbId']
		cur_rating = temp['rating']
		myMag += float(cur_rating) * float(cur_rating)

	myMag = pow(myMag, 0.5)

	for j in range(len(userRatings)):
		dot_product = 0
		ratings = userRatings[list(userRatings.keys())[j]]
		for k in range(len(ratings)):
			for i in range(len(new_user)):
				temp = new_user[i]
				cur_movie = temp['imdbId']
				cur_rating = temp['rating']
				if cur_movie in list(ratings[k].keys()):
					dot_product += float(ratings[k][cur_movie])*float(cur_rating)
		if myMag*foriegn_mag[j]!=0:
			similarity.append(dot_product/(myMag*foriegn_mag[j]))
		else:
			similarity.append(0)

	similarity_mod = sum(similarity)

	final_movie_ratings = []

	for x in myMovies.find():
		movie = dict(x)
		value_to_add = 0
		for j in range(len(userRatings)):
			dot_product = 0
			ratings = userRatings[list(userRatings.keys())[j]]
			for k in range(len(ratings)):
				if movie['imdbId'] in list(ratings[k].keys()):
					value_to_add += similarity[j]*float(ratings[k][movie['imdbId']])
		if similarity_mod!=0:
			p1 = movieNode(movie['imdbId'] ,value_to_add/similarity_mod)
		else:
			p1 = movieNode(movie['imdbId'] ,0)
		final_movie_ratings.append(p1)	
	final_movie_ratings.sort()
	return final_movie_ratings[-1].movieId


def item_item():

	myClient = pym.MongoClient("mongodb://admin:Div%401234@movietimebot-shard-00-00-jttos.mongodb.net:27017,movietimebot-shard-00-01-jttos.mongodb.net:27017,movietimebot-shard-00-02-jttos.mongodb.net:27017/test?ssl=true&replicaSet=movietimebot-shard-0&authSource=admin&retryWrites=true")
	moviesDB = myClient["movietime"]
	myUsers = moviesDB["users"]
	myMovies = moviesDB["movies"]

	userRatings = {}

	for x in myUsers.find():
		temp = dict(x)
		# print(temp)
		if(temp['userId'] < '200'):
			values = {temp['imdbId']:temp['rating']}
			if temp['userId'] in userRatings.keys():
				userRatings[temp['userId']].append(values)
			else:
				userRatings[temp['userId']] = [values]

	movieRatings = {}

	for x in myMovies.find():
		temp = dict(x)
		movieRatings[temp['imdbId']] = '0'

	newUserId = str(int(list(userRatings.keys())[-1])+1)

	new_user = [{'userId': newUserId, 'imdbId': '3682448', 'rating': '5.0'}, {'userId': newUserId, 'imdbId': '2948356', 'rating': '3.5'}, {'userId': newUserId, 'imdbId': '369610', 'rating': '1.0'}, {'userId': newUserId, 'imdbId': '1392190', 'rating': '1.0'}, {'userId': newUserId, 'imdbId': '2395427', 'rating': '4.0'}, {'userId': newUserId, 'imdbId': '2637276', 'rating': '2.0'}]

	myMag = 0

	final_movie_ratings = []
	initial_seen = []

	for i in range(len(new_user)):
		temp = new_user[i]
		cur_movie = temp['imdbId']
		cur_rating = temp['rating']
		initial_seen.append(cur_movie)
		movieRatings[cur_movie] = cur_rating
		myMag += float(cur_rating) * float(cur_rating)

	for i in range(len(movieRatings)):
		cur_movie = list(movieRatings.keys())[i]
		if movieRatings[cur_movie]=='0':
			dot_product_1 = {}
			dot_product_1_mag = 0
			for j in range(len(userRatings)):
				ratings = userRatings[list(userRatings.keys())[j]]
				dot_product_1[list(userRatings.keys())[j]] = '0'
				for k in range(len(ratings)):
					if cur_movie in list(ratings[k].keys()):
						dot_product_1[list(userRatings.keys())[j]] = ratings[k][cur_movie]
						# dot_product_1.append(ratings[k][cur_movie])
					# else:
					# 	dot_product_1.append('0')

			for z in range(len(dot_product_1.values())):
				dot_product_1_mag += float(list(dot_product_1.values())[z])*float(list(dot_product_1.values())[z])
			dot_product_1_mag = pow(dot_product_1_mag, 0.5)

			# print(dot_product_1)
			# exit()
			cosine_array = []

			for j in range(len(movieRatings)):
				check_movie = list(movieRatings.keys())[j]
				if(movieRatings[check_movie]!='0'):
					dot_product_2 = {}
					for jj in range(len(userRatings)):
						ratings = userRatings[list(userRatings.keys())[jj]]
						dot_product_2[list(userRatings.keys())[jj]] = '0'
						for k in range(len(ratings)):
							if check_movie in list(ratings[k].keys()):
								dot_product_2[list(userRatings.keys())[jj]] = ratings[k][check_movie]
								# dot_product_2.append(ratings[k][check_movie])
							# else:
							# 	dot_product_2.append('0')
					# print(dot_product_2)
					# exit()
					dot_product_2_mag = 0
					dot_product_3 = 0
					# print(dot_product_1)
					for z in range(len(dot_product_1)): 
						dot_product_3 += float(list(dot_product_1.values())[z])*float(list(dot_product_2.values())[z])
						dot_product_2_mag += float(list(dot_product_1.values())[z])*float(list(dot_product_1.values())[z])
					dot_product_2_mag = pow(dot_product_2_mag, 0.5)
					# print(dot_product_1_mag)
					# print(dot_product_2_mag)
					# exit()
					# print(dot_product_1.values())
					# print(dot_product_2.values())
					# print(dot_product_3)
					# exit()
					if(dot_product_1_mag*dot_product_2_mag > 0):
						p1 = movieNode(check_movie, dot_product_3/(dot_product_1_mag*dot_product_2_mag))
					else:
						p1 = movieNode(check_movie, 0)
					cosine_array.append(p1)
			# print(cosine_array)
			cosine_array.sort()
			# print(cosine_array[0].movieId)
			# exit()
			# print(cosine_array[-2].movieId)
			# print(float(movieRatings[cosine_array[-1].movieId]))
			if (float(cosine_array[-2].movieRating)+float(cosine_array[-1].movieRating)) > 0:
				# print((float(movieRatings[cosine_array[-2].movieId])*float(cosine_array[-2].movieRating)+float(movieRatings[cosine_array[-1].movieId])*float(cosine_array[-1].movieRating))/(float(cosine_array[-2].movieRating)+float(cosine_array[-1].movieRating)))
				movieRatings[cur_movie] = str((float(movieRatings[cosine_array[-2].movieId])*float(cosine_array[-2].movieRating)+float(movieRatings[cosine_array[-1].movieId])*float(cosine_array[-1].movieRating))/(float(cosine_array[-2].movieRating)+float(cosine_array[-1].movieRating)))
			else:
				movieRatings[cur_movie] = '0'

	toShow = []

	for i in range(len(movieRatings)):
		temp_movie = list(movieRatings.keys())[i]
		if temp_movie not in initial_seen:
			p1 = movieNode(temp_movie, movieRatings[temp_movie])
			toShow.append(p1)

	toShow.sort()
	print(toShow[-2].movieId)
	# print(tos)

	exit()

	# similarity = []

	# foriegn_mag = []
	# for j in range(len(userRatings)):
	# 	temp = []
	# 	ratings = userRatings[list(userRatings.keys())[j]]
	# 	for k in range(len(ratings)):
	# 		vv = float(list(ratings[k].values())[0])
	# 		temp.append(vv*vv)	
	# 	temp_val = sum(temp)
	# 	temp_val = pow(temp_val, 0.5)
	# 	foriegn_mag.append(temp_val)

	# print(movieRatings)

	# exit()

	# myMag = pow(myMag, 0.5)

	# for j in range(len(userRatings)):
	# 	dot_product = 0
	# 	ratings = userRatings[list(userRatings.keys())[j]]
	# 	for k in range(len(ratings)):
	# 		for i in range(len(new_user)):
	# 			temp = new_user[i]
	# 			cur_movie = temp['imdbId']
	# 			cur_rating = temp['rating']
	# 			if cur_movie in list(ratings[k].keys()):
	# 				dot_product += float(ratings[k][cur_movie])*float(cur_rating)
	# 	similarity.append(dot_product/(myMag*foriegn_mag[j]))

	# similarity_mod = sum(similarity)

	# final_movie_ratings = []

	# for x in myMovies.find():
	# 	movie = dict(x)
	# 	value_to_add = 0
	# 	for j in range(len(userRatings)):
	# 		dot_product = 0
	# 		ratings = userRatings[list(userRatings.keys())[j]]
	# 		for k in range(len(ratings)):
	# 			if movie['imdbId'] in list(ratings[k].keys()):
	# 				value_to_add += similarity[j]*float(ratings[k][movie['imdbId']])

	# 	p1 = movieNode(movie['imdbId'] ,value_to_add/similarity_mod)
	# 	final_movie_ratings.append(p1)
	# final_movie_ratings.sort()
	# print(final_movie_ratings[-1].movieId)

# user_user()
# item_item()