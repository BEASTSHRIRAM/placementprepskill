# DBMS Reference -- Database Management Systems

## ACID Properties

**Atomicity**: A transaction is all-or-nothing. If any step fails, the entire transaction is rolled back.
**Consistency**: A transaction brings the database from one valid state to another. Constraints and rules are always satisfied.
**Isolation**: Concurrent transactions execute as if they were serial. Changes made by a transaction are not visible to others until committed.
**Durability**: Once committed, a transaction persists even in the case of system failure. Achieved via write-ahead logging.

---

## Normalization

Organizing tables to reduce redundancy and improve data integrity.

**1NF (First Normal Form)**
- Each column contains atomic (indivisible) values
- No repeating groups or arrays in any column
- Each row is unique

**2NF (Second Normal Form)**
- Must be in 1NF
- No partial dependency: every non-key attribute must depend on the entire primary key (relevant when primary key is composite)

**3NF (Third Normal Form)**
- Must be in 2NF
- No transitive dependency: non-key attributes should not depend on other non-key attributes

**BCNF (Boyce-Codd Normal Form)**
- Stricter than 3NF
- For every functional dependency X -> Y, X must be a superkey

**Denormalization**: intentionally introducing redundancy for performance (fewer joins, faster reads). Used in data warehouses and analytics.

---

## SQL Must-Know Queries

```sql
-- Basic SELECT
SELECT name, salary FROM employees WHERE department = 'Engineering' ORDER BY salary DESC;

-- GROUP BY and HAVING
SELECT department, COUNT(*) as emp_count, AVG(salary) as avg_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 50000;

-- JOINS
SELECT e.name, d.department_name
FROM employees e
INNER JOIN departments d ON e.dept_id = d.id;

-- LEFT JOIN (includes unmatched rows from left table)
SELECT e.name, d.department_name
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.id;

-- Subquery
SELECT name FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

-- Second Highest Salary
SELECT MAX(salary) FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);

-- Using ROW_NUMBER or RANK
SELECT name, salary, RANK() OVER (ORDER BY salary DESC) as rnk
FROM employees;

-- Nth highest salary using DENSE_RANK
SELECT salary FROM (
    SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) as rnk FROM employees
) ranked
WHERE rnk = 2;

-- Find duplicate records
SELECT email, COUNT(*) FROM employees GROUP BY email HAVING COUNT(*) > 1;

-- Self Join (manager and employee in same table)
SELECT e.name as employee, m.name as manager
FROM employees e
JOIN employees m ON e.manager_id = m.id;

-- EXISTS
SELECT name FROM employees e
WHERE EXISTS (SELECT 1 FROM orders o WHERE o.employee_id = e.id);

-- UPDATE with JOIN
UPDATE employees SET salary = salary * 1.1
WHERE department_id IN (SELECT id FROM departments WHERE name = 'Engineering');
```

---

## Indexing

**What is an index?** A data structure that improves the speed of data retrieval operations. Works like a book index.

**B-Tree Index**: most common. Balanced tree structure. Efficient for range queries and equality checks. O(log n) search.

**Hash Index**: faster for exact equality lookups (O(1)), but cannot be used for range queries.

**Clustered Index**: determines the physical order of data in the table. Only one per table. In MySQL InnoDB, the primary key is the clustered index.

**Non-Clustered Index**: separate structure that points to the actual data rows. Multiple allowed per table.

**Tradeoffs**
- Indexes speed up SELECT queries
- Indexes slow down INSERT, UPDATE, DELETE (index must be maintained)
- Indexes consume additional storage

**When to index**: columns used in WHERE, JOIN ON, ORDER BY, GROUP BY clauses; columns with high cardinality (many distinct values).

---

## Transactions and Isolation Levels

**Isolation Levels (from lowest to highest)**

| Level | Dirty Read | Non-Repeatable Read | Phantom Read |
|---|---|---|---|
| Read Uncommitted | Possible | Possible | Possible |
| Read Committed | Not Possible | Possible | Possible |
| Repeatable Read | Not Possible | Not Possible | Possible |
| Serializable | Not Possible | Not Possible | Not Possible |

**Dirty Read**: reading uncommitted data from another transaction.
**Non-Repeatable Read**: reading same row twice and getting different values (another transaction updated it in between).
**Phantom Read**: re-running a query and getting different rows (another transaction inserted/deleted rows in between).

---

## NoSQL vs SQL

| Aspect | SQL (Relational) | NoSQL |
|---|---|---|
| Schema | Fixed schema | Schema-less or flexible |
| Data model | Tables with rows and columns | Document, Key-Value, Column-family, Graph |
| ACID | Full ACID support | Often eventual consistency (BASE) |
| Scaling | Vertical scaling (primarily) | Horizontal scaling |
| Joins | Native, efficient | Limited or not supported |
| Use cases | Banking, ERP, transactional systems | Social media, real-time analytics, IoT |
| Examples | MySQL, PostgreSQL, Oracle | MongoDB, Cassandra, Redis, DynamoDB |

**CAP Theorem**: a distributed system can guarantee at most two of Consistency, Availability, Partition Tolerance.

---

## Common Interview Questions

