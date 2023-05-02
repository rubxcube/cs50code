SELECT name FROM people, movies, stars
WHERE people.id = stars.person_id AND movies.id = stars.movie_id
AND movies.id IN (SELECT movies.id FROM people, movies, stars
WHERE people.id = stars.person_id AND movies.id = stars.movie_id
AND name = 'Kevin Bacon' AND birth = 1958) AND name != 'Kevin Bacon';