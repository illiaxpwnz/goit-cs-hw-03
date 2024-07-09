SELECT * FROM tasks WHERE user_id = 1;

SELECT * FROM tasks WHERE status_id = (SELECT id FROM status WHERE name = 'new');

UPDATE tasks SET status_id = (SELECT id FROM status WHERE name = 'in progress') WHERE id = 1;

SELECT * FROM users WHERE id NOT IN (SELECT DISTINCT user_id FROM tasks);

INSERT INTO tasks (title, description, status_id, user_id) VALUES ('Jump ', 'Jump on one feet', 1, 2);

SELECT * FROM tasks WHERE status_id != (SELECT id FROM status WHERE name = 'completed');

DELETE FROM tasks WHERE id = 41;

SELECT * FROM users WHERE email LIKE '%@example.com';

UPDATE users SET fullname = 'Michael Scott' WHERE id = 2;

SELECT s.name, COUNT(t.id) AS task_count FROM status s LEFT JOIN tasks t ON s.id = t.status_id GROUP BY s.name;

SELECT t.* FROM tasks t JOIN users u ON t.user_id = u.id WHERE u.email LIKE '%@example.com';

SELECT * FROM tasks WHERE description IS NULL OR description = '';

SELECT u.fullname, t.title, t.description FROM users u JOIN tasks t ON u.id = t.user_id JOIN status s ON t.status_id = s.id WHERE s.name = 'in progress';

SELECT u.fullname, COUNT(t.id) AS task_count FROM users u LEFT JOIN tasks t ON u.id = t.user_id GROUP BY u.fullname;
