# Movie Time
## Project for Precog Application

## Project

### Website
https://movietimebot.herokuapp.com/

### Local Machine
```
sudo python3 -m pip install -r requirements.txt
python3 run.py
```
Go to http://localhost:5000/

## Data Acquisition

### IMDB API
1. Using OMDb API (The Open Movie Database), RESTful web service to
obtain movie information from IMDb.
2. http://www.omdbapi.com/
3. API Key authenticated under free account for chiragjn120@gmail.com
4. http://www.omdbapi.com/?i=tt3896198&apikey=7ac1f872

### Dataset
1. Using Movietime dataset.
2. 100,000 ratings and 3,600 tag applications applied to 9,000 movies by 600 users. Last updated 9/2018.
3. No need to create dummy users since we already have a dataset created with ratings done by 600 users.
4. Movietime states that "These datasets will change over time, and are not appropriate for reporting research results."
5. Since this dataset is sufficient for a proof of concept, we will use this dataset only.
6. Dataset Used: http://files.grouplens.org/datasets/movielens/ml-latest-small-README.html
7. Original Data present at /scripts/data/movieRatings

### Modification of Dataset
1. The movieset which we are using has a lot of data which we don't need so we have to extract the required data from the dataset.
2. The modification of dataset is done in the script modifyData.py present under /scripts
3. generateIMDBLinks() function extracts the movieID (for OMDb Dataset) and IMDbID for all movies present in the dataset which were released in the years 2017.
4. generateRatings() function extracts the ratings of multiple users who rated the movies which were extracted using the previous function.
5. This data works as our data for dummy users which will be used in the Collaborative Filtering algorithm.
6. getDetailsFromID() function results in the JSON response for each movie's data from the OMDb website.

## Movie Recommendation System

### Collaborative Filtering Algorithms
1. Movies are recommended on the basis of User's ratings using both User based Collaborative filtering and Item based Collaborate filtering.
2. The algorithms are implemented in data/recommender.py
3. User Based Collaborative Filtering is written in user_user() function.
4. Item Based Collaborative Filtering is written in item_item() function.
5. Reference: https://towardsdatascience.com/various-implementations-of-collaborative-filtering-100385c6dfe0

## Deployment
1. The project is deployed on Heroku at: https://movietimebot.herokuapp.com/
2. The database is hosted on MongoDb Atlas