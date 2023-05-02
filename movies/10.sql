SELECT DISTINCT name FROM people, movies, ratings, directors
WHERE people.id = directors.person_id AND movies.id = directors.movie_id
AND movies.id = ratings.movie_id AND rating >= 9.0;