-- core sql structure
SELECT
FROM
WHERE
GROUP BY
HAVING
ORDER BY

/* =========================================
   SAMPLE TABLE ASSUMPTIONS
   employees(id, name, dept, salary, manager_id)
   departments(id, name)
   ========================================= */

/* =========================================
   1. BASIC SELECT
   ========================================= */

-- select specific columns
SELECT name, salary
FROM employees;

-- select everything
SELECT *
FROM employees;


/* =========================================
   2. WHERE (filter rows)
   ========================================= */

-- equals
SELECT *
FROM employees
WHERE dept = 'eng';

-- comparisons
SELECT *
FROM employees
WHERE salary > 70000;

SELECT *
FROM employees
WHERE salary >= 50000;

SELECT *
FROM employees
WHERE salary != 60000;

-- multiple conditions
SELECT *
FROM employees
WHERE dept = 'eng' AND salary > 80000;

-- OR
SELECT *
FROM employees
WHERE dept = 'eng' OR dept = 'hr';

-- IN
SELECT *
FROM employees
WHERE dept IN ('eng','hr');

-- BETWEEN
SELECT *
FROM employees
WHERE salary BETWEEN 50000 AND 100000;

-- LIKE (string matching)
SELECT *
FROM employees
WHERE name LIKE 'a%';   -- starts with a

SELECT *
FROM employees
WHERE name LIKE '%a';   -- ends with a


/* =========================================
   3. ORDER BY
   ========================================= */

-- ascending
SELECT *
FROM employees
ORDER BY salary;

-- descending
SELECT *
FROM employees
ORDER BY salary DESC;


/* =========================================
   4. LIMIT (top N)
   ========================================= */

-- top 3 highest salaries
SELECT *
FROM employees
ORDER BY salary DESC
LIMIT 3;


/* =========================================
   5. AGGREGATE FUNCTIONS
   ========================================= */

-- count rows
SELECT COUNT(*)
FROM employees;

-- average salary
SELECT AVG(salary)
FROM employees;

-- min salary
SELECT MIN(salary)
FROM employees;

-- max salary
SELECT MAX(salary)
FROM employees;

-- total salary payout
SELECT SUM(salary)
FROM employees;


/* =========================================
   6. GROUP BY (VERY IMPORTANT)
   ========================================= */

-- count employees per department
SELECT dept, COUNT(*)
FROM employees
GROUP BY dept;

-- average salary per department
SELECT dept, AVG(salary)
FROM employees
GROUP BY dept;


/* =========================================
   7. HAVING (filter groups)
   ========================================= */

-- departments with more than 2 employees
SELECT dept, COUNT(*)
FROM employees
GROUP BY dept
HAVING COUNT(*) > 2;


/* =========================================
   8. JOINS (MOST IMPORTANT)
   ========================================= */

-- INNER JOIN (matching only)
SELECT e.name, d.name
FROM employees e
JOIN departments d
ON e.dept = d.name;

-- LEFT JOIN (keep all employees)
SELECT e.name, d.name
FROM employees e
LEFT JOIN departments d
ON e.dept = d.name;

-- employees without a manager
SELECT *
FROM employees
WHERE manager_id IS NULL;


/* =========================================
   9. ALIASES
   ========================================= */

SELECT e.name, e.salary
FROM employees e;


/* =========================================
   10. INTERVIEW PATTERNS (MEMORIZE)
   ========================================= */

-- duplicates
SELECT name, COUNT(*)
FROM employees
GROUP BY name
HAVING COUNT(*) > 1;

-- second highest salary
SELECT DISTINCT salary
FROM employees
ORDER BY salary DESC
LIMIT 1 OFFSET 1;

-- highest paid per department
SELECT dept, MAX(salary)
FROM employees
GROUP BY dept;

-- total employees per department sorted
SELECT dept, COUNT(*) AS total
FROM employees
GROUP BY dept
ORDER BY total DESC;


/* =========================================
   SQL EXECUTION ORDER (MEMORY TRICK)
   SELECT
   FROM
   JOIN
   WHERE
   GROUP BY
   HAVING
   ORDER BY
   LIMIT
   ========================================= */
