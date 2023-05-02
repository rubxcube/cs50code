SELECT title FROM movies WHERE id IN (SELECT movies.id FROM people, movies, stars
WHERE people.id = stars.person_id AND movies.id = stars.movie_id
AND name = 'Johnny Depp') AND id IN (SELECT movies.id FROM people, movies, stars
WHERE people.id = stars.person_id AND movies.id = stars.movie_id
AND name = 'Helena Bonham Carter');