1. What is the difference between WHERE and HAVING?
2. What is a primary key vs a foreign key vs a unique key?
3. What is the difference between DELETE, TRUNCATE, and DROP?
4. What is a stored procedure? A trigger? A view?
5. What are the different types of joins?
6. Explain normalization with an example.
7. What is a transaction? What are its properties?
8. What is a deadlock in databases? How is it handled?
9. What is the difference between clustered and non-clustered index?
10. When would you choose NoSQL over SQL?
11. What is sharding in databases?
12. What is connection pooling?
13. Explain the difference between optimistic and pessimistic locking.
14. What is a cursor in SQL?
15. What is the N+1 query problem and how do you avoid it?


---

## SQL Practice Set

Schema (used by all queries below):
```sql
Department(id INT PK, name VARCHAR)
Employee(id INT PK, name VARCHAR, salary INT, email VARCHAR, manager_id INT NULL, dept_id INT FK -> Department.id)
```

**1. Second highest salary** (returns NULL if none)
```sql
SELECT (SELECT DISTINCT salary FROM Employee ORDER BY salary DESC LIMIT 1 OFFSET 1) AS second_highest;
```

**2. Nth highest salary** (n = 3 here; DENSE_RANK handles ties)
```sql
SELECT DISTINCT salary FROM (
    SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk FROM Employee
) t WHERE rnk = 3;
```

**3. Find duplicates** (by email)
```sql
SELECT email, COUNT(*) AS cnt FROM Employee GROUP BY email HAVING COUNT(*) > 1;
```

**4. Delete duplicates** (keep lowest id)
```sql
DELETE e1 FROM Employee e1
JOIN Employee e2 ON e1.email = e2.email AND e1.id > e2.id;   -- MySQL
-- Standard SQL (e.g. PostgreSQL):
-- DELETE FROM Employee WHERE id NOT IN (SELECT MIN(id) FROM Employee GROUP BY email);
-- MySQL rejects that form unless the subquery is wrapped in a derived table.
```

**5. Employees earning more than their manager**
```sql
SELECT e.name FROM Employee e JOIN Employee m ON e.manager_id = m.id WHERE e.salary > m.salary;
```

**6. Department-wise max salary** (with department name)
```sql
SELECT d.name, MAX(e.salary) AS max_salary
FROM Department d JOIN Employee e ON e.dept_id = d.id GROUP BY d.id, d.name;
```

**7. Top N per group** (top 3 salaries per department)
```sql
SELECT * FROM (
    SELECT e.name, e.dept_id, e.salary,
           DENSE_RANK() OVER (PARTITION BY e.dept_id ORDER BY e.salary DESC) AS rnk
    FROM Employee e
) t WHERE rnk <= 3;
```
- ROW_NUMBER: unique 1,2,3,4 (ties broken arbitrarily). RANK: 1,1,3,4 (gaps). DENSE_RANK: 1,1,2,3 (no gaps).

**8. Running total**
```sql
SELECT name, salary, SUM(salary) OVER (ORDER BY id) AS running_total FROM Employee;
```

**9. JOIN types demo**
```sql
SELECT e.name, d.name FROM Employee e INNER JOIN Department d ON e.dept_id = d.id;   -- matches only
SELECT e.name, d.name FROM Employee e LEFT JOIN Department d ON e.dept_id = d.id;    -- all employees
SELECT e.name, d.name FROM Employee e RIGHT JOIN Department d ON e.dept_id = d.id;   -- all departments
SELECT e.name, d.name FROM Employee e LEFT JOIN Department d ON e.dept_id = d.id
UNION
SELECT e.name, d.name FROM Employee e RIGHT JOIN Department d ON e.dept_id = d.id;   -- FULL OUTER (MySQL)
SELECT e.name, d.name FROM Employee e CROSS JOIN Department d;                       -- cartesian product
```
- Departments with no employees: LEFT JOIN from Department and filter `WHERE e.id IS NULL`.

**10. GROUP BY vs HAVING**
```sql
SELECT dept_id, COUNT(*) AS cnt FROM Employee
WHERE salary > 30000          -- WHERE filters rows before grouping
GROUP BY dept_id
HAVING COUNT(*) > 5;          -- HAVING filters groups after aggregation
```

**11. EXISTS vs IN**
```sql
SELECT name FROM Department d WHERE EXISTS (SELECT 1 FROM Employee e WHERE e.dept_id = d.id);
SELECT name FROM Department WHERE id IN (SELECT dept_id FROM Employee);
```
- EXISTS stops at first match and is NULL-safe; usually better for large inner tables. NOT IN returns no rows if the subquery contains NULL, so prefer NOT EXISTS.

**12. Self join and LEAD/LAG**
```sql
-- Self join: pairs in same department
SELECT a.name, b.name FROM Employee a JOIN Employee b ON a.dept_id = b.dept_id AND a.id < b.id;

-- LAG/LEAD: compare each salary with previous/next in department
SELECT name, salary,
       LAG(salary, 1)  OVER (PARTITION BY dept_id ORDER BY salary) AS prev_salary,
       LEAD(salary, 1) OVER (PARTITION BY dept_id ORDER BY salary) AS next_salary
FROM Employee;
```
