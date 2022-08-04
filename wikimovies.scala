/*
wikimovies.scala
reads in the wikipedia movies dataset, filters on year=2018 and genre='Drama', and saves the result as a .json
*/

/* read wikimovies data from url and format as a dataframe */
val url = "https://raw.githubusercontent.com/prust/wikipedia-movie-data/master/movies.json"
spark.sparkContext.addFile(url)
import org.apache.spark.SparkFiles
val df = spark.read.json("file://"+SparkFiles.get("movies.json"))

/* select records where the 'genre' array contains 'Drama' and the 'year equals 2018 */
val df_2018_drama = df.where(array_contains(col("genres"),"Drama") && (col("year") === 2018))

/* write result to a .json file */
df_2018_drama.write.json("wikimovies_2018_drama")

