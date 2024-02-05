CREATE TABLE employees(id SERIAL PRIMARY KEY, Name TEXT, Position TEXT, Departament TEXT, Salary TEXT);

INSERT INTO employees (Name, Position, Departament, Salary) VALUES
('Alex', 'ingineer', 'OGT', '2000'),
('Ivan', 'ingineer', 'YGK', '2200'),
('Viktor', 'master', 'CMS', '1500'),
('Maxim', 'turner', 'CMS', '2500');

UPDATE employees
SET position='engineer category 2'
WHERE position='ingineer';

ALTER TABLE employees
ADD hiredate TEXT;

UPDATE employees
SET hiredate='03.08.2018'
WHERE name='Alex';

UPDATE employees
SET hiredate='12.05.2015'
WHERE name='Ivan';

UPDATE employees
SET hiredate='23.03.2010'
WHERE name='Viktor';

UPDATE employees
SET hiredate='01.06.2024'
WHERE name='Maxim';

SELECT * FROM employees
WHERE position='engineer category 2';

SELECT * FROM employees
WHERE salary>='2000';

SELECT * FROM employees
WHERE departament='CMS';

SELECT CAST(AVG(CAST(salary AS INTEGER))AS INTEGER) as SALARY_AVG FROM employees;

DROP TABLE employees;