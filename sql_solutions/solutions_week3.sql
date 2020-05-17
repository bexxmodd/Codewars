/* Adults only (SQL for Beginners #1) */
SELECT
  name,
  age
FROM users
WHERE age >= 18;


/* On the Canadian Border (SQL for Beginners #2) */
SELECT
  name,
  country
FROM travelers
WHERE country NOT IN ('Canada', 'Mexico', 'USA');


/* Register for the Party (SQL for Beginners #3) */
INSERT INTO participants (name, age, attending)
VALUES ('Bexx', 28, True);

SELECT * FROM participants;


/* Collect Tuition (SQL for Beginners #4) */
SELECT * FROM students
WHERE tuition_received = False;

/* Best-Selling Books (SQL for Beginners #5) */
SELECT
  name,
  author,
  copies_sold
FROM books
ORDER BY copies_sold DESC
LIMIT 5;

/* Countries Capitals for Trivia Night (SQL for Beginners #6) */
SELECT
  capital
FROM countries
WHERE continent SIMILAR TO 'Afri(k|c)a'
    AND country LIKE 'E%'
ORDER BY capital
LIMIT 3;