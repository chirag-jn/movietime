import csv
from collectData import getData

def generateIMDBLinks():
	movieIDs = []
	with open('data/movieRatings/originalData/movies.csv') as movies_file:
		movies_reader = csv.reader(movies_file, delimiter=',')
		line_count = 0
		for row in movies_reader:
			if '2015' in row[1] or '2016' in row[1] or '2017' in row[1] or '2018' in row[1]:
				movieIDs.append(row[0])
			line_count += 1
	with open('data/movieRatings/movieIDs2.csv', mode='w') as movieID_file:
		movieID_writer = csv.writer(movieID_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		with open('data/movieRatings/originalData/links.csv') as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			line_count = 0
			for row in csv_reader:
				if line_count == 0:
					print(f'Column names are {", ".join(row)}')
					movieID_writer.writerow([row[0],row[1]])
					line_count += 1
				else:
					if row[0] in movieIDs:
						movieID_writer.writerow([row[0],row[1]])
					line_count += 1

def generateRatings():
	movieIDtoIMDbID = {}
	with open('data/movieRatings/movieIDs2.csv') as movieID_file:
		movieID_reader = csv.reader(movieID_file, delimiter=',')
		line_count = 0
		for row in movieID_reader:
			if line_count == 0:
				line_count += 1
			else:
				movieIDtoIMDbID[row[0]] = row[1]
				line_count += 1		

	with open('data/movieRatings/ratings2.csv', mode='w') as ratings_file:
		ratings_writer = csv.writer(ratings_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		with open('data/movieRatings/originalData/ratings.csv') as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			line_count = 0
			for row in csv_reader:
				if line_count == 0:
					print(f'Column names are {", ".join(row)}')
					ratings_writer.writerow([row[0],"imdbId",row[2]])
					line_count += 1
				else:
					if row[1] in movieIDtoIMDbID.keys():
						ratings_writer.writerow([row[0],movieIDtoIMDbID[row[1]], row[2]])
						line_count += 1

def getDetailsFromID():
	movieIDs = []
	with open('data/movieRatings/movieIDs.csv') as movieID_file:
		movieID_reader = csv.reader(movieID_file, delimiter=',')
		line_count = 0
		for row in movieID_reader:
			if line_count == 0:
				line_count += 1
			else:
				movieIDs.append(row[1])
				line_count += 1
	with open('data/movieRatings/movieData2.csv', mode='w') as movieData_file:
		movieData_writer = csv.writer(movieData_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		for i in range(len(movieIDs)):
			print(i)
			movieData_writer.writerow([getData(movieIDs[i])])
	
generateIMDBLinks()
generateRatings()
getDetailsFromID()