## SQL Operations Using pgAdmin

This assignment demonstrates creating database tables, inserting records, querying data, updating records, and deleting records using PostgreSQL and pgAdmin.

### A. Create Tables

Create the `users` table:

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

Create the `calculations` table:

```sql
CREATE TABLE calculations (
    id SERIAL PRIMARY KEY,
    operation VARCHAR(20) NOT NULL,
    operand_a FLOAT NOT NULL,
    operand_b FLOAT NOT NULL,
    result FLOAT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
```

### B. Insert Records

Insert users:

```sql
INSERT INTO users (username, email)
VALUES
('alice', 'alice@example.com'),
('bob', 'bob@example.com');
```

Insert calculations:

```sql
INSERT INTO calculations
(operation, operand_a, operand_b, result, user_id)
VALUES
('add', 2, 3, 5, 1),
('divide', 10, 2, 5, 1),
('multiply', 4, 5, 20, 2);
```

### C. Query Data

Retrieve all users:

```sql
SELECT * FROM users;
```

Retrieve all calculations:

```sql
SELECT * FROM calculations;
```

Join users and calculations:

```sql
SELECT
    u.username,
    c.operation,
    c.operand_a,
    c.operand_b,
    c.result
FROM calculations c
JOIN users u ON c.user_id = u.id;
```

### D. Update a Record

Update the result of calculation ID 1:

```sql
UPDATE calculations
SET result = 6
WHERE id = 1;
```

### E. Delete a Record

Delete calculation ID 2:

```sql
DELETE FROM calculations
WHERE id = 2;
```

### Database Relationships

The database contains a one-to-many relationship between the `users` and `calculations` tables. Each user has a unique primary key, and the `user_id` foreign key in the calculations table connects each calculation to its corresponding user. The `ON DELETE CASCADE` constraint allows associated calculations to be deleted when their parent user is deleted.