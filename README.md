# WikiMovies_slapp

a small & simple streamlit app to explore the [Wikipedia Movies dataset](https://raw.githubusercontent.com/prust/wikipedia-movie-data/master/movies.json)

The code in `app.py` does the following:
1. Load the json file into a Pandas dataframe
2. Generates a table showing the number of movies made in each year and also a visualization
3. Generates a dictionary which maps each genre to a list of movies. it then: 
  * shows a table with the number of movies in each genre
  * a corresponding bar chart
  * lets the user select a genre and view a list of movei titles
4. Generates a dictionary which maps each genre to a list of actors and actresses for a given year.
  * the user can select a year and genre of interest
  * shows a table with the number of actors/actresses per genre for the selected year
  * shows a list of actors and actresses names for the selected year & genre
  * the default values are 2018 'Drama'
  
The app has been containerized with Docker and pushed to a public ECR repo
