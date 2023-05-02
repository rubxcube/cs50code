SELECT title FROM people, movies, ratings, stars
WHERE people.id = stars.person_id AND movies.id = stars.movie_id
AND movies.id = ratings.movie_id AND name = 'Chadwick Boseman' ORDER BY rating DESC LIMIT 5;