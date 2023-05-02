SELECT title, rating FROM movies, ratings WHERE movies.id = ratings.movie_id
AND year = 2010 GROUP BY title, rating ORDER BY rating DESC;