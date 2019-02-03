# Movie Time
## Project for Precog Application

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
7. Data presetn at /data/movieRatings