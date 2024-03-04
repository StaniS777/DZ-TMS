--task 1

CREATE TABLE authors(
id SERIAL PRIMARY KEY,
first_name TEXT,
last_name TEXT);

INSERT INTO authors (first_name, last_name)
VALUES
('Alex', 'Ivanov'),
('Ivan', 'Petrov'),
('Viktor', 'Eskov'),
('Petr', 'Alexeev');

CREATE TABLE books(
id SERIAL PRIMARY KEY,
title TEXT,
author_id INTEGER REFERENCES authors(id),
publication_year TEXT);

CREATE TABLE sales(
id SERIAL PRIMARY KEY,
book_id INTEGER REFERENCES books(id),
quantity INTEGER);

INSERT INTO books (title, author_id, publication_year)
VALUES
('Harry Potter', 2, '1997'),
('The Little Prince', 1, '1943'),
('Peter Pan', 3, '1904'),
('War and Peace', NULL, '1868'),
('Harry Potter 2', 2, '1999'),
('Harry Potter 3', 2, '2001'),
('The Little Prince 2', 1, '1945'),
('The Little Prince 3', 1, '1948');


INSERT INTO sales (book_id, quantity)
VALUES
(1, 60),
(2, 90),
(3, 420);

-- task 2

SELECT a.first_name AS FIRST_NAME, a.last_name AS LAST_NAME, b.title AS TITLE
FROM authors a
INNER JOIN books b ON b.author_id=a.id;

SELECT a.first_name AS FIRST_NAME, a.last_name AS LAST_NAME, b.title AS TITLE
FROM authors a
LEFT JOIN books b ON b.author_id=a.id;

SELECT a.first_name AS FIRST_NAME, a.last_name AS LAST_NAME, b.title AS TITLE
FROM authors a
RIGHT JOIN books b ON b.author_id=a.id;

-- task 3

SELECT a.first_name AS FIRST_NAME,
a.last_name AS LAST_NAME,
b.title AS TITLE,
s.quantity AS COST
FROM authors a
INNER JOIN books b ON b.author_id=a.id
INNER JOIN sales s ON b.author_id=s.book_id;

SELECT a.first_name AS FIRST_NAME,
a.last_name AS LAST_NAME,
b.title AS TITLE,
s.quantity AS COST
FROM authors a
FULL JOIN books b ON b.author_id=a.id
FULL JOIN sales s ON b.author_id=s.book_id;


-- task 4

SELECT a.first_name AS first_name,
a.last_name AS last_name,
SUM(s.quantity)
FROM authors a
INNER JOIN books b ON b.author_id=a.id
INNER JOIN sales s ON b.author_id=s.book_id
GROUP BY a.first_name, a.last_name;

SELECT a.first_name AS first_name,
a.last_name AS last_name,
SUM(s.quantity)
FROM authors a
LEFT JOIN books b ON b.author_id=a.id
LEFT JOIN sales s ON b.author_id=s.book_id
GROUP BY a.first_name, a.last_name;

-- task 5

SELECT a.first_name AS first_name,
a.last_name AS last_name,
SUM(s.quantity)
FROM authors a
INNER JOIN books b ON b.author_id=a.id
INNER JOIN sales s ON b.author_id=s.book_id
GROUP BY a.first_name, a.last_name
ORDER BY SUM(s.quantity) DESC
LIMIT 1;

SELECT AVG(sales.quantity) FROM sales;

SELECT a.first_name,
a.last_name,
AVG(s.quantity) AS quantity
FROM authors a
JOIN sales s ON s.book_id=a.id
GROUP BY a.first_name, a.last_name
HAVING AVG(s.quantity) > (
SELECT AVG(sales.quantity) FROM sales
);


